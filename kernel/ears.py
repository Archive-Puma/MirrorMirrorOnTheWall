from threading import Thread
import speech_recognition as sr


class Ears(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.recognizer = sr.Recognizer()

    def run(self):
        with sr.Microphone() as micro:
            print("Di algo: ")
            input_audio = self.recognizer.listen(micro)

        try:
            input_text = self.recognizer.recognize_google(
                input_audio, language="es_ES")
            print("You said: {0}".format(input_text.encode('utf-8')))
        except sr.UnknownValueError:
            print("No he entendido lo que has dicho")
        except sr.RequestError:
            print("No hay conexion a Internet")


def debug():
    test = Ears()
    test.start()
    test.join()


if __name__ == '__main__':
    debug()
