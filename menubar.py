#!/usr/bin/env python
# encoding=utf-8
# maintainer: fad

from PySide import QtGui, QtCore


class MenuBarTransfer(QtGui.QMenuBar):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent=parent, *args, **kwargs)

        self.parent = parent

        # File
        #   > Exit
        file_ = self.addMenu(u"&Fichier")

        # Exit
        menu_exit = QtGui.QAction(u"Quitter", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setToolTip("Quitter l'application")
        self.connect(menu_exit, QtCore.SIGNAL("triggered()"),
                     self.parentWidget(), QtCore.SLOT("close()"))
        file_.addAction(menu_exit)

        # Help
        #   > About
        menu_help = self.addMenu(u"Aide")
        menu_help.addAction(QtGui.QIcon(''), "Aide", self.goto_help)
        menu_help.addAction(QtGui.QIcon(''), u"À propos", self.goto_about)

    #Aide
    def goto_help(self):

        # self.open_dialog(HTMLEditor, modal=True)
        pass

    #About
    def goto_about(self):
        QtGui.QMessageBox.about(self, u"À propos",
                                u"<h2>PACH TECH </h2><br/>"
                                u"<i>Logiciel de gestion pour les vendeurs"
                                u" de nsɛrɛ et paani (ex. cyber café)</i><br/>"
                                u"<h2>© 2012 yɛlɛman s.à.r.l</h2>"
                                u"<ul>"
                                    u"<li>Hippodrome, Rue 240 Porte 1068,"
                                    u" BPE. 3713 - Bamako (Mali)</li>"
                                    u"<li><b>Tél. :</b> (223) 20 21 05 87</li>"
                                    u"<li><b>E-mail :</b>info@yeleman.com</li>"
                                    u"<li><b>Site :</b> www.yeleman.com<li>"
                                    u"<li><b>Développeurs :</b></li>"
                                         u"<ul><li>Renaud Gaudin</li>"
                                         u"<li>Ibrahima Fadiga</li>"
                                         u"<li>Alou Dolo</li> </ul>"
                                u"</ul>")
