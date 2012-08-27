#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from PySide import QtGui, QtCore

MAIN_WIDGET_SIZE = 1300


class F_Widget(QtGui.QWidget):

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

class F_PageTitle(QtGui.QLabel):
    """ """

    def __init__(self, *args, **kwargs):
        super(F_PageTitle, self).__init__(*args, **kwargs)

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("color: bleu; font: 20 10pt"
                           " \"Tlwg Typist\" ; border:1px solid bleu;\
                           border-radius: 14px 14px 4px 4px;font-variant: small-caps;")
