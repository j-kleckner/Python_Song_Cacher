import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Builds GUI main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Music Diary") 

        label = QLabel("Please Enter Artist, Song Title.") 
        lab_a = QLabel("Artist")
        lab_s = QLabel("Song")
        artist = QLineEdit(self)
        song = QLineEdit(self)
        button = QPushButton("Play/Stop")
        

        label.setAlignment(Qt.AlignCenter)
        lab_a.setAlignment(Qt.AlignBottom & Qt.AlignLeft)
        lab_s.setAlignment(Qt.AlignBottom & Qt.AlignCenter)
        artist.setAlignment(Qt.AlignBottom & Qt.AlignLeft)
        song.setAlignment(Qt.AlignBottom & Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
        button.show()
        
