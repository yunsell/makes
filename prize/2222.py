import sys
from PyQt5.QtWidgets import *

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('눌러주세요', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('버튼을 설명해줌.')
        btn.move(25, 30)

        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('첫번째 윈도우')
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
