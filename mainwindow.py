#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Maintainer: Fad

from PySide import QtCore
from PySide import QtGui
from PySide import QtWebKit

from menubar import MenuBarTransfer


class ZWebView(QtWebKit.QWebView):

    def __init__(self, parent):
        super(ZWebView, self).__init__(parent)


class MainWindow(QtGui.QMainWindow):
    """  """
    def __init__(self):
        self.resize_subscribers = []
        self.base_url = u'http://127.0.0.1:5000'

        QtGui.QMainWindow.__init__(self)

        # self.resize(1200, 600)
        self.setWindowTitle(u"Zerin")
        # self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.change_context(ZWebView)

        self.menubar = MenuBarTransfer(self)
        self.setMenuBar(self.menubar)
        self.startTimer(3000) # 3s

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

    def resizeEvent(self, event):
        for sub in self.resize_subscribers:
            sub.windowdResized(event)

    def subscribe_resize(self, widget):
        self.resize_subscribers.append(widget)

    def timerEvent(self, event):
        self.view_widget.load(QtCore.QUrl(self.base_url))
        self.killTimer(event.timerId())