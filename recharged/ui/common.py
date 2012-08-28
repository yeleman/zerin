#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from PySide import QtGui, QtCore

MAIN_WIDGET_SIZE = 1300


class Z_Widget(QtGui.QWidget):

    def __init__(self, parent=0, *args, **kwargs):

        QtGui.QWidget.__init__(self, parent=parent, *args, **kwargs)

        self.setMaximumWidth(MAIN_WIDGET_SIZE)

    def refresh(self):
        pass

    def change_main_context(self, context_widget, *args, **kwargs):
        return self.parentWidget()\
                          .change_context(context_widget, *args, **kwargs)

    def open_dialog(self, dialog, modal=False, *args, **kwargs):
        return self.parentWidget().open_dialog(dialog, \
                                               modal=modal, *args, **kwargs)

class Z_PageTitle(QtGui.QLabel):
    """ """

    def __init__(self, *args, **kwargs):
        super(Z_PageTitle, self).__init__(*args, **kwargs)

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("color: bleu; font: 20 10pt"
                           " \"Tlwg Typist\" ; border:1px solid bleu;\
                           border-radius: 14px 14px 4px 4px;font-variant: small-caps;")


class TabPane(QtGui.QTabBar):

    def __init__(self, parent=None):
        super(TabPane, self).__init__(parent)

    def addBox(self, box):
        self.setLayout(box)


class Z_BoxTitle(QtGui.QLabel):
    """ """

    def __init__(self, *args, **kwargs):
        super(Z_BoxTitle, self).__init__(*args, **kwargs)

        self.setAlignment(QtCore.Qt.AlignCenter)


class Button(QtGui.QCommandLinkButton):

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setAutoDefault(True)
        self.setCursor(QtCore.Qt.PointingHandCursor)

        self.setFont(QtGui.QFont("Comic Sans MS", 13, QtGui.QFont.Bold, True))


class FormLabel(QtGui.QLabel):

    def __init__(self, text, parent=None):
        QtGui.QLabel.__init__(self, text, parent)
        font = QtGui.QFont()
        font.setBold(True)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignLeft)


class IntLineEdit(QtGui.QLineEdit):
    """Accepter que des nombre positive """

    def __init__(self, parent=None):
        QtGui.QLineEdit.__init__(self, parent)
        self.setValidator(QtGui.QIntValidator(0, 100000000, self))


class FormatDate(QtGui.QDateTimeEdit):

    def __init__(self, *args, **kwargs):
        super(FormatDate, self).__init__(*args, **kwargs)
        self.setDisplayFormat(u"dd/MM/yyyy")
        self.setCalendarPopup(True)
