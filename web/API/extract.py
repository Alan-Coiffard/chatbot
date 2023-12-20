# Use a pipeline as a high-level helper
from transformers import pipeline
import re


symptoms=[]
text = """
My name is Alan Coiffard. 
I have a phase 2 skin cancer. 
My arm hurts, I've got a fever, I've been throwing up, I feel dizzie. 
what should I do ?
"""

text2 = """
My name is Alan Coiffard. 
I have a phase 2 skin cancer. 
My arm hurt and I've got a fever and I've been throwing up and I have some diarrhea.  
what should I do ?
"""

text3 = """
My name is Alan Coiffard. 
I have a phase 2 skin cancer. 
I have 40,5 temperature.
what should I do ?
"""
text4 = """
My name is Alan Coiffard. 
I have a phase 2 skin cancer. 
I have 39°c temperature.
what should I do ?
"""


# pipe = pipeline("token-classification", model="medical-ner-proj/albert-medical-ner-proj")

# out = pipe(text)
# for entity in out:
#     print(f"Entity: {entity['entity']}")
#     print(f"Score: {entity['score']}")
#     print(f"Word: {entity['word']}")
#     print(f"Start: {entity['start']}")
#     print(f"End: {entity['end']}")
#     print("-------------------")

def extract_symptoms(text):
    res=[]
    pipe = pipeline("token-classification", model="silpakanneganti/bert-medical-ner")
    out = pipe(text)
    for x in out:
        if x['entity'] == "B-Sign_symptom" and "#" not in x['word']:
            res.append(x)
    return res
    
def extract_cancer_type(text):
    res=[]
    pipe = pipeline("token-classification", model="DrM/BERT_Cancer_type_extraction2")
    out = pipe(text)
    for x in out:
        if x['entity'] == "I-BRDCAN" or x['entity'] == "B-BRDCAN":
            res.append(x)
    return res

def extract_fever(text):
    expression = r"(([0-9]{2}[,|\.|]{0,1}[0-9]{0,})(°|°[cf]|) (temperature|temp|fever))"
    res = re.findall(expression, text, re.M)
    return res


textUsed = text3

symptoms = extract_symptoms(textUsed)
cancerType = extract_cancer_type(textUsed)
fever = extract_fever(textUsed)

print("Cancer Type:\n")
print(cancerType)
print()
print(f"Symptoms:({len(symptoms)})\n")
print(symptoms)
print()
print(f"Fever:\n")
print(fever)
