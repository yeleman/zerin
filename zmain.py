#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

def main():
    """  """
    app = QApplication(sys.argv)

    web = QWebView()
    web.load(QUrl("http://google.com"))
    web.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
