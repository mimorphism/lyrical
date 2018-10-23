# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lyrical.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 674)
        self.gBoxLyrical = QtWidgets.QGroupBox(Dialog)
        self.gBoxLyrical.setGeometry(QtCore.QRect(19, 69, 591, 591))
        self.gBoxLyrical.setTitle("")
        self.gBoxLyrical.setObjectName("gBoxLyrical")
        self.textBoxLyrics = QtWidgets.QPlainTextEdit(self.gBoxLyrical)
        self.textBoxLyrics.setGeometry(QtCore.QRect(20, 20, 541, 551))
        self.textBoxLyrics.setReadOnly(True)
        self.textBoxLyrics.setObjectName("textBoxLyrics")
        self.btnGetSpotHandle = QtWidgets.QPushButton(Dialog)
        self.btnGetSpotHandle.setGeometry(QtCore.QRect(20, 20, 161, 23))
        self.btnGetSpotHandle.setObjectName("btnGetSpotHandle")
        self.btnFetchLyrics = QtWidgets.QPushButton(Dialog)
        self.btnFetchLyrics.setGeometry(QtCore.QRect(210, 20, 131, 23))
        self.btnFetchLyrics.setObjectName("btnFetchLyrics")
        self.lblSpotifyHandle = QtWidgets.QLabel(Dialog)
        self.lblSpotifyHandle.setGeometry(QtCore.QRect(380, 20, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblSpotifyHandle.setFont(font)
        self.lblSpotifyHandle.setObjectName("lblSpotifyHandle")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lyrical"))
        self.btnGetSpotHandle.setText(_translate("Dialog", "Get Spotify Window Handler"))
        self.btnFetchLyrics.setText(_translate("Dialog", "Fetch Lyrics!"))
        self.lblSpotifyHandle.setText(_translate("Dialog", "Dont play anything yet!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

