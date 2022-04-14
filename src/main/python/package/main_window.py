from PySide2.QtWidgets import QMainWindow, QToolBar
from PySide2 import QtMultimedia, QtMultimediaWidgets, QtWidgets


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

    def create_widgets(self):
        self.video_widget=QtMultimediaWidgets.QVideoWidget()#Lire les video
        self.player=QtMultimedia.QMediaPlayer()
        self.toolbar=QToolBar()
        self.file_menu=self.menuBar().addMenu("Fichier")


    def modify_widgets(self):
        pass
    def create_layouts(self):
        pass
    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.video_widget)
        self.player.setVideoOutput(self.video_widget)

    def setup_connections(self):
        pass