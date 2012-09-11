#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import sys
import random

import desub
from PySide import QtGui

from database import setup
from mainwindow import MainWindow


def main():

    setup()
    http_port = random.randrange(3000, 4999)
    http = desub.join(['./http.py', str(http_port)])
    http.start()

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.base_url = u'http://127.0.0.1:%d' % http_port
    window.show()

    ret = app.exec_()
    http.stop()
    sys.exit(ret)

if __name__ == "__main__":
    main()
