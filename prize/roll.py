import sys, random
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        self.lcd = lcd
        dial = QDial(self)
        btn1 = QPushButton('결과확인', self)
        btn2 = QPushButton('종료', self)
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.result)
        btn2.clicked.connect(self.exit_bt)

        self.setWindowTitle('경품 당첨')
        self.setGeometry(700, 300, 400,450) # 창 위치 및 크기
        self.show()

    def result(self):   # 결과 확인
        text = '꽝입니디.'
        ran = random.sample(range(1, 101), 6)
        first = ran[0]
        second = ran[1:]
        display_value = self.lcd.intValue()
        print(ran)
        if display_value == first:
            text = '1등입니다.'
        elif display_value in second:
            text = '2등입니다.'

        QMessageBox.about(self, "결과는!?", text)

    def exit_bt(self):  # 종료 버튼
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())