#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import sys

from PySide import QtGui

from database import setup
from ui.mainwindow import MainWindow


def main():
    """  """
    setup()

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
