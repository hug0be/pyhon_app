# ![Alt text](resources/images/favicon_32x32.png?raw=true "Title") WinQuest
Projet débuté dans un module Polytech, se concentrant sur la création d'application et la gestion de projet. 

# Introduction
WinQuest est une application permettant de créer et de jouer à des quizz.
WinQuest est réalisé par quatre développeurs de renom : Hugo BEAUBRUN, Mathieu FERREIRA, Ronan**g** TERRAS et Théo PLEBANI.
Développé en Python, elle utilise les modules de PySide6

# Installation
[WIP 🛠️]
Les identifiants par défaut sont `admin` et `foobar2` pour un compte admin, `user` et `foobar2` pour un compte utilisateur 

# Tutoriel
## Importer un quizz
Commencez par créer un fichier `.txt` : 
- Pour donner un titre à votre quizz, saisissez `quizz: Le sens de l'existence`

- Pour ajouter une question : 
  - Saisissez `question: Qu'elle est la réponse à la vie, l'univers et le reste ?`
  - Saisissez les réponses, `reponse: J'en sais rien gros`
  - Saisissez **une** bonne réponse, `bonne_reponse: 42`
  - Vous pouvez saisir jusqu'à **4 réponses maximum** (bonne réponse incluse)
  
- Si vous avez saisi **plus d'une question**, vous pouvez :
  - Choisir leur ordre d'affichage : 
    - `ordre: normal` (par défaut)
    - `ordre: aléatoire`
  - Choisir le nombre de questions à afficher, par exemple : 
    - `nombre_questions: 2` (1 par défaut)

Pour importer ce quizz, cliquer sur le bouton : ![Alt text](resources/images_tuto/import_button.png?raw=true "Bouton import"), 
sélectionnez votre fichier, puis validez.

[WIP 🛠️]