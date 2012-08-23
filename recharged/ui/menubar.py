#!/usr/bin/env python
# encoding=utf-8
# maintainer: fad

from PyQt4 import QtGui, QtCore

from common import F_Widget


class MenuBar(QtGui.QMenuBar, F_Widget):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent=parent, *args, **kwargs)

        self.parent = parent
        #Menu File
        file_ = self.addMenu(u"&Fichier")

        # Exit
        exit_ = QtGui.QAction(u"Exit", self)
        exit_.setShortcut("Ctrl+Q")
        exit_.setToolTip("Quiter l'application")
        self.connect(exit_, QtCore.SIGNAL("triggered()"), self.parentWidget(),
                                          QtCore.SLOT("close()"))
        file_.addAction(exit_)

        #Menu Aide
        help_ = self.addMenu(u"Aide")
        help_.addAction(QtGui.QIcon('images/help.png', "Aide"),
                                    self.goto_help)
        help_.addAction(QtGui.QIcon('images/info.png', u"A poropos"),
                                    self.goto_about)

    #About
    def goto_about(self):
        from model import VERSION
        QtGui.QMessageBox.about(self, u"À propos",
                                u"<h1>ZERIN  %s </h1>"
                                u"<ul><b><li>Logiciel d'envoi de zerin</li>"
                                    u"<li>© 2012 yɛlɛman s.à.r.l</li>"
                                    u"<li><b>Hippodrome, Avenue Al Quds, BPE. 3713 - Bamako (Mali)</b></li>"
                                    u"<li><b>Tel:</b> (223) 76 33 30 05</li>"
                                    u"<li><b>Tel:</b> (223) </li>"
                                    u"<li><b>E-mail:</b>info@yeleman.com</li>"
                                    u"<ul><b>Developpeur:</b>"
                                         u"<li>Renaud Gaudin</li>"
                                         u"<li>Ibrahima Fadiga</li>"
                                         u"<li>Alou Dolo</li> </ul>"
                                    u"<b>Site:</b> www.yeleman.com<br/></ul>" % VERSION)
