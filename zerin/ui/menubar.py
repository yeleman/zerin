#!/usr/bin/env python
# encoding=utf-8
# maintainer: fad

from PySide import QtGui, QtCore

from common import ZWidget
from help import HTMLEditor


class MenuBarTransfer(QtGui.QMenuBar, ZWidget):

    def __init__(self, parent=None, *args, **kwargs):
        QtGui.QMenuBar.__init__(self, parent=parent, *args, **kwargs)

        self.parent = parent
        #Menu File
        file_ = self.addMenu(u"&Fichier")

        # Exit
        menu_exit = QtGui.QAction(u"Quitter", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setToolTip("Quitter l'application")
        self.connect(menu_exit, QtCore.SIGNAL("triggered()"), self.parentWidget(),
                                          QtCore.SLOT("close()"))
        file_.addAction(menu_exit)

        # Menu Aide
        menu_help = self.addMenu(u"Aide")
        menu_help.addAction(QtGui.QIcon('images/help.png'), "Aide",
                                    self.goto_help)
        menu_help.addAction(QtGui.QIcon('images/info.png'), u"À propos",
                                    self.goto_about)

        # Menu Options
        menu_settings = self.addMenu(u"Options")
        menu_settings.addAction(QtGui.QIcon('images/help.png'), u"Options",
                                    self.goto_settings)
        # Menu adressbook
        #   => add contact
        #   => search contact
        #   => delete contact
        menu_adressbook = self.addMenu(u"Carnet d'adresse")
        menu_adressbook.addAction(QtGui.QIcon('images/help.png'),
                                         u"Ajouter contact",
                                    self.goto_add_contact)
        menu_adressbook.addAction(QtGui.QIcon('images/help.png'),
                                         u"Chercher contact",
                                    self.goto_search_contact)
        menu_adressbook.addAction(QtGui.QIcon('images/help.png'),
                                        u"Supprimer contact",
                                    self.goto_delete_contact)


    #Add contact
    def goto_add_contact(self):
        QtGui.QMessageBox.about(self, u"Ajouter contact",
                                u"<h3>Pour ajouter un contact</h3>")
    #Search contact
    def goto_search_contact(self):
        QtGui.QMessageBox.about(self, u"Recherche contact",
                                u"<h3>Pour chercher un contact</h3>")
    #Delete contact
    def goto_delete_contact(self):
        QtGui.QMessageBox.about(self, u"Supprimer contact",
                                u"<h3>Pour supprimer un contact</h3>")

    #Settings
    def goto_settings(self):
        QtGui.QMessageBox.about(self, u"Options",
                                u"<h3>Settings</h3>")

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
