#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui, QtCore

from models import Contact, Transfer, ContactGroup, Group, PhoneNumber

from common import ZWidget, ZBoxTitle, ZTableWidget


class ContactViewWidget(ZWidget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(ContactViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.parent = parent
        self.parentWidget().setWindowTitle(u"Carnet d'adresse")

        self.group = "Tous"
        hbox = QtGui.QHBoxLayout(self)

        self.table_contact = ContactTableWidget(parent=self)
        self.table_resultat = ResultatTableWidget(parent=self)
        self.table_info = InfoTableWidget(parent=self)
        self.table_group = GroupTableWidget(parent=self)
        self.table_transf = TransfTableWidget(parent=self)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        splitter_left = QtGui.QSplitter(QtCore.Qt.Vertical)

        splitter_left.addWidget(ZBoxTitle(u"Les groupes"))
        splitter_left.addWidget(self.table_group)

        splitter_details = QtGui.QSplitter(QtCore.Qt.Horizontal)
        # splitter_details.resize(15, 20)
        # splitter_details.addWidget(ZBoxTitle(self.info_name))
        splitter_details.addWidget(self.table_info)

        splitter_down = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_down.addWidget(self.table_resultat)

        splitter_transf = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter_transf.addWidget(self.table_transf)

        splt_contact = QtGui.QSplitter(QtCore.Qt.Vertical)
        splt_contact.addWidget(ZBoxTitle(u"Les contactes"))
        splt_contact.addWidget(self.table_contact)
        splt_contact.resize(900, 1000)

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
        items = [["Groupes", [gr.name for gr in Group.all()]]]
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


class ContactTableWidget(ZTableWidget):
    """ Reçoit un groupe et affiche ses contactes et affiche tous les
        contactes par defaut"""

    def __init__(self, parent, *args, **kwargs):
        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.header = [u'', u"Nom"]

        self.group = parent.group

        self.set_data_for(self.group)
        self.refresh(True)

    def refresh_(self, group):
        self._reset()
        self.set_data_for(group)
        self.refresh(True)

    def set_data_for(self, group):

        if group == "Tous":
            self.data = [("", contact.name) for contact in Contact.all()]
        else:
            self.data = [("", contact_gp.contact.name) for contact_gp in
                                        ContactGroup.filter(group__name=group)]

    def _item_for_data(self, row, column, data, context=None):
        if column == 0:
            return QtGui.QTableWidgetItem(QtGui.QIcon("images/info.png"), "")
        return super(ContactTableWidget, self)._item_for_data(row, column,
                                                               data, context)

    def click_item(self, row, column, *args):

        number = PhoneNumber.filter(contact__name=self.data[row][1]).get()
        self.parent.table_info.refresh_(number)
        self.parent.table_transf.refresh_(number)


class InfoTableWidget(ZTableWidget):

    def __init__(self, parent=0, *args, **kwargs):
        super(InfoTableWidget, self).__init__(parent=parent, *args, **kwargs)
        self.parent = parent
        self.header = [u"Nom", u"Telephone"]

    def refresh_(self, number):
        self._reset()
        self.set_data_for(number)
        self.refresh(True)

    def set_data_for(self, number):
        self.data = [(tel.contact.name, tel.number) for tel in PhoneNumber.all()
                                            if number.contact==tel.contact]


class TransfTableWidget(ZTableWidget):
    """ Reçoit un numero de telephone et Affiche dans un tableau tout
       les transfers effectué par ce numero """

    def __init__(self, parent, *args, **kwargs):
        ZTableWidget.__init__(self, parent=parent, *args, **kwargs)

        self.header = [u"Numero", u"Date du transfert", u"Montant(FCFA)"]
        self.set_data_for("")
        self.refresh(True)

    def refresh_(self, number):
        self._reset()
        self.set_data_for(number)
        self.refresh(True)

    def set_data_for(self, number):

        try:
            self.data = [(transf.number, transf.date.strftime(u"%A le %d %b %Y a %Hh:%Mmn"), transf.amount)
                          for transf in Transfer.all()\
                           if transf.number.contact==number.contact]
        except AttributeError:
            pass
