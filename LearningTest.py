import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TooltipForm(QWidget):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):

        self.setToolTip('打法发打法 ')
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('a12dkjfa大咖啡机')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())