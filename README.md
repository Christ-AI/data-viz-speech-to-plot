# 🎙️ Data-Viz Speech-to-Plot  
**De la requête en langage naturel à la visualisation de données (CSV → Graph)**

## 📌 Présentation
**Data-Viz Speech-to-Plot** est un projet Python qui permet de **générer automatiquement des graphiques à partir de requêtes en langage naturel**, saisies en **texte** ou en **voix**.

L’utilisateur décrit le graphique souhaité (ex. *« comparer la moyenne des scores de maths par genre »*), et le système :
1. interprète la demande à l’aide d’un modèle de langage (LLM),
2. génère dynamiquement du code Python de visualisation,
3. exécute ce code sur un dataset CSV,
4. affiche le graphique ainsi qu’une **interprétation concise des résultats**.

Objectif : **réduire la barrière technique** entre utilisateurs non spécialistes et analyse de données.

---

## 🧠 Fonctionnalités
- Requêtes en langage naturel → graphiques automatiques
- Entrée **texte** (CLI) et **voix** (reconnaissance vocale)
- Génération dynamique de code Python (matplotlib / seaborn)
- Interprétation automatique du graphique généré
- Structure de projet propre et reproductible
- Aucune clé / chemin sensible codé en dur (via `.env`)

---

## 🏗️ Structure du projet
data-viz-speech-to-plot/
├─ src/
│ └─ main.py # Script principal
├─ data/
│ └─ StudentsPerformance.csv # Dataset d’exemple
├─ .env.example # Modèle de variables d’environnement
├─ requirements.txt
├─ README.md
└─ .gitignore


---

## 📊 Exemples de requêtes
- « Compare la moyenne des scores de mathématiques par genre. »
- « Affiche la distribution des scores de lecture. »
- « Montre la relation entre le score de maths et le score d’écriture. »

**Sorties :**
- Un graphique pertinent (bar chart, histogramme, scatter plot, etc.)
- Une interprétation courte et explicite des résultats

---
