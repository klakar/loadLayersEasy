# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_loadlayerseasy.ui'
#
# Created: Sun Apr 27 23:01:12 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_loadLayersEasy(object):
    def setupUi(self, loadLayersEasy):
        loadLayersEasy.setObjectName(_fromUtf8("loadLayersEasy"))
        loadLayersEasy.resize(374, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loadLayersEasy.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(loadLayersEasy)
        self.buttonBox.setGeometry(QtCore.QRect(20, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.listWidget = QtGui.QListWidget(loadLayersEasy)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 351, 181))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(loadLayersEasy)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.findList = QtGui.QPushButton(loadLayersEasy)
        self.findList.setGeometry(QtCore.QRect(330, 230, 31, 21))
        self.findList.setObjectName(_fromUtf8("findList"))
        self.listfil = QtGui.QLabel(loadLayersEasy)
        self.listfil.setGeometry(QtCore.QRect(10, 230, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listfil.setFont(font)
        self.listfil.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.listfil.setObjectName(_fromUtf8("listfil"))
        self.label_2 = QtGui.QLabel(loadLayersEasy)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(loadLayersEasy)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), loadLayersEasy.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), loadLayersEasy.reject)
        QtCore.QMetaObject.connectSlotsByName(loadLayersEasy)

    def retranslateUi(self, loadLayersEasy):
        loadLayersEasy.setWindowTitle(QtGui.QApplication.translate("loadLayersEasy", "Ladda Lager - Load Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(False)
        self.label.setText(QtGui.QApplication.translate("loadLayersEasy", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Lägg till lager i QGIS</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.findList.setToolTip(QtGui.QApplication.translate("loadLayersEasy", "Öppna en listfil", None, QtGui.QApplication.UnicodeUTF8))
        self.findList.setText(QtGui.QApplication.translate("loadLayersEasy", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.listfil.setText(QtGui.QApplication.translate("loadLayersEasy", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("loadLayersEasy", "<html><head/><body><p><span style=\" font-size:10pt; color:#959595;\">Add Layer to QGIS</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

