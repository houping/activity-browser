# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from eight import *

from ...signals import signals
from .line_edit import SignalledLineEdit, SignalledPlainTextEdit
from PyQt4 import QtCore, QtGui


class ActivityDataGrid(QtGui.QWidget):
    def __init__(self, parent=None, activity=None):
        super(ActivityDataGrid, self).__init__(parent)
        self.activity = activity

        self.grid = self.get_grid()
        self.setLayout(self.grid)

        if activity:
            self.populate()

    def get_grid(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(QtGui.QLabel('Database'), 1, 1)
        self.database = QtGui.QLabel('')
        grid.addWidget(self.database, 1, 2, 1, 3)

        grid.addWidget(QtGui.QLabel('Name'), 2, 1)
        self.name_box = SignalledLineEdit(
            key=getattr(self.activity, "key", None),
            field="name",
            parent=self,
        )
        self.name_box.setPlaceholderText("Activity name")
        grid.addWidget(self.name_box, 2, 2, 1, 3)

        grid.addWidget(QtGui.QLabel('Comment'), 3, 1, 2, 1)
        self.comment_box = SignalledPlainTextEdit(
            key=getattr(self.activity, "key", None),
            field="comment",
            parent=self,
        )
        grid.addWidget(self.comment_box, 3, 2, 2, 3)

        grid.addWidget(QtGui.QLabel('Location'), 4, 1)
        self.location_box = SignalledLineEdit(
            key=getattr(self.activity, "key", None),
            field="location",
            parent=self,
        )
        self.location_box.setPlaceholderText("ISO 2-letter code or custom name")
        grid.addWidget(self.location_box, 4, 2, 1, 3)

        grid.addWidget(QtGui.QLabel('Unit'), 5, 1)
        self.unit_box = SignalledLineEdit(
            key=getattr(self.activity, "key", None),
            field="unit",
            parent=self,
        )
        grid.addWidget(self.unit_box, 5, 2, 1, 3)

        grid.setAlignment(QtCore.Qt.AlignTop)

        return grid

    def populate(self, activity=None):
        if activity:
            self.activity = activity
        self.database.setText(self.activity['database'])
        self.name_box.setText(self.activity['name'])
        self.name_box._key = self.activity.key
        self.comment_box.setPlainText(self.activity.get('comment', ''))
        self.comment_box._before = self.activity.get('comment', '')
        self.comment_box._key = self.activity.key
        self.location_box.setText(self.activity.get('location', ''))
        self.location_box._key = self.activity.key
        self.unit_box.setText(self.activity.get('unit', ''))
        self.unit_box._key = self.activity.key