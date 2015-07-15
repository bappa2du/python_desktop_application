from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        url.setPlaceholderText("URL")
        save_location.setPlaceholderText("File save Location")

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()