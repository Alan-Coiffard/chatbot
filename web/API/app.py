from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from nearest import select_question
import json
import re
import time
from api import Patient
from transformers import pipeline

def extract_cancer_type(text):
    res=[]
    pipe = pipeline("token-classification", model="DrM/BERT_Cancer_type_extraction2")
    out = pipe(text)
    for x in out:
        if x['entity'] == "I-BRDCAN" or x['entity'] == "B-BRDCAN":
            res.append(x)
    return res

def extract_fever(text):
    print(text)
    expression = r"(([0-9]{2}[,|\.|]{0,1}[0-9]{0,})(°|°[cf]|) (temperature|temp|fever))"
    res = re.findall(expression, text, re.M)
    return res

def extract_symptoms(text):
    res=[]
    pipe = pipeline("token-classification", model="silpakanneganti/bert-medical-ner")
    out = pipe(text)
    for x in out:
        if x['entity'] == "B-Sign_symptom" and "#" not in x['word']:
            res.append(x)
    return res

def extract_info(name: str, type: str):
    with open('information.json') as file:
        # Load JSON data
        data = json.load(file)
    print(data['cancer']['breast'])
    info = data[name][type]
    return info


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

patient = Patient("Jan")

@app.route('/api/new', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def create_patient():
    time.sleep(2)
    patient = Patient("Jan")   
    patient.create_patient()
    chatBotName = 'OncologyAid'
    data = {
        'Connection': 'Connected',
        'messages': [
            {
                "message": 'Welcome to ' + chatBotName + ' !',
                "direction": 'left'
            },
            {
                "message": 'What can I do for you ?',
                "direction": 'left'
            }
        ]
    }
    return jsonify(data)


@app.route('/api/data', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_data():
    information = ""
    listSymptoms = ""
    questionToAsk = ""
    msg = request.args.get('text')
    res = select_question(msg)
    cancerType = extract_cancer_type(msg)

    if res == "I would like to know more about cancer":
        if cancerType != []:
            information = extract_info("cancer", cancerType[0]['word'])
            res = "Here what I found about " + cancerType[0]['word'] + " cancer :"
    if res == "What should I do ?":
        symptoms = extract_symptoms(msg)
        fever = extract_fever(msg)
        datas = patient.missing_information(cancerType, symptoms, fever)
        questionToAsk = datas['questionToAsk']
        information = datas['information']
    
    fever = extract_fever(msg)
    if fever:
        print(fever)
        for i in fever:
            temp = i[1]
            print(f"fever = {i}")
            print("temp value=", i[1])
            patient.change_temp(float(temp))        
    
    res = patient.sync_ontology()
    
    data = {
        'message': res,
        'info': information,
        'questionToAsk': questionToAsk,
        'listSymptoms': listSymptoms,
        'direction': 'left'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
