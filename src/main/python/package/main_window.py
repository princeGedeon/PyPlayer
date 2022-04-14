from functools import partial
import torchvision
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QMainWindow, QToolBar, QFileDialog, QDialog
from PyQt5 import QtMultimedia, QtMultimediaWidgets, QtWidgets,QtCore



class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mon Lecteur")

        self.open_icon=self.style().standardIcon(QtWidgets.QStyle.SP_DriveDVDIcon)
        self.play_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
        self.previous_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaSeekBackward)
        self.pause_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause)
        self.stop_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop)
        self.setup_ui()



    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.video_widget=QtMultimediaWidgets.QVideoWidget()#Lire les video
        self.player=QtMultimedia.QMediaPlayer()
        self.toolbar=QToolBar()
        self.file_menu=self.menuBar().addMenu("Fichier")

        #ACTIONS
        self.act_open=self.file_menu.addAction(self.open_icon,"Ouvrir")
        self.act_open.setShortcut("Ctrl+O")
        self.act_play=self.toolbar.addAction(self.play_icon,"Lire")
        self.act_previous=self.toolbar.addAction(self.previous_icon,"Revenir au debut")
        self.act_pause = self.toolbar.addAction(self.pause_icon, "Faire une pause")
        self.act_stop = self.toolbar.addAction(self.stop_icon, "Arreter")


    def modify_widgets(self):
        self.toolbar.setStyleSheet("background-color:black;")
    def create_layouts(self):
        pass
    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.video_widget)
        self.player.setVideoOutput(self.video_widget)

    def setup_connections(self):
        self.act_open.triggered.connect(self.open)
        self.act_play.triggered.connect(self.play)
        self.act_pause.triggered.connect(self.player.pause)
        self.act_stop.triggered.connect(self.player.stop)
        self.act_previous.triggered.connect(partial(self.player.setPosition,0))
        self.player.stateChanged.connect(self.update_buttons)



    def play(self):
        self.player.play()


    def update_buttons(self,state):

        self.act_play.setDisabled(state==QtMultimedia.QMediaPlayer.PlayingState)
        self.act_pause.setDisabled(state == QtMultimedia.QMediaPlayer.PausedState)
        self.act_stop.setDisabled(state == QtMultimedia.QMediaPlayer.StoppedState)

    def open(self):
        file_dialog=QFileDialog(self)
        file_dialog.setMimeTypeFilters(['video/mp4',"video/mkv","video.avi"])
        movie_dir=QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movie_dir)

        if file_dialog.exec_()==QDialog.Accepted:
            movie=file_dialog.selectedUrls()[0]
            self.player.setMedia(QMediaContent(movie))
            self.player.play()