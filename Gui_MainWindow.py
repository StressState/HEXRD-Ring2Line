# -*- coding: utf-8 -*-
"""
2020.08.18创建
用于处理HEXRD将德拜衍射环转换为线
Harbin Institute of Technology
Author: Kesong Miao
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Gui_macpreview import MacWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global macpara_list #定义Fit2D的核心mac文件为全局
        macpara_list = open('./Sample.txt').readlines()
        global lastdir #记住上次选择的路径
        lastdir = "./"
        self.mainGUI = self.initUI()




    def initUI(self):
        self.resize(1088, 437)
        self.setWindowTitle('高能X射线衍射切向积分软件')
        _translate = QCoreApplication.translate #html富文本翻译


        '''布局调整'''
        #文件路径布局
        horizontalLayout_datapath_widget = QWidget(self)
        horizontalLayout_datapath_widget.setGeometry(QRect(10, 20, 591, 41))
        horizontalLayout_datapath = QHBoxLayout(horizontalLayout_datapath_widget)
        horizontalLayout_datapath.setContentsMargins(0, 0, 0, 0)

        label_datapath = QLabel('<b><font size=4>数据文件夹路径:</font></b>')
        self.lineedit_datapath = QLineEdit() #需要在槽函数中修改的需要定义为Attribute

        horizontalLayout_datapath.addWidget(label_datapath)
        horizontalLayout_datapath.addWidget(self.lineedit_datapath)

        #实验参数布局
        frame_exppara = QFrame(self)
        frame_exppara.setGeometry(QRect(10, 60, 291, 361))
        frame_exppara.setFrameShape(QFrame.Box)
        frame_exppara.setFrameShadow(QFrame.Plain)

        gridLayout_exppara_widget = QWidget(frame_exppara)
        gridLayout_exppara_widget.setGeometry(QRect(20, 40, 251, 311))
        gridLayout_exppara = QGridLayout(gridLayout_exppara_widget)
        gridLayout_exppara.setContentsMargins(0, 0, 0, 0)

        label_beamcenterx = QLabel()
        label_beamcentery = QLabel()
        label_wavelength = QLabel()
        label_sample2detector = QLabel()
        label_detectortiltrotation = QLabel()
        label_detectortiltangle = QLabel()
        label_exppara = QLabel(frame_exppara)
        label_exppara.setGeometry(QRect(20, 10, 131, 31))

        label_beamcenterx.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束中心 X</span></p><p><span style=\" font-weight:600;\">(Beam Center X)</span></p></body></html>"))
        label_beamcentery.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束中心 Y</span></p><p><span style=\" font-weight:600;\">(Beam Center Y)</span></p></body></html>"))
        label_wavelength.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束波长(埃)</span></p><p><span style=\" font-weight:600;\">(WaveLength)</span></p></body></html>"))
        label_sample2detector.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器距离（毫米）</span></p><p><span style=\" font-weight:600;\">(Sample to Detector)</span></p></body></html>"))
        label_detectortiltrotation.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器倾斜方向(度)</span></p><p><span style=\" font-weight:600;\">(Detector tilt rotation)</span></p></body></html>"))
        label_detectortiltangle.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器倾斜角度(度)</span></p><p><span style=\" font-weight:600;\">(Detector tilt angle)</span></p></body></html>"))
        label_exppara.setText(_translate('', "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">实验修正参数</span></p></body></html>"))

        gridLayout_exppara.addWidget(label_beamcenterx, 1, 0, 1, 1)
        gridLayout_exppara.addWidget(label_beamcentery, 2, 0, 1, 1)
        gridLayout_exppara.addWidget(label_wavelength, 3, 0, 1, 1)
        gridLayout_exppara.addWidget(label_sample2detector, 4, 0, 1, 1)
        gridLayout_exppara.addWidget(label_detectortiltrotation, 5, 0, 1, 1)
        gridLayout_exppara.addWidget(label_detectortiltangle, 6, 0, 1, 1)

        self.lineedit_beamcenterx = QLineEdit()
        self.lineedit_beamcentery = QLineEdit()
        self.lineedit_wavelength = QLineEdit()
        self.lineedit_sample2detector = QLineEdit()
        self.lineedit_detectortiltrotation = QLineEdit()
        self.lineedit_detectortiltangle = QLineEdit()

        gridLayout_exppara.addWidget(self.lineedit_beamcenterx, 1, 1, 1, 1)
        gridLayout_exppara.addWidget(self.lineedit_beamcentery, 2, 1, 1, 1)
        gridLayout_exppara.addWidget(self.lineedit_wavelength, 3, 1, 1, 1)
        gridLayout_exppara.addWidget(self.lineedit_sample2detector, 4, 1, 1, 1)
        gridLayout_exppara.addWidget(self.lineedit_detectortiltrotation, 5, 1, 1, 1)
        gridLayout_exppara.addWidget(self.lineedit_detectortiltangle, 6, 1, 1, 1)

        expparaconfirmbtn = QPushButton('确认')
        gridLayout_exppara.addWidget(expparaconfirmbtn, 7, 0, 1, 2)

        #处理参数布局
        frame_processpara = QFrame(self)
        frame_processpara.setGeometry(QRect(310, 60, 291, 361))
        frame_processpara.setFrameShape(QFrame.Box)
        frame_processpara.setFrameShadow(QFrame.Plain)

        gridLayout_processpara_widget = QWidget(frame_processpara)
        gridLayout_processpara_widget.setGeometry(QRect(20, 40, 251, 311))
        gridLayout_processpara = QGridLayout(gridLayout_processpara_widget)
        gridLayout_processpara.setContentsMargins(0, 0, 0, 0)

        label_firstazimuthangle = QLabel()
        label_lastazimuthangle = QLabel()
        label_innerradius = QLabel()
        label_outerradius = QLabel()
        label_savefoldername = QLabel()
        label_processpara = QLabel(frame_processpara)
        label_processpara.setGeometry(QRect(20, 10, 131, 31))

        label_firstazimuthangle.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分初始角度(度)</span></p><p><span style=\" font-weight:600;\">(First azimuth angle)</span></p></body></html>"))
        label_lastazimuthangle.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分终止角度(度)</span></p><p><span style=\" font-weight:600;\">(Last azimuth angle)</span></p></body></html>"))
        label_innerradius.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分起始半径(像素)</span></p><p><span style=\" font-weight:600;\">(Inner radius)</span></p></body></html>"))
        label_outerradius.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分终止半径(像素)</span></p><p><span style=\" font-weight:600;\">(Outer radius)</span></p></body></html>"))
        label_savefoldername.setText(_translate('', "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">保存文件夹名称</span></p><p><span style=\" font-weight:600;\">(Save in folder)</span></p></body></html>"))
        label_processpara.setText(_translate('', "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">积分处理参数</span></p></body></html>"))

        gridLayout_processpara.addWidget(label_firstazimuthangle, 1, 0, 1, 1)
        gridLayout_processpara.addWidget(label_lastazimuthangle, 2, 0, 1, 1)
        gridLayout_processpara.addWidget(label_innerradius, 3, 0, 1, 1)
        gridLayout_processpara.addWidget(label_outerradius, 4, 0, 1, 1)
        gridLayout_processpara.addWidget(label_savefoldername, 5, 0, 1, 1)

        self.lineedit_firstazimuthangle = QLineEdit()
        self.lineedit_lastazimuthangle = QLineEdit()
        self.lineedit_innerradius = QLineEdit()
        self.lineedit_outerradius = QLineEdit()
        self.lineedit_savefoldername = QLineEdit()

            #设置默认值
        self.lineedit_firstazimuthangle.setText('0')
        self.lineedit_lastazimuthangle.setText('360')
        self.lineedit_savefoldername.setText('Ring2Line')

        gridLayout_processpara.addWidget(self.lineedit_firstazimuthangle, 1, 1, 1, 1)
        gridLayout_processpara.addWidget(self.lineedit_lastazimuthangle, 2, 1, 1, 1)
        gridLayout_processpara.addWidget(self.lineedit_innerradius, 3, 1, 1, 1)
        gridLayout_processpara.addWidget(self.lineedit_outerradius, 4, 1, 1, 1)
        gridLayout_processpara.addWidget(self.lineedit_savefoldername, 5, 1, 1, 1)

        processparaconfirmbtn = QPushButton('确认')
        gridLayout_processpara.addWidget(processparaconfirmbtn, 6, 0, 1, 2)

        #显示控制布局
        gridLayout_displaycontrol_widget = QWidget(self)
        gridLayout_displaycontrol_widget.setGeometry(QRect(610, 370, 451, 47))
        gridLayout_displaycontrol = QGridLayout(gridLayout_displaycontrol_widget)
        gridLayout_displaycontrol.setContentsMargins(0, 0, 0, 0)

        check_color = QCheckBox('彩色模式')
        check_scale = QCheckBox('显示标尺')
        check_preview = QCheckBox('显示预览')
        check_preview.setChecked(True)

        label_intensity = QLabel('显示调节')
        label_intensity.alignment()
        Hbar_intensity = QScrollBar(gridLayout_displaycontrol_widget)

        Hbar_intensity.setOrientation(Qt.Horizontal)
        Hbar_intensity.setProperty("value", 49)

        label_processtimer = QLabel('出图进度')
        progressBar_processtimer = QProgressBar(gridLayout_displaycontrol_widget)
        progressBar_processtimer.setProperty("value", 0)

        gridLayout_displaycontrol.addWidget(label_processtimer, 1, 0, 1, 1)
        gridLayout_displaycontrol.addWidget(progressBar_processtimer, 1, 1, 1, 5)
        gridLayout_displaycontrol.addWidget(check_color, 2, 0, 1, 1)
        gridLayout_displaycontrol.addWidget(check_scale, 2, 1, 1, 1)
        gridLayout_displaycontrol.addWidget(check_preview, 2, 2, 1, 1)
        gridLayout_displaycontrol.addWidget(label_intensity, 2, 3, 1, 1)
        gridLayout_displaycontrol.addWidget(Hbar_intensity, 2, 4, 1, 2)

        #图像窗口
        graphicsview_intergratepic = QGraphicsView(self)
        graphicsview_intergratepic.setGeometry(QRect(610, 30, 451, 331))

        #Tab顺序
        MainWindow.setTabOrder(self.lineedit_datapath, self.lineedit_beamcenterx)
        MainWindow.setTabOrder(self.lineedit_beamcenterx, self.lineedit_beamcentery)
        MainWindow.setTabOrder(self.lineedit_beamcentery, self.lineedit_wavelength)
        MainWindow.setTabOrder(self.lineedit_wavelength, self.lineedit_sample2detector)
        MainWindow.setTabOrder(self.lineedit_sample2detector, self.lineedit_detectortiltrotation)
        MainWindow.setTabOrder(self.lineedit_detectortiltrotation, self.lineedit_detectortiltangle)
        MainWindow.setTabOrder(self.lineedit_detectortiltangle, self.lineedit_firstazimuthangle)
        MainWindow.setTabOrder(self.lineedit_firstazimuthangle, self.lineedit_lastazimuthangle)
        MainWindow.setTabOrder(self.lineedit_lastazimuthangle, self.lineedit_innerradius)
        MainWindow.setTabOrder(self.lineedit_innerradius, self.lineedit_outerradius)
        MainWindow.setTabOrder(self.lineedit_outerradius, self.lineedit_savefoldername)
        MainWindow.setTabOrder(self.lineedit_savefoldername, check_color)
        MainWindow.setTabOrder(check_color, check_scale)
        MainWindow.setTabOrder(check_scale, check_preview)

        #菜单布局
        menubar = self.menuBar()
        menubar.setGeometry(QRect(0, 0, 1088, 22))

        menu_file = menubar.addMenu('文件')
        menu_proccess = menubar.addMenu('处理')
        menu_debug = menubar.addMenu('调试')
        menu_info = menubar.addMenu('关于')

        menu_file_openfolder = menu_file.addAction('打开数据文件夹')
        menu_file_inputpara = menu_file.addAction('导入处理参数')
        menu_file_outputpara = menu_file.addAction('导出处理参数')

        menu_proccess_runtest = menu_proccess.addAction('单张积分测试')
        menu_proccess_run = menu_proccess.addAction('批量处理积分')
        menu_proccess_runoutputpictest = menu_proccess.addAction('测试出图')
        menu_proccess_runoutputpic = menu_proccess.addAction('批量出图')

        menu_debug_fit2dmac = menu_debug.addAction("查看MAC文件")

        '''信号-槽调整'''
        '''实验参数信号'''
        '''处理参数信号'''
        '''显示控制信号'''
        check_preview.toggled['bool'].connect(graphicsview_intergratepic.setVisible)
        '''菜单栏信号'''
        menu_file_openfolder.triggered.connect(self.menu_file_openfolder_trigger)
        menu_file_inputpara.triggered.connect(self.menu_file_inputpara_trigger)
        menu_file_outputpara.triggered.connect(self.menu_file_outputpara_trigger)
        menu_debug.triggered.connect(self.menu_debug_trigger)

    '''槽函数'''
    def menu_file_openfolder_trigger(self):
        '''菜单栏-文件-打开数据文件夹'''
        global lastdir
        datapath = QFileDialog.getExistingDirectory(self, "选取文件夹", lastdir)
        if datapath == "":
            return
        lastdir = datapath
        #输入值给datapath文本框
        self.lineedit_datapath.setText(datapath)

    def menu_file_inputpara_trigger(self):
        '''菜单栏-文件-导入处理参数'''
        global macpara_list, lastdir
        parapath, paratpye = QFileDialog.getOpenFileName(self, "选取文件夹", lastdir)
        if parapath == "":
            return
        lastdir = parapath
        macpara_list = open(parapath).readlines()
        #调整界面显示
        self.lineedit_firstazimuthangle.setText(macpara_list[1])
        self.lineedit_lastazimuthangle.setText(macpara_list[3])
        self.lineedit_innerradius.setText(macpara_list[5])
        self.lineedit_outerradius.setText(macpara_list[7])
        self.lineedit_beamcenterx.setText(macpara_list[17])
        self.lineedit_beamcentery.setText(macpara_list[19])
        self.lineedit_wavelength.setText(macpara_list[21])
        self.lineedit_sample2detector.setText(macpara_list[23])
        self.lineedit_detectortiltrotation.setText(macpara_list[29])
        self.lineedit_detectortiltangle.setText(macpara_list[31])
        self.lineedit_savefoldername.setText(macpara_list[43])

    def menu_file_outputpara_trigger(self):
        global macpara_list, lastdir
        parapath, paratype = QFileDialog.getSaveFileName(self, "输出处理参数", lastdir+"/Fit2D_para.txt", "*.txt")
        if parapath == "":
            return
        lastdir = parapath
        savefile = open(parapath, "w")
        for line in macpara_list:
            savefile.write(line)
        savefile.close()

    def menu_debug_trigger(self):
        '''读取当前的macpara并显示在新窗口中'''
        global macpara_list
        macpara = ''.join(macpara_list) #转换list 为 str
        self.macGUI = MacWindow(macpara)
        self.macGUI.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())