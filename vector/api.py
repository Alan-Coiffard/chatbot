from owlready2 import *

class Patient:
        def __init__(self, patient_name):
            self.onto = get_ontology("D:/Universiteit Umea/HT23/Interactivity in smart environments/chatbot/OncologyAid.rdf").load()

            self.patient_name = patient_name
            self.str_name = str(self.patient_name)
            self.onto.Patient(self.str_name)

        def create_patient(self):
            # str_name = str(self.patient_name)
            # self.onto.Patient(str_name)

            # initialize fact instances
            self.blood_stool_instance            = self.onto.BloodInStool(("BloodStoolRatingOfPatient" + str(self.patient_name)))
            self.blood_urine_instance            = self.onto.BloodInUrine("BloodUrineRatingOfPatient" + str(self.patient_name))
            self.nosebleed_instance              = self.onto.NoseBleeding("NoseBlOfPatient" + str(self.patient_name))
            self.bowel_movements_instance        = self.onto.BowelMovements("BowelMsOfPatient" + str(self.patient_name))
            self.difficulty_breathing_instance   = self.onto.DifficultyBreathing("DifficultyBreathingOfPatient" + str(self.patient_name))
            # dizzines_fact_instance          = onto.DizzinesFact("DizzinessOfPatient" + str(patient_name))
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
            # onto.Patient(str_name).hasFact.append(dizzines_fact_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.fainting_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.ingestion_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.pain_fact_instance)
            self.onto.Patient(self.str_name).hasFact.append(self.skin_rash_fact_instance) 
            self.onto.Patient(self.str_name).hasFact.append(self.temp_instance)

            # initialize fact numbers to -1
            self.onto.BloodStoolRatingOfPatientJan.hasBloodInStoolRating = -1
            self.onto.BloodUrineRatingOfPatientJan.hasBloodInUrineRating = -1
            self.onto.NoseBlOfPatientJan.hasNoseBleedRating = -1
            self.onto.BowelMsOfPatientJan.hasBowelMovementCount = -1
            self.onto.DifficultyBreathingOfPatientJan.hasDifficultyBreathing = -1
            self.onto.FaintingOfPatientJan.hasFainted = -1
            self.onto.IngestionOfPatientJan.hasIngestionRating = -1
            self.onto.PainFactOfPatientJan.hasPainRating = -1
            self.onto.SkinRashOfPatientJan.hasSkinRashPain = -1
            self.onto.SkinRashOfPatientJan.hasSkinRashRating = -1
            self.onto.TempOfPatientJan.hasTemperatureValue = 45

            return self.onto.Patient(self.str_name)
    
        def sync_ontology(self):
            with self.onto:
                sync_reasoner_pellet(infer_data_property_values=True, infer_property_values=True)

        def check_symptoms(self):
            for patient in self.onto.Patient.instances():
                print(f"Patient: {patient.name}")
                print(f"Patient facts: {patient.hasFact=}")
                print(f"test temp rating jan = {self.onto.TempOfPatientJan.hasTemperatureValue=}")
                print(f"Patient symptoms: {patient.hasSymptom}")
                print("------------------------------------------------")
        
        def change_temp(self, temp):
            del(self.onto.TempOfPatientJan.hasTemperatureValue)
            self.onto.TempOfPatientJan.hasTemperatureValue = temp
        
        def missing_information(self):
            missing_info = []
            patient_instance = self.onto.Patient(self.str_name)
            symptoms = patient_instance.hasSymptom
            for i in symptoms:
                print(f"Symptom = {i}")
                if "Unknown" in str(i):
                    missing_info.append(i)
                    # print(f"symptom unknown? = {i}")
            print(f"{missing_info=}")
            # print(f"Missing information for Patient {self.str_name}: {symptoms}")

             




patient = Patient("Jan")   
patient.create_patient()
patient.sync_ontology()
patient.check_symptoms()
patient.missing_information()


