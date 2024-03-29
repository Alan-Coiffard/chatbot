from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
import pickle

import psycopg2

# Define your database connection parameters
db_params = {
    "database": "chatBot",
    "user": "postgres",
    "password": "root",
    "host": "localhost",  # Use "localhost" if the database is on your local machine
    "port": "5432",  # Typically 5432 for PostgreSQL
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print(f"Connected")
except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")

# Create a table for quotes and embeddings if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS Quotes (
        Quote_ID SERIAL PRIMARY KEY,
        Quote_Text TEXT,
        Quote_Embedding BYTEA
    )
'''
cursor.execute(create_table_query)
conn.commit()

def ligne_existe_dans_fichier(nom_fichier, ligne_recherchee):
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            # Supprime les espaces blancs à gauche et à droite pour éviter les fausses correspondances
            if ligne.strip() == ligne_recherchee:
                return True
    return False

#Our sentences we like to encode
sentences = []
with open('sentences.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not ligne_existe_dans_fichier("sentences_in_db.txt", line):
            print('La ligne existe dans le fichier.')
            sentences.append(line)
        

#Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences)
quotes_and_embeddings = []

#Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("type:", type(embedding))
    print("")
    # Insert the data into the Quotes table
    insert_query = "INSERT INTO Quotes (Quote_Text, Quote_Embedding) VALUES (%s, %s::BYTEA)"
    pickle_string = pickle.dumps(embedding)
    quote_and_embedding = (sentence, pickle_string)
    
    cursor.execute(insert_query, quote_and_embedding)
    conn.commit()
    with open("sentences_in_db.txt", "a") as myfile:
        print("Ajout dans indb"+ sentence)
        myfile.write(sentence + "\n")


#Print number of sentences
print("Total of sentences:", len(sentences))

# Close the cursor and the database connection
cursor.close()
conn.close()
