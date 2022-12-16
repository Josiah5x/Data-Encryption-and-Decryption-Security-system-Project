import sys
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import(QApplication, QWidget, QLineEdit, QPushButton, QPlainTextEdit)
from PyQt5.Qt import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 450)

        self.search = QLineEdit(self)
        self.search.setGeometry(QRect(10, 0, 200, 40))

        self.btn_search = QPushButton(self)
        self.btn_search.setGeometry(QRect(225, 0, 120, 40))
        self.btn_search.setText("Search")
        self.btn_search.clicked.connect(self.search_verse)

        self.plaintext = QPlainTextEdit(self)
        self.plaintext.setGeometry(QRect(10, 50, 400, 400))
    
    def search_verse(self):
        dictionary={"Psalm 1": """QRect(int, int, int, int): not enough arguments
                    QRect(QPoint, QPoint): argument 1 has unexpected type 'int'
                    QRect(QPoint, QSize): argument 1 has unexpected type 'int'
                    QRect(QRect): argument 1 has unexpected type 'int'"""}
        if self.search.text() in dictionary:
            print("hello")
        else:
            print("Error")


if __name__ in '__main__':
    app = QApplication(sys.argv)

    demo = MainApp()
    demo.show()

    sys.exit(app.exec_())