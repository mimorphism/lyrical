import win32gui
import requests
import pickle
import sys
from bs4 import BeautifulSoup
from lyrical_form import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
import os


class LyricalForm(QDialog):
    def __init__(self, parent=None):
        super(LyricalForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnGetSpotHandle.clicked.connect(self.saveSpotifyHandle)
        self.ui.btnFetchLyrics.clicked.connect(self.run_them_all)
        self.spotify_window_handle = self.getSpotifyWindowHandle()

    def saveSpotifyHandle(self):
        try:
            spotifyhandle = win32gui.FindWindowEx(None, None, None, "Spotify")
            if spotifyhandle == 0:
                pass
            else:
                with open("spotifyhandle/spothandle.pickle", "wb") as f:
                    pickle.dump(spotifyhandle, f)
                print("Spotify handle successfully saved")

        except Exception as e:
            print(e)



    def getSpotifyWindowHandle(self):
        # test.saveSpotifyHandle()
        spotify_window_handle = pickle.load(open("spotifyhandle/spothandle.pickle", "rb"))
        self.ui.lblSpotifyHandle.setText("Spotify handle : {}".format(spotify_window_handle))
        return spotify_window_handle


    def getSongTitle(self, spotify_window_handle):
        self.song_name = win32gui.GetWindowText(spotify_window_handle)
        return self.song_name


    def getSongInfo(self, songname):
        try:
            song_info = None
            song_name = songname.split('-')
            artistname = song_name[0].strip()
            trackname = song_name[1].strip()
            url = 'https://api.genius.com/search'
            mytoken = "INSERT YOUR OWN TOKEN"
            header = {'Authorization': 'Bearer ' + mytoken}
            data = {'q': trackname + ' ' + artistname}
            response = requests.get(url, data=data, headers=header)
            response = response.json()
            for match in response['response']['hits']:
                if artistname.lower() in match['result']['primary_artist']['name'].lower():
                    song_info = match
                    break
                else:
                    break
            return song_info
        except IndexError as e:
            QMessageBox.critical(self, "Error",
                                 "Error getting the lyrics for the song! Maybe an ad is playing...")




    def getThemLyrics(self, song_info):
        try:
            lyricspath = song_info['result']['url']
            page = requests.get(lyricspath)
            bsobject = BeautifulSoup(page.text, 'lxml')
            lyrics = bsobject.find('div', class_='lyrics').get_text()
            self.ui.textBoxLyrics.setPlainText(lyrics)
            self.ui.gBoxLyrical.setTitle(self.song_name)
        except TypeError as e:
            QMessageBox.critical(self, "Error", "Error getting the lyrics for the song! Maybe an ad is playing or you're a hipster ass who listen to obscure muzique ;)")





    def run_them_all(self):
        sonk = self.getSongTitle(self.spotify_window_handle)
        sonk2 = self.getSongInfo(sonk)
        self.getThemLyrics(sonk2)




# if __name__ == '__main__':
#     sonk = getSpotifyWindowHandle()
#     sonk2 = getSongTitle(sonk)
#     sonk3 = getSongInfo(sonk2)
#     getThemLyrics(sonk3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LyricalForm()
    main.show()

    sys.exit(app.exec_())







