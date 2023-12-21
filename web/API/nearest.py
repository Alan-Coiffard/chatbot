import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
import pickle

# Function to calculate Euclidean distance between two vectors
def euclidean_distance(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)

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
    print("Connected")
except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")
    exit()

def select_question(text):
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        print("Connected")
    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        exit()
    # Retrieve all sentences and their embeddings from the database
    select_query = "SELECT Quote_ID, Quote_Text, Quote_Embedding FROM Quotes"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    if not rows:
        print("No sentences found in the database.")
        cursor.close()
        conn.close()
        return "No sentences found in the database."
    else:
        # Parse the database data
        sentences = [row[1] for row in rows]
        embeddings = [np.array(pickle.loads(row[2]))  for row in rows]

        # Calculate Euclidean distances and find the nearest sentence
        min_distance = float('inf')
        nearest_sentence = None

        input_embedding = model.encode(text)  # Replace with your input embedding

        for i, embedding in enumerate(embeddings):
            distance = euclidean_distance(input_embedding, embedding)
            print(f"distance: {distance}")
            if distance < min_distance:
                min_distance = distance
                nearest_sentence = sentences[i]

        # Display the nearest sentence
        print(f"Nearest sentence in the database: {nearest_sentence}")
        return nearest_sentence
