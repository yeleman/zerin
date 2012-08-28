#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui, QtCore

from model import AddressBook
from data_helper import date_datetime
from common import (Z_Widget, Z_PageTitle, Z_BoxTitle, FormLabel, FormatDate,
                    Z_TableWidget, Button, IntLineEdit, date_datetime)


class AddressBookViewWidget(Z_Widget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(AddressBookViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.parent = parent
        self.parentWidget().setWindowTitle(u"Carnet d'adresse")

        self.all = "tous"
        vbox = QtGui.QVBoxLayout(self)
        hbox = QtGui.QHBoxLayout(self)
        editbox = QtGui.QGridLayout()
        formbox = QtGui.QGridLayout()

        self.table_order = BuyTableWidget(parent=self)
        self.table_resultat = ResultatTableWidget(parent=self)
        self.table_info = InfoTableWidget(parent=self)
        self.table_resultat.refresh_(self.all)
        completer = [self.all]
        for address in AddressBook.all():
            completer.append(address.name)
            completer.append(address.phone.name)
            completer.append(address.group.name)

        self.date = FormatDate(QtCore.QDate.currentDate())
        self.name_client = QtGui.QLineEdit()
        self.rech = QtGui.QLineEdit()
        self.rech.setMaximumSize(200, self.rech.maximumSize().height())
        self.rech.setCompleter(QtGui.QCompleter(completer))
        self.rech.textChanged.connect(self.finder)

        editbox.setColumnStretch(5, 2)

        self.vline = QtGui.QFrame()
        self.vline.setFrameShape(QtGui.QFrame.VLine)
        self.vline.setFrameShadow(QtGui.QFrame.Sunken)

        editbox.addWidget(FormLabel(u"Rechercher un produit:"), 0, 0)
        editbox.addWidget(self.rech, 1, 0)
        editbox.addWidget(self.vline, 0, 1, 2, 3)
        editbox.addWidget(FormLabel(u"Date d'achat:"), 0, 3)
        editbox.addWidget(self.date, 0, 4)

        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        splitter_left = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_down = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_left.addWidget(Z_BoxTitle(u"Resultats de la recherche"))
        splitter_left.addWidget(self.table_resultat)
        splitter_down.resize(15, 20)
        splitter_down.addWidget(self.table_info)
        splitter_rigth = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter_rigth.addWidget(Z_BoxTitle(u"Les adresses"))
        splitter_rigth.addWidget(self.table_order)
        splitter_rigth.resize(500, 900)

        splitter_left.addWidget(splitter_down)
        splitter.addWidget(splitter_left)
        splitter.addWidget(splitter_rigth)

        hbox.addWidget(splitter)
        vbox.addLayout(formbox)
        vbox.addLayout(editbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def finder(self):
        value = unicode(self.rech.text())
        self.table_resultat.refresh_(value)

    def save_b(self):
        ''' add operation '''
        pass


class ResultatTableWidget(Z_TableWidget):
    """docstring for ResultatTableWidget"""
    def __init__(self, parent, *args, **kwargs):
        Z_TableWidget.__init__(self, parent=parent, *args, **kwargs)

        self.hheaders = ["info", u"Resultat", u"Ajouter"]

        self.stretch_columns = []
        self.align_map = {2: 'l'}
        self.max_rows = 1
        self.display_vheaders = False
        self.display_fixed = True
        self.refresh()

    def refresh_(self, value):
        """ """
        self._reset()
        self.set_data_for(value)
        self.refresh()

    def set_data_for(self, value):

        address = []
        prod_rech = value.capitalize()
        if prod_rech == self.all:
            address = AddressBook.all()
        try:
            produit = AddressBook.filter(article=prod_rech).get()
            address.append(produit)
        except AddressBook.DoesNotExist:
            pass
        try:
            self.data = [("", prod.article, "") for prod in address]
        except AttributeError:
            pass

    def _item_for_data(self, row, column, data, context=None):
        if column == 2:
            return QtGui.QTableWidgetItem(QtGui.QIcon("images/go-next.png"),
                                                      "Ajouter")
        if column == 0:
            return QtGui.QTableWidgetItem(QtGui.QIcon("images/info.png"), "")
        return super(ResultatTableWidget, self)._item_for_data(row, column,
                                                               data, context)

    def click_item(self, row, column, *args):
        self.choix = AddressBook.filter(article=self.data[row][1]).get()
        if column != 2:
            self.parent.table_info.refresh_(self.choix.id)
        if column == 2:
            # self.removeRow(row)
            self.parent.table_order.refresh_(self.choix)


class InfoTableWidget(Z_Widget):

    def __init__(self, parent=0, *args, **kwargs):
        super(InfoTableWidget, self).__init__(parent=parent,\
                                                        *args, **kwargs)
        self.parent = parent
        self.refresh()
        self.articlelabel = QtGui.QLabel("")
        self.article = QtGui.QLabel(" ")
        self.stock_restant = QtGui.QLabel(" ")
        self.imagelabel = QtGui.QLabel("")

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        gridbox = QtGui.QGridLayout()
        self.image = Button("")
        self.image.clicked.connect(self.chow_image)
        gridbox.addWidget(self.articlelabel, 1, 0)
        gridbox.addWidget(self.article, 1, 1)
        gridbox.addWidget(self.stock_restant, 4, 0, 1, 2)
        gridbox.addWidget(self.imagelabel, 5, 0, 1, 5)
        hbox.addWidget(self.image)
        # gridbox.setColumnStretch(3, 3)
        vbox.addLayout(gridbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def refresh_(self, idd):

        self.prod = AddressBook.get(id=idd)

        self.articlelabel.setText((u"<b>Article:<b>"))
        self.article.setText(self.prod.article)

        self.article.setStyleSheet("solid #B1B1B4;"
                                         "font-size:20px;")

        self.imagelabel.setText(u"<b>Pas d'image</b>")
        self.image.setStyleSheet("")
        if self.prod.image:
            self.imagelabel.setText(u"<b>Image</b>")
            self.image.setStyleSheet("background: url(%s)"
                                     " no-repeat scroll 20px 110px #CCCCCC;"
                                     "width: 55px"
                                     % self.prod.image)

    def chow_image(self):
        """ doit afficher l'image complete dans une autre fenetre"""
        from show_image import ShowImageViewWidget
        try:
            self.parent.open_dialog(ShowImageViewWidget, modal=True,
                                                            prod=self.prod)
        except:
            pass


class BuyTableWidget(Z_TableWidget):

    def __init__(self, parent, *args, **kwargs):
        Z_TableWidget.__init__(self, parent=parent, *args, **kwargs)
        self.hheaders = [u"Quantité du produit", u"Désignation"]

        self.setSelectionMode(QtGui.QAbstractItemView.NoSelection)

        self.stretch_columns = [0,1]
        self.align_map = {1: 'l', 0: 'r'}
        self.max_rows = 100
        self.display_vheaders = False
        self.display_fixed = True
        self.refresh()
        self.isvalid = False

    def extend_rows(self):
        nb_rows = self.rowCount()

        self.setRowCount(nb_rows + 1)
        self.setSpan(nb_rows, 0, 1, 1)
        bicon = QtGui.QIcon.fromTheme('',
                                       QtGui.QIcon('images/save.png'))
        self.button = QtGui.QPushButton(bicon, u"Enrgistré")
        self.button.released.connect(self.parent.save_b)
        self.setCellWidget(nb_rows, 1, self.button)

        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 500)

    def _item_for_data(self, row, column, data, context=None):
        if column != 1 and column != 3:
            self.line_edit = IntLineEdit()
            self.line_edit.textChanged.connect(self.changed_value)
            return self.line_edit
        return super(BuyTableWidget, self)._item_for_data(row,
                                                            column, data,
                                                            context)

    def is_int(self, value):
        try:
            return int(value)
        except:
            return 0

    def get_table_items(self):
        """  """
        list_order = []
        for i in range(self.rowCount() - 1):
            liste_item = []
            try:
                liste_item.append(str(self.cellWidget(i, 0).text()))
                liste_item.append(str(self.item(i, 1).text()))
                list_order.append(liste_item)
            except:
                liste_item.append("")

        return list_order

    def changed_value(self, refresh=False):
        """ Calcule les Resultat """
        for row_num in xrange(0, self.data.__len__()):

            qtsaisi = self.is_int(self.cellWidget(row_num, 0).text())

            self.isvalid = True
            viderreur_qtsaisi = ""
            stylerreur = "background-color: rgb(255, 235, 235);border: 3px double SeaGreen"
            if qtsaisi == 0:
                viderreur_qtsaisi = stylerreur
                self.cellWidget(row_num, 0).setToolTip(u"La quantité est obligatoire")
                self.isvalid = False

            self.cellWidget(row_num, 0).setStyleSheet(viderreur_qtsaisi)

            self.cellWidget(row_num, 0).setToolTip("")


    def refresh_(self, choix=None):

        self.line = [0, u"%s" % choix.article]

        self.ex_data = self.get_table_items()
        if not self.line in self.data:
            self._reset()
            self.set_data_for()
            self.refresh()

    def set_data_for(self):

        self.data.extend([self.line])
