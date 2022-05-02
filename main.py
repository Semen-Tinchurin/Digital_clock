import sys
import pyglet
from datetime import datetime
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

pyglet.font.add_file("digital-7.ttf")


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        # self.oldPosition = None
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.color = '#31ee14'
        self.bgcolor = 'black'
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.start()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.setupLabels)
        self.timer.start(100)

    def start(self):
        self.window.setWindowTitle('Digital Clock')
        self.window.setWindowIcon(QIcon('digital-clock.png'))
        self.window.setFixedSize(400, 200)
        self.window.setStyleSheet(f'background-color: {self.bgcolor};')
        self.setupLabels()
        # self.get_date_and_time()
        self.window.show()

    def setupLabels(self):
        self.label1.setText(datetime.now().strftime('%H:%M:%S'))
        self.label2.setText(f"{datetime.now().strftime('%A')}        {datetime.now().strftime('%d-%m-%Y')}")

        self.label1.setStyleSheet(f'color: {self.color};')
        self.label1.setFont(QFont('digital-7', 80))
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2.setStyleSheet(f'color: {self.color};')
        self.label2.setFont(QFont('digital-7', 20))
        self.label2.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.window.setLayout(self.layout)
        # flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.WindowStaysOnTopHint)
        # self.window.setWindowFlags(flags)


# self.l1.layout(self.window)
# def mousePressEvent(self, event):
#     self.oldPosition = event.globalPos()
#
# # action #2
# def mouseMoveEvent(self, event):
#     delta = QPoint(event.globalPos() - self.oldPosition)
#     self.move(self.x() + delta.x(), self.y() + delta.y())
#     self.oldPosition = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    app.exec_()
