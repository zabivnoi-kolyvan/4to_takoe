import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("untitled.ui", self)

        self.k1 = 0
        self.k2 = 0
        self.k3 = 0
        self.btn_on.clicked.connect(self.on_click)
        self.btn_off.clicked.connect(self.off_click)
        self.btn_red.clicked.connect(self.fred)
        self.btn_yellow.clicked.connect(self.fyellow)
        self.btn_green.clicked.connect(self.fgreen)


    def fred(self):
        if self.k1 == 0:
            self.btn_red.setStyleSheet("""
                        QPushButton{
                        background-color: red;
                        border-radius: 30px;
                    }
                    """)
            self.k1 = 1
        else:
            self.btn_red.setStyleSheet("""
                        QPushButton{
                        background-color: rgb(44, 44, 44);
                        border-radius: 30px;
                    }
                    """)
            self.k1 = 0

    def fyellow(self):
        if self.k2 == 0:
            self.btn_yellow.setStyleSheet("""
                        QPushButton{
                        background-color: yellow;
                        border-radius: 30px;
                    }
                    """)
            self.k2 = 1
        else:
            self.btn_yellow.setStyleSheet("""
                        QPushButton{
                        background-color: rgb(44, 44, 44);
                        border-radius: 30px;
                    }
                    """)
            self.k2 = 0

    def fgreen(self):
        if self.k3 == 0:
            self.btn_green.setStyleSheet("""
                        QPushButton{
                        background-color: green;
                        border-radius: 30px;
                    }
                    """)
            self.k3 = 1
        else:
            self.btn_green.setStyleSheet("""
                        QPushButton{
                        background-color: rgb(44, 44, 44);
                        border-radius: 30px;
                    }
                    """)
            self.k3 = 0
    def on_click(self):
        self.btn_red.setStyleSheet("""
            QPushButton{
            background-color: red;
            border-radius: 30px;
        }
        """)
        self.btn_yellow.setStyleSheet("""
                    QPushButton{
                    background-color: yellow;
                    border-radius: 30px;
                }
                """)
        self.btn_green.setStyleSheet("""
                    QPushButton{
                    background-color: green;
                    border-radius: 30px;
                }
                """)
    def off_click(self):
        self.btn_red.setStyleSheet("""
            QPushButton{
            background-color: rgb(44, 44, 44);
            border-radius: 30px;
        }
        """)
        self.btn_yellow.setStyleSheet("""
                    QPushButton{
                    background-color: rgb(44, 44, 44);
                    border-radius: 30px;
                }
                """)
        self.btn_green.setStyleSheet("""
                    QPushButton{
                    background-color: rgb(44, 44, 44);
                    border-radius: 30px;
                }
                """)




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()