import os
import cv2
from threading import Thread


class Eyes(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.camera = cv2.VideoCapture(0)

        cascade = os.path.join(
            "kernel", "eyes", "haarcascade_frontalface_default.xml")
        if not os.path.isfile(cascade):
            print("Missing file: {0}".format(cascade))
        self.classifier = cv2.CascadeClassifier(cascade)

    def run(self):
        while(True):
            __, frame = self.camera.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.classifier.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Ojos", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.stop()

    def stop(self):
        self.camera.release()
        cv2.destroyAllWindows()


def debug():
    test = Eyes()
    test.start()
    test.join()


if __name__ == '__main__':
    debug()
