import os
import cv2
import numpy as np
from PIL import Image

path = 'data/photos/all'
recognizer = cv2.createLBPHFaceRecognizer()


def getImageWithID(path):
    imagePaths = [os.path.join(path, pht) for pht in os.listdir(path)]
    faces = []
    IDs = []

    for img in imagePaths:
        emotionImg = Image.open(img).convert('L')
        emotionNP = np.array(emotionImg, 'uint8')
        emotion = os.path.split(img)[1].split('_')[0]
        ID = int(os.path.split(img)[1].split('_')[1].split('.')[0])

        if(emotion == "angry"):
            faces.append(emotionNP)
            IDs.append(ID)

        cv2.imshow("training", emotionNP)
        cv2.waitKey(10)
    return IDs, faces


Ids, faces = getImageWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('data/recognizer/trainingData.yml')
cv2.destroyAllWindows()
