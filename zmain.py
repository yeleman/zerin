#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import sys

import desub
from PySide import QtGui

from database import setup
from mainwindow import MainWindow


def main():

    setup()
    http = desub.join(['/home/fad/src/envs/zerin/bin/python', './http.py'])
    http.start()

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    ret = app.exec_()
    print('before stop')
    print(http.is_running())
    print(http.pid)
    http.stop()
    print('after stop')
    print(http.is_running())
    print(http.pid)
    sys.exit(ret)

if __name__ == "__main__":
    main()
