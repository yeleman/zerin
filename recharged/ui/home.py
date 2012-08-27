#!/usr/bin/env python
# -*- coding: utf-8 -*-
# maintainer: Fadiga

from PySide import QtGui

from common import F_Widget, F_PageTitle


class HomeViewWidget(F_Widget):
    """ Shows the home page  """

    def __init__(self, parent=0, *args, **kwargs):
        super(HomeViewWidget, self).__init__(parent=parent,
                                                        *args, **kwargs)
        self.parent = parent
        self.parentWidget().setWindowTitle(u"Bienvenue sur Zerin")
        self.title = F_PageTitle(u"MENU GENERAL")

        pixmap = QtGui.QPixmap("images/logo.jpg")
        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        vbox = QtGui.QHBoxLayout()
        formbox = QtGui.QHBoxLayout()
        formbox.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        editbox = QtGui.QGridLayout()
        vbox.addWidget(self.title)
        editbox.addWidget(label, 0, 0, 0, 0)

        vbox.addLayout(editbox)
        self.setLayout(vbox)