
# 🧮 Gestion de contexte avancée

## 📘 Description

Cette série de projets Python illustre l’utilisation des context managers pour gérer efficacement les ressources :

- Création et suppression automatique de fichiers temporaires

- Gestion de connexions avec journalisation et traitement des erreurs

- Traitement par lot de fichiers CSV avec traçabilité et logs

- Utilisation de ExitStack pour combiner plusieurs contextes

## 📂 Project Structure
````
projets/
├── Exercice1/
│   ├── a.txt
│   ├── b.txt
│   ├── c.txt
│   ├── partie1.py
│   ├── partie2.py
│   └── partie3.py
├── Exercice2/
│   ├── partie1.py
│   └── log.txt
├── Exercice3/
│   ├── exercice3.py
│   └── fichier.csv
│   └── main.py
└── README.md

````


## ⚙️ Features

### **1.** TempFileWriter – Fichiers temporaires
Classe TempFileWriter

- Attributs : filepath, f

Méthodes :

- __enter__() : crée et ouvre un fichier temporaire

- __exit__() : ferme et supprime le fichier automatiquement

temp_file() : context manager basé sur @contextmanager pour créer un fichier temporaire

ExitStack : ouverture simultanée de plusieurs fichiers (a.txt, b.txt, c.txt) et écriture

### **2.** ConnectionManager – Connexions et journalisation
Classe ConnectionManager

- Attributs : service_name

Méthodes :

- __enter__() : affiche la connexion établie avec horodatage

- __exit__() : affiche la déconnexion et journalise les erreurs éventuelles

Programme principal

- Utilisation de ExitStack pour gérer simultanément un fichier log et une connexion

- Journalisation des tâches effectuées sur un service

- Détection et affichage des erreurs (RuntimeError) avec horodatage

### **3.** BatchProcessor – Traitement CSV par lot
Classe BatchProcessor

- Attributs : csv_path, csv_file, csv_reader, log_path, log_file

Méthodes :

- __enter__() : ouvre le fichier CSV et le fichier log, écrit le début du batch

- line_processeur() : lit chaque ligne du CSV, traite et journalise les opérations, capture les erreurs

- __exit__() : journalise la fin du batch, ferme les fichiers et gère les exceptions

- Ouverture du batch avec with BatchProcessor()

- Traitement des lignes du CSV avec journalisation des opérations et erreurs

Programme principal

- Ouverture du batch avec with BatchProcessor()

- Traitement des lignes du CSV avec journalisation des opérations et erreurs
## 🖥️ Example Execution

### Exercice1 :

### Exercice2 : 

### Exercice3 :
## 💡 Concepts Practiced

- tiliser les context managers pour gérer automatiquement les ressources (fichiers, connexions)

- Exploiter ExitStack pour combiner plusieurs contextes dans un seul bloc with

- Assurer la traçabilité des opérations grâce aux logs et horodatages

- Gérer les erreurs de manière centralisée dans __exit__()

- Structurer le code pour un traitement par lot robuste et extensible
## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : python
- 🎓 Instructor	Mr.LACHGAR
- 📅 22	novembre 2025
