#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Importation des librairies 
import pandas as pd
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
import speech_recognition as sr
import openai
import seaborn as sns
# Configurer Azure Speech-to-Text
SPEECH_KEY = "maclé"
SERVICE_REGION = "francecentral"
speech_config = SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)


# In[9]:


# ✅ Configuration OpenAI pour Azure
openai.api_type = "azure"
openai.api_key = "maclé"
openai.api_base = "lien"
openai.api_version = "2024-05-01-preview"

# ✅ Chargement du dataset
df = pd.read_csv(r"C:\Users\Chris\speech_text_plot\dataset\StudentsPerformance.csv")

# 🔹 Fonction de reconnaissance vocale
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Parlez maintenant (nous écoutons)...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            print("❌ Aucun son détecté.")
            return ""

    try:
        print("🧠 Analyse en cours...")
        text = recognizer.recognize_google(audio, language="fr-FR")
        print(f"✅ Texte capturé : {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Impossible de reconnaître la parole.")
        return ""
    except sr.RequestError:
        print("⚠️ Erreur de connexion à Google Speech-to-Text.")
        return ""

# 🔹 Fonction pour entrer une demande en texte
def text_to_plot():
    return input("✍️ Entrez votre demande en langage naturel : ")

# 🔹 Construction du prompt
def construire_prompt_analyse(user_prompt):
    return f"""
    Tu travailles avec un dataset possédant les colonnes suivantes :
    - gender : Genre de l'étudiant (object).
    - math score : Score en mathématiques (int).
    - reading score : Score en lecture (int).
    - writing score : Score en écriture (int).

    Génère un code Python qui affiche un graphique pertinent basé sur les statistiques du dataset df pour répondre à cette demande utilisateur : '{user_prompt}'.
    Donne ensuite une **seule interprétation concise mais claire et explicite** des résultats.
    """

# 🔹 Appel à OpenAI
def consulter_openai_adapte(user_prompt):
    print("🔄 Génération du prompt pour OpenAI...")
    prompt = construire_prompt_analyse(user_prompt)

    try:
        response = openai.ChatCompletion.create(
            engine="gpt-4o",
            messages=[
                {"role": "system", "content": "Tu es un expert en analyse de données."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )

        response_text = response["choices"][0]["message"]["content"].strip()

        # Extraction du code Python
        code_part = ""
        if "```python" in response_text:
            code_part = response_text.split("```python")[1].split("```")[0].strip()

        # Suppression de la répétition
        interpretation_part = response_text.replace(f"```python\n{code_part}\n```", "").strip()

        return code_part, interpretation_part
    except Exception as e:
        print(f"❌ Erreur lors de l'appel à OpenAI : {e}")
        return "", ""

# 🔹 Exécution du code généré
def executer_plot_code(code_generated, interpretation):
    if not code_generated:
        print("⚠️ Aucun code généré.")
        return

    afficher_code = input("\n🔍 Voulez-vous afficher le code Python généré ? (oui/non) : ").strip().lower()
    
    if afficher_code == "oui":
        print("\n💻 Code Python généré :\n")
        print(code_generated)
    
    try:
        print("\n🛠️ Exécution du code généré...")
        exec(code_generated, globals())  # ⚠️ Risqué si non contrôlé
        print("\n✅ Code exécuté avec succès.")
        print("\n📊 Explication basée sur les statistiques :")
        print(interpretation)
    except Exception as e:
        print(f"❌ Erreur d'exécution : {e}")

# 🔹 Programme principal
print("📂 Chargement des données...\n✅ Dataset chargé avec succès.")
mode = input("🗣️ Entrez votre demande par (1) voix ou (2) texte ? (1/2) : ").strip()

if mode == "1":
    user_request = speech_to_text()
elif mode == "2":
    user_request = text_to_plot()
else:
    print("⚠️ Choix invalide.")
    exit()

if user_request:
    print(f"📌 Demande reçue : {user_request}")
    code_python, interpretation = consulter_openai_adapte(user_request)
    executer_plot_code(code_python, interpretation)
else:
    print("⚠️ Aucune demande valide saisie.")


# In[ ]:




