#runs GUI and gets the input to write to file and fetch music.
import io
import json
import os
import songcacher

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	app.exec_()
	a = window.artist.text()
	s = window.song.text()
	Entry = Music(a, s)
    button.clicked.connect(Entry.sound())
	file = "music_diary.json" 
	with open(file, 'w') as json_file:
		json.dump(Entry, json_file)