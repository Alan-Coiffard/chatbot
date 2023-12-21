from owlready2 import *


# TODO: Fever checking, parse result of symptoms, IF FEVER IN SYMPTOM: ASK TEMP, IF "TEMPERATURE" FEVER, BUT NO NUMBER, 
# TODO: Formulate sentence back to user, check for comma/dot. Information request
# TODO: 
#




class Patient:
        def __init__(self, patient_name):
            """
            - Initialize patient with the given patient name. This name will be used in the rest of the code
            - missing info list is made for eventual reasoning which questions should be asked
            - self.situation is the assessment of the patient. This is checked when the ontology is synced. If 
            this is critical, it will print something to tell you. This can be changed if needed

            """
            self.onto = get_ontology("D:/Universiteit Umea/HT23/Interactivity in smart environments/chatbot/OncologyAid.rdf").load()
            self.missing_info = []
            self.patient_name = patient_name
            self.str_name = str(self.patient_name)
            self.onto.Patient(self.str_name)
            self.situation = None

        def create_patient(self):

            # initialize fact instances
            self.blood_stool_instance            = self.onto.BloodInStool(("BloodStoolRatingOfPatient" + str(self.patient_name)))
            self.blood_urine_instance            = self.onto.BloodInUrine("BloodUrineRatingOfPatient" + str(self.patient_name))
            self.nosebleed_instance              = self.onto.NoseBleeding("NoseBlOfPatient" + str(self.patient_name))
            self.bowel_movements_instance        = self.onto.BowelMovements("BowelMsOfPatient" + str(self.patient_name))
            self.difficulty_breathing_instance   = self.onto.DifficultyBreathing("DifficultyBreathingOfPatient" + str(self.patient_name))
            self.dizziness_fact_instance         = self.onto.DizzinessFact("DizzinessOfPatient" + str(self.patient_name))
            self.fainting_instance               = self.onto.Fainting("FaintingOfPatient" + str(self.patient_name))
            self.ingestion_instance              = self.onto.Ingestion("IngestionOfPatient" + str(self.patient_name))
            self.pain_fact_instance              = self.onto.PainFact("PainFactOfPatient" + str(self.patient_name))
            self.skin_rash_fact_instance         = self.onto.SkinRashFact("SkinRashOfPatient" + str(self.patient_name))
            self.temp_instance                   = self.onto.Temperature("TempOfPatient" + str(self.patient_name))
            
            # give new patient facts
            self.onto.Patient(self.str_name).hasFact.append(self.blood_stool_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.blood_urine_instance) 
            self.onto.Patient(self.str_name).hasFact.append( self.nosebleed_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.bowel_movements_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.difficulty_breathing_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.dizziness_fact_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.fainting_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.ingestion_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.pain_fact_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.skin_rash_fact_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.temp_instance)

            # initialize fact numbers to -1
            self.onto.BloodStoolRatingOfPatientJan.hasBloodInStoolRating = -1
            self.onto.BloodUrineRatingOfPatientJan.hasBloodInUrineRating = -1
            self.onto.NoseBlOfPatientJan.hasNoseBleedRating = -1
            self.onto.BowelMsOfPatientJan.hasBowelMovementCount = 7
            self.onto.DifficultyBreathingOfPatientJan.hasDifficultyBreathing = -1
            self.onto.DizzinessOfPatientJan.hasDizzinessRating = -1
            self.onto.FaintingOfPatientJan.hasFainted = -1
            self.onto.IngestionOfPatientJan.hasIngestionRating = -1
            self.onto.PainFactOfPatientJan.hasPainRating = 1
            self.onto.SkinRashOfPatientJan.hasSkinRashPain = -1
            self.onto.SkinRashOfPatientJan.hasSkinRashRating = -1
            self.onto.TempOfPatientJan.hasTemperatureValue = -1

            return self.onto.Patient(self.str_name)
    
        def sync_ontology(self):
            with self.onto:
                sync_reasoner_pellet(infer_data_property_values=True, infer_property_values=True)
            
            patient_instance = self.onto.Patient(self.str_name)
            self.situation = patient_instance.hasSituationAssessment
            print(f"situation = {self.situation}")
            if "SeekImmediateHelp" in str(self.situation):
                print("CALL YOUR DOCTOR NOW YA SILLY GOOSE")

        def check_symptoms(self):
            patient_instance = self.onto.Patient(self.str_name)
            print(patient_instance.hasSymptom)

        def change_bowel_movements(self, value):
          del(self.onto.BowelMsOfPatientJan.hasBowelMovementCount)
          self.onto.BowelMsOfPatientJan.hasBowelMovementCount = value

        def change_blood_in_stool(self, value):
          del(self.onto.BloodStoolRatingOfPatientJan.hasBloodInStoolRating)
          self.onto.BloodStoolRatingOfPatientJan.hasBloodInStoolRating = value

        def change_blood_in_urine(self, value):
          del(self.onto.BloodUrineRatingOfPatientJan.hasBloodInUrineRating)
          self.onto.BloodUrineRatingOfPatientJan.hasBloodInUrineRating = value

        def change_nosebleed(self, value):
          del(self.onto.NoseBlOfPatientJan.hasNoseBleedRating)
          self.onto.NoseBlOfPatientJan.hasNoseBleedRating = value

        def change_breathing(self, value):
          del(self.onto.DifficultyBreathingOfPatientJan.hasDifficultyBreathing)
          self.onto.DifficultyBreathingOfPatientJan.hasDifficultyBreathing = value

        def change_dizziness(self, value):
          del(self.onto.DizzinessOfPatientJan.hasDizzinessRating)
          self.onto.DizzinessOfPatientJan.hasDizzinessRating = value

        def change_fainted(self, value):
          del(self.onto.FaintingOfPatientJan.hasFainted)
          self.onto.FaintingOfPatientJan.hasFainted = value

        def change_ingestion(self, value):
          del(self.onto.IngestionOfPatientJan.hasIngestionRating)
          self.onto.IngestionOfPatientJan.hasIngestionRating = value
        
        def change_pain_rating(self, value):
          del(self.onto.PainFactOfPatientJan.hasPainRating)
          self.onto.PainFactOfPatientJan.hasPainRating = value

        def change_skin_rash_pain(self, value):
          del(self.onto.SkinRashOfPatientJan.hasSkinRashPain)
          self.onto.SkinRashOfPatientJan.hasSkinRashPain = value

        def change_skin_rash_rating(self, value):
          del(self.onto.SkinRashOfPatientJan.hasSkinRashRating)
          self.onto.SkinRashOfPatientJan.hasSkinRashRating = value

        def change_temp(self, temp):
            del(self.onto.TempOfPatientJan.hasTemperatureValue)
            self.onto.TempOfPatientJan.hasTemperatureValue = temp
        
        def missing_information(self):
            patient_instance = self.onto.Patient(self.str_name)
            self.situation = patient_instance.hasSituationAssessment
            symptoms = patient_instance.hasSymptom
            for i in symptoms:
                print(f"Symptom = {i}")
                if "Unknown" in str(i):
                    self.missing_info.append(i)
            print(f"{self.missing_info=}")

            # Sentence forming for unknown symptoms

            if len(self.missing_info) > 2:
                substring_to_remove = "OncologyAid.Unknown"

                symptom_1 = str(self.missing_info[0]).replace(substring_to_remove, '')
                symptom_2 = str(self.missing_info[1]).replace(substring_to_remove, '')
                print(symptom_1, symptom_2)
            if len(self.missing_info) == 1:
                substring_to_remove = "OncologyAid.Unknown"

                symptom_1 = str(self.missing_info[0]).replace(substring_to_remove, '')
                print(symptom_1)
            if len(self.missing_info) == 0:
                symptom_1 = ''


        # Check symptoms and fever
        
            symptoms = extract_symptoms(textUsed)
            cancerType = extract_cancer_type(textUsed)
            fever = extract_fever(textUsed)



            # Returning questions
            for i in symptoms:
                if i["word"] == "fever" or i["word"] == "temperature":
                    if not fever:
                        print("what is the temperature?")
                    else:
                        pass
                if i["word"] == "pain" or "hurt" in i["word"]  or "ache" in i["word"]:
                        self.change_pain_rating(5)
                        print("PAIN 1-10")
                if i["word"] == "throwing" or i["word"] == "queasy" or i["word"] == "vomiting" or i["word"] == "vomit":
                        self.change_ingestion(2)
                        print("Nausea")
                if i["word"] ==  "di":
                        print("diarrhea")
                        print("How many bowel movements have you had today?")
                        self.change_bowel_movements(7)
                if i["word"] == "rash":
                        print("How much? 0-2")
                        self.change_skin_rash_rating(1)
                if i["word"] == "faint":
                        print("faint")
                        self.change_fainted(2)
                if i["word"] == "dizzy" or i["word"] == "dizziness":
                        print("dizzy")
                        self.change_dizziness(2)


                for i in cancerType:
                    print(f"cancer type = {i}")

                for i in fever:
                    temp = i[1]
                    print(f"fever = {i}")
                    print("temp value=", i[1])

                    self.change_temp(temp)

             




patient = Patient("Jan")   
patient.create_patient()
patient.change_temp(37)
patient.sync_ontology()
patient.check_symptoms()
patient.missing_information()


"""

JAVA memory: msys64


TODO FOR TOMORROW:
MAKE SURE THE RIGHT STRINGS ARE IN THE CHAT
JAVA MEMORY
REWRITE API FILE TO THE RIGHT FORMAT


Steps for demo:
    1. Welcome message
    1a. initiate a patient
    2. user types set message: I have been feeling a little dizzy and I have a slight fever. Is this serious?
    3. infer dizziness and fever
    3a. ask for temperature
    4. user writes temperature
    5. critical assessment, is there anything else?


User
I have been feeling a little dizzy and I have a slight fever. Is this serious?
OncologyAid
Can you tell me how high your temperature is, exactly?
User
37.7 degrees celsius.
OncologyAid
This symptom combination does not seem critical. Have you also experienced symptoms such as pain or skin rash?
User
No, nothing else.
OncologyAid
Then I recommend that you rest and keep hydrated.
If you notice your fever reaching 38 degrees, please contact your care team for further assessment. To find out more about how to handle high fever, you can click here: https://www.1177.se/Vasterbotten/sjukdomar--besvar/infektioner/feber/feber/

Is there anything else I can help you with?
User
No, thanks.


"""


