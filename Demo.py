import sys
import Gui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Gui_MainWindow.MainWindow()
    main.show()
    print('sdaf')
    sys.exit(app.exec_())