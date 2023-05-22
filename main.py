import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

# Accéder à la caméra de l'ordinateur
cap = cv2.VideoCapture(0)
# Détecter le visage et tracer des points sur les yeux
detector = FaceMeshDetector(maxFaces=1)

# Liste d'ID pour les points à tracer sur les yeux
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []  # Stocke les ratios de longueur de pupille à distance horizontale
blinkCounter = 0
counter = 0
color = (0, 0, 0)
isBlink = False  # Variable booléenne pour suivre les clignements d'œil

# Débute une boucle qui permet de continuer le traitement des images jusqu'à ce que l'utilisateur ferme la fenêtre
while True:

    # Réinitialise la vidéo une fois qu'elle est terminée
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Lit la vidéo, utilise le détecteur de points sur le visage pour trouver les points sur les yeux.
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    # Si visage d'iguane détecté, calcule la longueur de la pupille de l'œil et la distance horizontale entre les yeux
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5, color, cv2.FILLED)

        # Calcule la longueur de la pupille de l'œil et la distance horizontale entre les yeux
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        # Trace les lignes entre les points de l'œil (facultatif)
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        # Calcule le ratio de la longueur de la pupille de l'œil à la distance horizontale entre les yeux
        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)

        # Si le ratio est inférieur à 35, l'utilisateur cligne des yeux
        if ratioAvg < 35 and counter == 0:
            blinkCounter += 1
            color = (0, 0, 0)
            counter = 1
            isBlink = True
        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0
                color = (0, 0, 0)
                isBlink = False

        # Affiche le nombre de clignements sur l'écran
        if isBlink:
            text = "oui"
        else:
            text = "non"
        cvzone.putTextRect(img, f'Clignement: {blinkCounter}', (50, 100))
        cvzone.putTextRect(img, text, (50, 150))


    else:
        img = cv2.resize(img, (640, 360))

    # Affiche l'image
    cv2.imshow("Image", img)
    cv2.waitKey(25)