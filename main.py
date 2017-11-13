# -*- coding: utf-8 -*-
from kernel.eyes import Eyes
from kernel.ears import Ears


def main():
    ojos = Eyes()
    oidos = Ears()

    ojos.start()
    oidos.start()

    ojos.join()
    oidos.join()


if __name__ == '__main__':
    main()
