# Détection des clignements d'œil

Ce projet utilise la bibliothèque OpenCV et le module cvzone pour détecter les clignements d'œil à partir de la vidéo capturée par la caméra de l'ordinateur.

## Installation des dépendances

Avant d'exécuter le code, assurez-vous d'installer les dépendances suivantes :

- **OpenCV** (version 3.4.2 ou supérieure)
- **cvzone** (disponible sur PyPI)

Vous pouvez installer les dépendances en utilisant la commande suivante :

```pip install opencv-python-headless cvzone```

ou bien sur Linux ; 

```sudo apt-get install python3-opencv```

aussi il faut :

```pip install mediapipe```

## Utilisation

Assurez-vous d'avoir une caméra connectée à votre ordinateur.

Exécutez le script Python en utilisant la commande suivante :

```python main.py```

Le script commencera à capturer la vidéo de votre caméra et détectera les clignements d'œil en temps réel. Le nombre de clignements détectés sera affiché à l'écran.




