#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import sys

from PySide import QtGui

from database import setup
from ui.mainwindow import MainWindow
from ui.window import Z_Window


def main():
    """  """
    setup()

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    setattr(Z_Window, 'window', window)
    window.show()
    # window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
