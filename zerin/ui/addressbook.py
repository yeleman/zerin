#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui, QtCore

from models import Contact

from common import ZWidget, ZBoxTitle, ZTableWidget, Button


class ContactViewWidget(ZWidget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(ContactViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.parent = parent
        self.parentWidget().setWindowTitle(u"Carnet d'adresse")

        self.group = "tous"
        hbox = QtGui.QHBoxLayout(self)

        self.table_contact = ContactTableWidget(parent=self)
        self.table_resultat = ResultatTableWidget(parent=self)
        self.table_info = InfoTableWidget(parent=self)
        self.table_group = GroupTableWidget(parent=self)
        self.table_transf = TransfTableWidget(parent=self)

        self.button_all = Button(u"Tous")
        # self.button_all.clicked.connect(self.)
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        splitter_left = QtGui.QSplitter(QtCore.Qt.Vertical)
        # splitter_left.addWidget(self.button_all)
        splitter_left.addWidget(ZBoxTitle(u"Les groups"))
        splitter_left.addWidget(self.table_group)

        splitter_details = QtGui.QSplitter(QtCore.Qt.Horizontal)
        # splitter_details.resize(15, 20)
        # splitter_details.addWidget(ZBoxTitle(u"details"))
        splitter_details.addWidget(self.table_info)

        splitter_down = QtGui.QSplitter(QtCore.Qt.Vertical)
        # splitter_down.resize(615, 110)
        # splitter_down.addWidget(ZBoxTitle(u"Les groupes"))
        splitter_down.addWidget(self.table_resultat)

        splitter_transf = QtGui.QSplitter(QtCore.Qt.Horizontal)
        # splitter_transf.addWidget(ZBoxTitle(u"Transfert"))
        # splitter_transf.resize(815, 420)
        splitter_transf.addWidget(self.table_transf)

        splt_contact = QtGui.QSplitter(QtCore.Qt.Vertical)
        splt_contact.addWidget(ZBoxTitle(u"Les contacts"))
        splt_contact.addWidget(self.table_contact)
        splt_contact.resize(1500, 1000)

        splitter_left.addWidget(splitter_down)
        splitter_details.addWidget(splitter_transf)
        splt_contact.addWidget(splitter_details)
        splitter.addWidget(splitter_left)
        splitter.addWidget(splt_contact)

        hbox.addWidget(splitter)
        self.setLayout(hbox)


class ResultatTableWidget(ZTableWidget):
    """docstring for ResultatTableWidget"""

    def __init__(self, parent, *args, **kwargs):
        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)

        self.header = ["info", u"Resultat", u"Ajouter"]


class InfoTableWidget(ZTableWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(InfoTableWidget, self).__init__(parent=parent,\
                                                        *args, **kwargs)
        self.parent = parent
        self.header = [u'', u"Nom", u"Telephone"]

    def refresh_(self, number):
        self._reset()
        self.set_data_for(number)
        self.refresh(True)

    def set_data_for(self, number):
        self.data = [('', number, "ejsfsv")]


class ContactTableWidget(ZTableWidget):
    """ Reçoit un groupe et affiche ses contactes et affiche tous les
        contactes par defaut"""

    def __init__(self, parent, *args, **kwargs):
        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [u'', u"Nom", u"Telephone"]
        self.group = parent.group

        self.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.set_data_for(self.group)
        self.refresh(True)

    def refresh_(self, group):
        self._reset()
        self.set_data_for(group)
        self.refresh(True)

    def set_data_for(self, group):
        self.data = [('', group, "ejsfsv")]

    def _item_for_data(self, row, column, data, context=None):
        if column == 0:
            return QtGui.QTableWidgetItem(QtGui.QIcon("images/info.png"), "")
        return super(ContactTableWidget, self)._item_for_data(row, column,
                                                               data, context)

    def click_item(self, row, column, *args):
        # self.choix = Contact.filter(phone__number=self.data[row][1]).get()
        if column == 0:
            self.parent.table_info.refresh_(self.data[row][1])
            self.parent.table_transf.refresh_(self.data[row][1])


class GroupTableWidget(QtGui.QTreeWidget):
    """affiche tout le nom de tous les groupes"""

    def __init__(self, parent, *args, **kwargs):
        super(GroupTableWidget, self).__init__(parent)
        self.parent = parent

        self.setHeaderHidden(True)
        self.setAlternatingRowColors(True)
        self.setMouseTracking(True)
        self.setAllColumnsShowFocus(False)
        self.setFocusPolicy(QtCore.Qt.TabFocus)
        self.setAnimated(True)
        self.itemClicked.connect(self.handleClicked)
        self.setTextElideMode(QtCore.Qt.ElideMiddle)
        # self.setRootIsDecorated(False)
        # self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        h = QtGui.QTreeWidgetItem(self)
        h.setText(0, "Tous")
        items = [["Groupes", [gr.name for gr in Contact.all()]]]
        for item in items:
            p = QtGui.QTreeWidgetItem(self)
            # p.setIcon(0, QtGui.QIcon('images/group.png'))
            p.setText(0, item[0])
            for i in item[1]:
                c = QtGui.QTreeWidgetItem(p)
                c.setIcon(0, QtGui.QIcon('images/group.png'))
                c.setText(0, i)

    def handleClicked(self, item, column):
        self.gr = item.data(column, 0)
        self.parent.table_contact.refresh_(self.gr)


class TransfTableWidget(ZTableWidget):
    """docstring for ResultatTableWidget"""


    def __init__(self, parent, *args, **kwargs):
        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)

        self.header = ["Date", u"Numero", u"Montant"]

        self.group = parent.group
        self.set_data_for(self.group)
        self.refresh(True)

    def refresh_(self, group):
        self._reset()
        self.set_data_for(group)
        self.refresh(True)

    def set_data_for(self, number):
        self.data = [('', number, 300)]