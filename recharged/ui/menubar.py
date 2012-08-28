#!/usr/bin/env python
# encoding=utf-8
# maintainer: fad

from PySide import QtGui, QtCore

from common import Z_Widget
from help import HTMLEditor

class MenuBar(QtGui.QMenuBar, Z_Widget):

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
        help_.addAction(QtGui.QIcon('images/help.png'), "Aide",
                                    self.goto_help)
        help_.addAction(QtGui.QIcon('images/info.png'), u"À propos",
                                    self.goto_about)

    #Aide
    def goto_help(self):

        self.open_dialog(HTMLEditor, modal=True)
    #About
    def goto_about(self):
        QtGui.QMessageBox.about(self, u"À propos",
                                u"<h2>PACH TECH </h2><br/>"
                                u"<i>Logiciel de gestion pour les vendeurs de nsɛrɛ et paani (ex. cyber café)</i><br/>"
                                u"<h2>© 2012 yɛlɛman s.à.r.l</h2>"
                                u"<ul>"
                                    u"<li>Hippodrome, Rue 240 Porte 1068, BPE. 3713 - Bamako (Mali)</li>"
                                    u"<li><b>Tél. :</b> (223) 20 21 05 87</li>"
                                    u"<li><b>E-mail :</b>info@yeleman.com</li>"
                                    u"<li><b>Site :</b> www.yeleman.com<li>"
                                    u"<li><b>Développeurs :</b></li>"
                                         u"<ul><li>Renaud Gaudin</li>"
                                         u"<li>Ibrahima Fadiga</li>"
                                         u"<li>Alou Dolo</li> </ul>"
                                u"</ul>")
