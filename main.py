# -*- coding: utf-8 -*-
from kernel.eyes import Eyes
from kernel.ears import Ears
from kernel.mouth import Mouth


def main():
    ojos = Eyes()
    oidos = Ears()
    boca = Mouth("Buenos dias")

    ojos.start()
    oidos.start()
    boca.start()

    ojos.join()
    oidos.join()
    boca.join()


if __name__ == '__main__':
    main()
