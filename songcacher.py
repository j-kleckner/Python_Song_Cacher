# This following code produces a GUI -> GUI created using QT tools
import io
import json
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Music import Music


class Ui_SongCacher(object):

    # Added by me
    def __init__(self, music_db):
        self.music_db = music_db

    def setupUi(self, SongCacher):
        SongCacher.setObjectName("SongCacher")
        SongCacher.resize(363, 320)
        self.A_Input = QtWidgets.QLineEdit(SongCacher)
        self.A_Input.setGeometry(QtCore.QRect(10, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.A_Input.setFont(font)
        self.A_Input.setObjectName("A_Input")
        self.S_Input = QtWidgets.QLineEdit(SongCacher)
        self.S_Input.setGeometry(QtCore.QRect(140, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.S_Input.setFont(font)
        self.S_Input.setObjectName("S_Input")
        self.Artist = QtWidgets.QLabel(SongCacher)
        self.Artist.setGeometry(QtCore.QRect(10, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Artist.setFont(font)
        self.Artist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Artist.setAutoFillBackground(True)
        self.Artist.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.Artist.setObjectName("Artist")
        self.Song = QtWidgets.QLabel(SongCacher)
        self.Song.setGeometry(QtCore.QRect(140, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.Song.setFont(font)
        self.Song.setAutoFillBackground(True)
        self.Song.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.Song.setObjectName("Song")
        self.Prompt = QtWidgets.QLabel(SongCacher)
        self.Prompt.setGeometry(QtCore.QRect(20, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.Prompt.setFont(font)
        self.Prompt.setObjectName("Prompt")
        self.LoadPrompt = QtWidgets.QLabel(SongCacher)
        self.LoadPrompt.setGeometry(QtCore.QRect(20, 170, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setItalic(True)
        self.LoadPrompt.setFont(font)
        self.LoadPrompt.setObjectName("LoadPrompt")
        self.pushButton = QtWidgets.QPushButton(SongCacher)
        self.pushButton.setGeometry(QtCore.QRect(270, 160, 75, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.ErrorLabel = QtWidgets.QLabel(SongCacher)
        self.ErrorLabel.setGeometry(QtCore.QRect(40, 230, 271, 41))
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")

        self.retranslateUi(SongCacher)
        QtCore.QMetaObject.connectSlotsByName(SongCacher)
        
        # Added by me
        self.pushButton.clicked.connect(self.play)

    def retranslateUi(self, SongCacher):
        _translate = QtCore.QCoreApplication.translate
        SongCacher.setWindowTitle(_translate("SongCacher", "Song Cacher"))
        self.Artist.setText(_translate("SongCacher", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Artist</span></p></body></html>"))
        self.Song.setText(_translate("SongCacher", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Song</span></p></body></html>"))
        self.Prompt.setText(_translate("SongCacher", "Enter Artist and Song Title"))
        self.LoadPrompt.setText(_translate("SongCacher", "<html><head/><body><p align=\"center\">Click Play To Cache Song and Play. </p></body></html>"))
        self.pushButton.setText(_translate("SongCacher", "Play"))
        
    # addded by me, checks for song entry and will call to add to db and play
    def play(self):
        artist = self.A_Input.text()
        song = self.S_Input.text()
        
        entry = self.music_db.lookup(artist, song)
        if entry is None:
            # attempt to download (add function)
            # if failure, return failure and cannot download messge
            # if success, song = new entry
            self.ErrorLabel.setText("Attempting Download")
            files = self.music_db.download(artist, song)
            if files is None:
                self.ErrorLabel.setText("Error:Cannot Fetch Song {} - {}".format(artist,song))
            else:
                self.music_db.Add(artist, song, files)
        else:
            files = entry[2]
        
        # play song
        if files is not None:
            self.ErrorLabel.setText("Playing...Click to Play Again/Enter New Song")
            self.music_db.sound(files)
        else:
            self.ErrorLabel.setText("Cannot find song...Enter New Song")
            

#Main to run GUI       
if __name__ == "__main__":
    music_db = Music()
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    ui = Ui_SongCacher(music_db)
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_()) 
