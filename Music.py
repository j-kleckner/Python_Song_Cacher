#This class will open a json file to add music entries to.  It will load the entry and play it if it exists
from os import path
from pygame import mixer
import json
import urllib.request

class Music(object):
    #load json file
    def __init__(self):
        self.file = "music.json"
        if path.exists(self.file):
            with open(self.file, 'r') as json_file:
                self.db = json.load(json_file)
        else:
            # self.db = [["artist","song", "file"]]
            self.db = []
    
    #play MP3
    def sound(self, file):
        mixer.init()
        mixer.music.load('./{}'.format(file))
        mixer.music.play()

    #check to see if song exists
    def lookup(self, artist, song):
        for entry in self.db:
            if entry[0] == artist and entry[1] == song:
                return entry
        return None

    #download song from archive.org  
    def download(self, artist, song):
        a = urllib.parse.quote(artist)
        s = urllib.parse.quote(song)
        url = "https://ia601504.us.archive.org/16/items/{}/{}.mp3".format(a,s)
        filepath = "{} - {}.mp3".format(artist, song)
        try:
            urllib.request.urlretrieve(url, filepath)
        except:
            return None
        return filepath

    #add song/artist/filepath (song.mp3) to db
    def Add(self, artist, song, filepath):
        self.db.append([artist, song, filepath])
        
        with open(self.file, 'w') as json_file:
            json.dump(self.db, json_file)
