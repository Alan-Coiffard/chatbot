from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

#Our sentences we like to encode
sentences = []
# Open the file in read mode
with open('sentences.txt', 'r') as file:
    for line in file:
        line = line.strip()
        sentences.append(line)

#Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences)


#Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
    
#Print number of sentences
print("Total of sentences:", len(sentences))
