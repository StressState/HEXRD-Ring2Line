# -*- coding: utf-8 -*-
"""
2020.08.18创建
mac文件预览窗口
Harbin Institute of Technology
Author: Kesong Miao
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MacWindow(QWidget):
    '''
    传入参数通过MacWindow(macpara)调用，其中macpara通过read()函数读取
    '''
    def __init__(self, macpara):
        super().__init__()
        self.initUI(macpara)

    def initUI(self, macpara):
        self.resize(700, 300)
        self.setWindowTitle('.mac文件预览')
        macwindow_layout = QGridLayout(self)
        textedit_macpreview = QTextEdit()
        textedit_macpreview.setFontFamily('Arial')
        textedit_macpreview.setFontPointSize(14)
        textedit_macpreview.setText(macpara)
        macwindow_layout.addWidget(textedit_macpreview)
        self.setLayout(macwindow_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = open('Sample.txt')
    para = f.read()
    print(para)
    main = MacWindow(para)
    main.show()
    sys.exit(app.exec_())