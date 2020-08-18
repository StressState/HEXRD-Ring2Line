# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_exppara = QtWidgets.QFrame(self.centralwidget)
        self.frame_exppara.setGeometry(QtCore.QRect(10, 60, 291, 361))
        self.frame_exppara.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_exppara.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_exppara.setObjectName("frame_exppara")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_exppara)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 251, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_exppara = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_exppara.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_exppara.setObjectName("gridLayout_exppara")
        self.label_sample2detector = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sample2detector.setTextFormat(QtCore.Qt.AutoText)
        self.label_sample2detector.setObjectName("label_sample2detector")
        self.gridLayout_exppara.addWidget(self.label_sample2detector, 4, 0, 1, 1)
        self.label_wavelength = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wavelength.setTextFormat(QtCore.Qt.AutoText)
        self.label_wavelength.setObjectName("label_wavelength")
        self.gridLayout_exppara.addWidget(self.label_wavelength, 3, 0, 1, 1)
        self.label_detectortiltrotation = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_detectortiltrotation.setTextFormat(QtCore.Qt.AutoText)
        self.label_detectortiltrotation.setObjectName("label_detectortiltrotation")
        self.gridLayout_exppara.addWidget(self.label_detectortiltrotation, 6, 0, 1, 1)
        self.label_beamcenterx = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_beamcenterx.setTextFormat(QtCore.Qt.AutoText)
        self.label_beamcenterx.setObjectName("label_beamcenterx")
        self.gridLayout_exppara.addWidget(self.label_beamcenterx, 1, 0, 1, 1)
        self.label_beamcentery = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_beamcentery.setTextFormat(QtCore.Qt.AutoText)
        self.label_beamcentery.setObjectName("label_beamcentery")
        self.gridLayout_exppara.addWidget(self.label_beamcentery, 2, 0, 1, 1)
        self.lineedit_beamcenterx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_beamcenterx.setObjectName("lineedit_beamcenterx")
        self.gridLayout_exppara.addWidget(self.lineedit_beamcenterx, 1, 1, 1, 1)
        self.lineedit_beamcentery = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_beamcentery.setObjectName("lineedit_beamcentery")
        self.gridLayout_exppara.addWidget(self.lineedit_beamcentery, 2, 1, 1, 1)
        self.lineedit_wavelength = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_wavelength.setObjectName("lineedit_wavelength")
        self.gridLayout_exppara.addWidget(self.lineedit_wavelength, 3, 1, 1, 1)
        self.lineedit_sample2detector = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_sample2detector.setObjectName("lineedit_sample2detector")
        self.gridLayout_exppara.addWidget(self.lineedit_sample2detector, 4, 1, 1, 1)
        self.lineedit_detectortiltrotation = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_detectortiltrotation.setObjectName("lineedit_detectortiltrotation")
        self.gridLayout_exppara.addWidget(self.lineedit_detectortiltrotation, 6, 1, 1, 1)
        self.lineedit_detectortiltangle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineedit_detectortiltangle.setObjectName("lineedit_detectortiltangle")
        self.gridLayout_exppara.addWidget(self.lineedit_detectortiltangle, 8, 1, 1, 1)
        self.label_detectortiltangle = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_detectortiltangle.setTextFormat(QtCore.Qt.AutoText)
        self.label_detectortiltangle.setObjectName("label_detectortiltangle")
        self.gridLayout_exppara.addWidget(self.label_detectortiltangle, 8, 0, 1, 1)
        self.label_exppara = QtWidgets.QLabel(self.frame_exppara)
        self.label_exppara.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label_exppara.setObjectName("label_exppara")
        self.frame_processpara = QtWidgets.QFrame(self.centralwidget)
        self.frame_processpara.setGeometry(QtCore.QRect(310, 60, 291, 361))
        self.frame_processpara.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_processpara.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_processpara.setLineWidth(1)
        self.frame_processpara.setObjectName("frame_processpara")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_processpara)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 251, 311))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_processpara = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_processpara.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_processpara.setObjectName("gridLayout_processpara")
        self.lineedit_innerradius = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineedit_innerradius.setObjectName("lineedit_innerradius")
        self.gridLayout_processpara.addWidget(self.lineedit_innerradius, 3, 1, 1, 1)
        self.lineedit_firstazimuthangle = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineedit_firstazimuthangle.setObjectName("lineedit_firstazimuthangle")
        self.gridLayout_processpara.addWidget(self.lineedit_firstazimuthangle, 1, 1, 1, 1)
        self.label_outerradius = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_outerradius.setTextFormat(QtCore.Qt.AutoText)
        self.label_outerradius.setObjectName("label_outerradius")
        self.gridLayout_processpara.addWidget(self.label_outerradius, 4, 0, 1, 1)
        self.label_savefilename = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_savefilename.setTextFormat(QtCore.Qt.AutoText)
        self.label_savefilename.setObjectName("label_savefilename")
        self.gridLayout_processpara.addWidget(self.label_savefilename, 6, 0, 1, 1)
        self.label_firstazimuthangle = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_firstazimuthangle.setTextFormat(QtCore.Qt.AutoText)
        self.label_firstazimuthangle.setObjectName("label_firstazimuthangle")
        self.gridLayout_processpara.addWidget(self.label_firstazimuthangle, 1, 0, 1, 1)
        self.label_lastazimuthangle = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_lastazimuthangle.setTextFormat(QtCore.Qt.AutoText)
        self.label_lastazimuthangle.setObjectName("label_lastazimuthangle")
        self.gridLayout_processpara.addWidget(self.label_lastazimuthangle, 2, 0, 1, 1)
        self.lineedit_outerradius = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineedit_outerradius.setObjectName("lineedit_outerradius")
        self.gridLayout_processpara.addWidget(self.lineedit_outerradius, 4, 1, 1, 1)
        self.lineedit_savefilename = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineedit_savefilename.setObjectName("lineedit_savefilename")
        self.gridLayout_processpara.addWidget(self.lineedit_savefilename, 6, 1, 1, 1)
        self.lineedit_lastazimuthangle = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineedit_lastazimuthangle.setObjectName("lineedit_lastazimuthangle")
        self.gridLayout_processpara.addWidget(self.lineedit_lastazimuthangle, 2, 1, 1, 1)
        self.label_innerradius = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_innerradius.setTextFormat(QtCore.Qt.AutoText)
        self.label_innerradius.setObjectName("label_innerradius")
        self.gridLayout_processpara.addWidget(self.label_innerradius, 3, 0, 1, 1)
        self.label_processpara = QtWidgets.QLabel(self.frame_processpara)
        self.label_processpara.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label_processpara.setObjectName("label_processpara")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_datapath = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_datapath.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_datapath.setObjectName("horizontalLayout_datapath")
        self.label_datapath = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_datapath.setTextFormat(QtCore.Qt.AutoText)
        self.label_datapath.setObjectName("label_datapath")
        self.horizontalLayout_datapath.addWidget(self.label_datapath)
        self.lineedit_datapath = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineedit_datapath.setObjectName("lineedit_datapath")
        self.horizontalLayout_datapath.addWidget(self.lineedit_datapath)
        self.graphicsview_intergratepic = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsview_intergratepic.setGeometry(QtCore.QRect(610, 20, 451, 341))
        self.graphicsview_intergratepic.setObjectName("graphicsview_intergratepic")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(610, 370, 451, 47))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_displaycontrol = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_displaycontrol.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_displaycontrol.setObjectName("gridLayout_displaycontrol")
        self.check_scale = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.check_scale.setObjectName("check_scale")
        self.gridLayout_displaycontrol.addWidget(self.check_scale, 2, 1, 1, 1)
        self.check_preview = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.check_preview.setChecked(True)
        self.check_preview.setObjectName("check_preview")
        self.gridLayout_displaycontrol.addWidget(self.check_preview, 2, 2, 1, 1)
        self.check_color = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.check_color.setObjectName("check_color")
        self.gridLayout_displaycontrol.addWidget(self.check_color, 2, 0, 1, 1)
        self.Hbar_intensity = QtWidgets.QScrollBar(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hbar_intensity.sizePolicy().hasHeightForWidth())
        self.Hbar_intensity.setSizePolicy(sizePolicy)
        self.Hbar_intensity.setProperty("value", 49)
        self.Hbar_intensity.setOrientation(QtCore.Qt.Horizontal)
        self.Hbar_intensity.setObjectName("Hbar_intensity")
        self.gridLayout_displaycontrol.addWidget(self.Hbar_intensity, 2, 4, 1, 1)
        self.label_intensity = QtWidgets.QLabel(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_intensity.sizePolicy().hasHeightForWidth())
        self.label_intensity.setSizePolicy(sizePolicy)
        self.label_intensity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_intensity.setObjectName("label_intensity")
        self.gridLayout_displaycontrol.addWidget(self.label_intensity, 2, 3, 1, 1)
        self.horizontalLayout_processtimer = QtWidgets.QHBoxLayout()
        self.horizontalLayout_processtimer.setObjectName("horizontalLayout_processtimer")
        self.label_processtimer = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_processtimer.setObjectName("label_processtimer")
        self.horizontalLayout_processtimer.addWidget(self.label_processtimer)
        self.progressBar_processtimer = QtWidgets.QProgressBar(self.gridLayoutWidget_3)
        self.progressBar_processtimer.setProperty("value", 0)
        self.progressBar_processtimer.setObjectName("progressBar_processtimer")
        self.horizontalLayout_processtimer.addWidget(self.progressBar_processtimer)
        self.gridLayout_displaycontrol.addLayout(self.horizontalLayout_processtimer, 1, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_proccess = QtWidgets.QMenu(self.menubar)
        self.menu_proccess.setObjectName("menu_proccess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.list_openfile = QtWidgets.QAction(MainWindow)
        self.list_openfile.setObjectName("list_openfile")
        self.list_inputpara = QtWidgets.QAction(MainWindow)
        self.list_inputpara.setObjectName("list_inputpara")
        self.list_outputpara = QtWidgets.QAction(MainWindow)
        self.list_outputpara.setObjectName("list_outputpara")
        self.list_runtest = QtWidgets.QAction(MainWindow)
        self.list_runtest.setObjectName("list_runtest")
        self.list_run = QtWidgets.QAction(MainWindow)
        self.list_run.setObjectName("list_run")
        self.list_runoutputpictest = QtWidgets.QAction(MainWindow)
        self.list_runoutputpictest.setObjectName("list_runoutputpictest")
        self.list_runoutputpic = QtWidgets.QAction(MainWindow)
        self.list_runoutputpic.setObjectName("list_runoutputpic")
        self.menu_file.addAction(self.list_openfile)
        self.menu_file.addAction(self.list_inputpara)
        self.menu_file.addAction(self.list_outputpara)
        self.menu_proccess.addAction(self.list_runtest)
        self.menu_proccess.addAction(self.list_run)
        self.menu_proccess.addAction(self.list_runoutputpictest)
        self.menu_proccess.addAction(self.list_runoutputpic)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_proccess.menuAction())

        self.retranslateUi(MainWindow)
        self.check_preview.toggled['bool'].connect(self.graphicsview_intergratepic.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
        MainWindow.setTabOrder(self.lineedit_outerradius, self.lineedit_savefilename)
        MainWindow.setTabOrder(self.lineedit_savefilename, self.check_color)
        MainWindow.setTabOrder(self.check_color, self.check_scale)
        MainWindow.setTabOrder(self.check_scale, self.check_preview)
        MainWindow.setTabOrder(self.check_preview, self.graphicsview_intergratepic)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sample2detector.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器距离（毫米）</span></p><p><span style=\" font-weight:600;\">(Sample to Detector)</span></p></body></html>"))
        self.label_wavelength.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束波长(埃)</span></p><p><span style=\" font-weight:600;\">(WaveLength)</span></p></body></html>"))
        self.label_detectortiltrotation.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器倾斜方向(度)</span></p><p><span style=\" font-weight:600;\">(Detector tilt rotation)</span></p></body></html>"))
        self.label_beamcenterx.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束中心 X</span></p><p><span style=\" font-weight:600;\">(Beam Center X)</span></p></body></html>"))
        self.label_beamcentery.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">光束中心 Y</span></p><p><span style=\" font-weight:600;\">(Beam Center Y)</span></p></body></html>"))
        self.label_detectortiltangle.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">探测器倾斜角度(度)</span></p><p><span style=\" font-weight:600;\">(Detector tilt angle)</span></p></body></html>"))
        self.label_exppara.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">实验修正参数</span></p></body></html>"))
        self.lineedit_firstazimuthangle.setText(_translate("MainWindow", "0"))
        self.label_outerradius.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分终止半径(像素)</span></p><p><span style=\" font-weight:600;\">(Outer radius)</span></p></body></html>"))
        self.label_savefilename.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">保存文件夹名称</span></p><p><span style=\" font-weight:600;\">(Save in folder)</span></p></body></html>"))
        self.label_firstazimuthangle.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分初始角度(度)</span></p><p><span style=\" font-weight:600;\">First azimuth angle)</span></p></body></html>"))
        self.label_lastazimuthangle.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分终止角度(度)</span></p><p><span style=\" font-weight:600;\">Last azimuth angle)</span></p></body></html>"))
        self.lineedit_savefilename.setText(_translate("MainWindow", "Ring2Line"))
        self.lineedit_lastazimuthangle.setText(_translate("MainWindow", "360"))
        self.label_innerradius.setText(_translate("MainWindow", "<html><head/><body><p style=\'line-height:50%\'><span style=\" font-weight:600;\">积分起始半径(像素)</span></p><p><span style=\" font-weight:600;\">(Inner radius)</span></p></body></html>"))
        self.label_processpara.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">积分处理参数</span></p></body></html>"))
        self.label_datapath.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">数据文件夹路径</span></p></body></html>"))
        self.check_scale.setText(_translate("MainWindow", "显示标尺"))
        self.check_preview.setText(_translate("MainWindow", "显示预览"))
        self.check_color.setText(_translate("MainWindow", "彩色模式"))
        self.label_intensity.setText(_translate("MainWindow", "显示调节"))
        self.label_processtimer.setText(_translate("MainWindow", "出图进度"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_proccess.setTitle(_translate("MainWindow", "处理"))
        self.list_openfile.setText(_translate("MainWindow", "打开数据文件夹"))
        self.list_inputpara.setText(_translate("MainWindow", "导入处理参数"))
        self.list_outputpara.setText(_translate("MainWindow", "导出处理参数"))
        self.list_runtest.setText(_translate("MainWindow", "单张积分测试"))
        self.list_run.setText(_translate("MainWindow", "批量处理积分"))
        self.list_runoutputpictest.setText(_translate("MainWindow", "测试出图"))
        self.list_runoutputpic.setText(_translate("MainWindow", "批量出图"))
