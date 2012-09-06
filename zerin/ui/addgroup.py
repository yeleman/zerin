#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from PySide import QtGui

from models import Group
from common import ZWidget, ZBoxTitle


class GroupViewWidget(QtGui.QDialog, ZWidget):
    def __init__(self, table_group, parent, *args, **kwargs):
        QtGui.QDialog.__init__(self, parent, *args, **kwargs)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(ZBoxTitle(u"Ajout des groupes"))
        self.parent = table_group

        self.name = QtGui.QLineEdit()
        editbox = QtGui.QGridLayout()

        editbox.addWidget(QtGui.QLabel(u"Nom"), 0, 0)
        editbox.addWidget(self.name, 0, 1)
        bicon = QtGui.QIcon.fromTheme('document-save',
                                       QtGui.QIcon(''))
        butt = QtGui.QPushButton(bicon, u"Enregistrer")
        butt.clicked.connect(self.edit_prod)
        cancel_but = QtGui.QPushButton(u"Annuler")
        cancel_but.clicked.connect(self.cancel)
        editbox.addWidget(butt, 1, 1)
        editbox.addWidget(cancel_but, 1, 0)

        vbox.addLayout(editbox)
        self.setLayout(vbox)

    def cancel(self):
        self.close()

    def edit_prod(self):

        name = unicode(self.name.text())
        group = Group()
        try:
            group.name = name
            group.save()
            self.cancel()
            self.parent.table_group.refresh_()
        except:
            raise
