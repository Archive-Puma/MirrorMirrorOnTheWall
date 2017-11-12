# -*- coding: utf-8 -*-
from kernel.eyes import Eyes


def main():
    ojos = Eyes()
    ojos.start()
    ojos.join()


if __name__ == '__main__':
    main()
