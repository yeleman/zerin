#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fad

from PyQt4 import QtGui

from home import HomeViewWidget
from menubar import MenuBar


class MainWindow(QtGui.QMainWindow):
    """  """
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(1200, 600)
        self.setWindowTitle(u"GE.DOUG")
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.change_context(HomeViewWidget)

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)

    def change_context(self, context_widget, *args, **kwargs):

        # instanciate context
        self.view_widget = context_widget(parent=self, *args, **kwargs)

        # attach context to window
        self.setCentralWidget(self.view_widget)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        d = dialog(parent=self, *args, **kwargs)
        d.setModal(modal)
        d.setWindowOpacity(0.90)
        d.exec_()
