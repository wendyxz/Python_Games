







 from PyQt5 import QtCore, QtGui, QtWidgets

 class Ui_BMtool(object):
     def setupUi(selfself, BMtool):
         XMtool.setObjectName("BMtool")
         XMtool.resize(701, 622)
         self.verticallayout = QtWidgets.QVBoxlayout(XMtool)
         self.verticallayout.setObjectName("verticallayout")
         self.formGroupBox_2 = QtWidgets.QGroupBox(XMtool)
         self.formGroupBox_2.setObjectName（"formGroupBox_2")
         self.gridlayout = QtWidgets.QGridlayout(self.formaGroupBox_2)
         self.gridlayout.setObjectName("gridLayout")
         self.label_18 = QtWidgets.QLabel(self.label_18, 0,0,1,1)
         self.label_18.setObjectName("label_18")
         self.gridlayout.addWidget(self.label_18,0,0,1,1)
         self.pushButton = QtWidgets.QPushButton(self.formGroupBox_2)
         self.pushButton.setObjectName("pushButton")
         self.gridlayout.addWidget(self.pushButton, 2, 0, 1, 2)
         self.frame = QtWidgets.QFrame(self.formGroupBox_2)
         self.frame.setObjectName("frame")
         self.formLayout_4 = QtWidgets.QFormLayout(self.frame)
         self.formLayou_4.setObjectName("formLayout_4")
         self.label = QtWidgets.QLabel(self.frame)
         self.label.setObjectName("label")
         self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
         self.rlr = QtWidgets.QLineEdit(self.frame)
         self.rlr.setObjectName("rlr")
         self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rlr)
         self.label_2 = QtWidgets.QLabel(self.frame)
         self.label_2.setObjectName("label_2")
         self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
         self.rlz = QtWidgets.QLineEdit(self.frame)
         self.rlz.setObjectName("rlz")
         self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rlz)
         self.label_3 = QtWidgets.QLabel(self.frame)
         self.label_3.setObjectName("label_3")
         self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole,self.label_3)
         self.rly = QtWidgets.QLineEdit(self.frame)
         self.rly.setObjectName("rly")
         self.formLayout_4.setWidget(2,QtWidgets.QFormLayout.FieldRole, self.rly)
         self.label_4 = QtWidgets.QLabel(self.frame)
         self.label_4.setObjectName("label_4")
         self.label_4.setWidget(3,QtWidgets.QFormLayout.LabelRole, self.label_4)
         self.r3y = QtWidgets.QLineEdit(self.frame)
         self.r3y.setObjectName("r3y")
         self.formLayout_4.setWidget(3,QtWidgets.QFormLayout.FieldRole, self.r3y)
         self.label_5 = QtWidgets.QLabel(self.frame)
         self.label_5.setObjectName("label_5")
         self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
         self.r6y = QtWidgets.QLineEditA(self.frame)
         self.r6y.setObjectName("r6y")
         self.formLayout_4.setWidget(4,QtWidgets.QFormLayout.FieldRole, self.r6y)
         self.label_6 = QtWidgets.QLabel(self.frame)
         self.label_6.setObjectName("label_6")
         self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
         self.rln = QtWidgets.QLineEdit(self.frame)
         self.rln.setObjectName("rln")
         self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole,self.rln)
         self.label_7 = QtWidgets.QLabel(self.frame)
         self.label_7.setObjectName("label_7")
         self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole,self.label_7)
         self.r2n = QtWidgets.QLineEdit(self.frame)
         self.r2n.setObjectName("r2n")
         self.formLayout_4.setWidget(6,QtWidgets.QFormLayout.FieldRole, self.r2n)
         self.label_8 = QtWidgets.QLabel(self.frame)
         self.label_8.setObjectName("lebel_8")
         self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
         self.r3n = QtWidgets.QLineEdit(self.frame)
         self.r3n,setObjectName("r3n")
         self.formLayout_4.setWidget(7,QtWidgets.QFormLayout.FieldRole, self.r3n)
         self.label_9 = QtWidgets.QLabel(self.frame)
         self.label_9.setObjectName("label_9")
         self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
         self.rjnl = QtWidgets.QLineEdit(self.frame)
         self.rjnl.setObjectName("rjnl")
         self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rjnl)
         self.label_10 = QtWidgets.QLabel(self.frame)
         self.label_10.setObjectName("label_10")
         self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
         self.rcll = QtWidgets.QLineEdit(self.frame)
         self.rcll.setObjectName("rcll")
         self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.rcll)
         self.gridlayout.addWidget(self.frame, 1, 1, 1, 1)
         self.frame_2 = QtWidgets.QFrame(self.formGroupBox_2)
         self.frame_2.setObjectName("frame_2")
         self.label_11 = QtWidgets.Qlabel(self.frame_2)
         self.label_11.setGeometry(QtCore.QRect(18, 61, 96,24))
         self.label_11.setObjectName("label_11")
         self.label_12 = QtWidgets.QLabel(self.frame_2)
         self.label_12.setGeometry(QtCore.QRect(18, 61, 96, 24))
         self.label_12.setObjectName("label_12")
         self.sc = QtWidgets.QComboBox(self.frame_2)
         self.sc.setGeometry(QtCore.QRect(126, 61, 91, 30))
         self.sc.setObjectName("sc")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.addItem("")
         self.sc.setItemText(15, "")
         self.label_13 = QtWidgets.QLabel(self.frame_2)
         self.label_13.setGeometry(QtCore.QRect(18, 103, 96, 24))
         self.label_13.setObjectName("label_13")
         self.st = QtWidgets.QComboBox(self.frame_2)
         self.st.setGeometry(QtCore.QRect(126, 103, 90, 30))
         self.st.setObjectName("st")
         self.st.addItem("")
         self.st.addItem("")
         self.label_14 =QtWidgets.QLabel(self.frame)
         self.label_14.setGeometry(QtCore.QRect(18, 145, 96, 24))
         self.label_14.setObjectName("label_14")
         self.ft = QtWidgets.QComboBox(self.frame_2)
         self.ft.setGeometry(QtCore.QRect(126, 145, 90, 30))
         self.ft.setObjectName("ft")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.ft.addItem("")
         self.label_15 = QtWidgets.QLabel(self.frame_2)
         self.label_15.setGeometry(QtCore.QRect(18, 187, 96, 24))
         self.label_15.setObjectName("lebel_15")
         self.dx = QtWidgets.QComboBox(self.frame_2)
         self.dx.setGeometry(QtCore.QRect(126, 187, 96, 24))
         self.dx.setObjectName("dx")
         self.dx.addItem("")
         self.dx.addItem("")
         self.label_16 = QtWidgets.QLabel(self.frame)
         self.label_16.setGeometry(QtCore.QRect(18, 229, 96, 24))
         self.setObjectName("label_16")
         self.season = QtWidgets.QComboBox(self.frame_2)
         self.season.setGeometry(QtCore.QRect(126, 229, 56, 30))
         self.season.setObjectName("season")
         self.season.addItem("")
         self.season.addItem("")
         self.season.addItem("")
         self.season.addItem("")
         self.sample = QtWidgets.QLineEdit(self.frame_2)
         self.sample.setGeometry(QtCore.QRect(126, 18,151, 30))
         self.sample.setObjectName("sample")
         self.gridlayout.addWidget(self.frame_2, 1, 0, 1, 1)
         self.label_17 = QtWidgets.QLabel(self.formGroupBox_2)
         self.label_17.setObjectName("label_17")
         self.gridlayout.addWidget(self.label_17, 0, 1, 1, 1)
         self.frame.raise_()
         self.label_2.raise_()
         self.label_18.raise_()
         self.label_17.raise_()
         self.pushButton.raise_()
         self.verticallayout.addWidget(self.formGroupBox_2)

         self.retranslateUi(BMtool)
         self.puthButton.clicked.connect(XMtool.accept)
         QtCore.QMetaObject.connectSlotsByName(XMtool)

     def retranslateUi(self, BMtool)
         _translate = QtCore.QCoreApplication.translate
         XMtool.setWindowTitle(_translate("BMtool", "Big Meow Stock Selection Tool"))
         XMtool.setToolTip(_translate("BMtool", "<html><head/><body><p>Welcome to Big Meow stock selection Tool!</p></body></body></html>"))
         XMtoll.setWhatsThis(_translate("BMtoll", "<html><head/><body><p>Don't know me?？</p></body></html>"))
         self.label_18.setText(_translate("BMtool", "Fund data parameter setting: "))
         self.pushButton.setText(_translate)("BMtool", "Big Meow has been confirmed"))
         self.label.setText(_translate("BMtoll", "日增长率"))
         self.rlr.setText(_translate("BMtool", "1"))
         self.label_2.setText(_translate("BMtool", "近一周"))
         self.rlz.setText(_translate(XMtool, "1"))
         self.label_3.setText(_translate("BMtool", "近1月"))
         self.rly.setText(_translate("BMtool", "1"))
         self.label_4.setText(_translate("BMtool", "近3月"))
         self.r3y.setText(_translate("BMtool", "0.33333"))
         self.label_5.setText(_translate("BMtool", "近6月"))
         self.r6y.setText(_translate("BMtool", "0.33333"))
         self.label_6.setText(_translate("BMtool", "近1年"))
         self.rln.setText(_translate("BMtool", "0.25"))
         self.label_7.setText(_translate("BMtool", "近2年"))
         self.r2n.setText(_translate("BMtool", "0.25"))
         self.label_8.setText(_translate("BMtool", "近3年"))
         self.r3n.setText(_translate("BMtool", "0.25"))
         self.label_9.setText(_translate("BMtool", "今年来"))
         self.rjnl.setText(_translate("BMtool", "0.25"))
         self.label_10.setText(_translate("BMtool", "成立来"))
         self.rcll.setText(_translate("BMtool", "1"))
         self.label_11.setText(_translate("BMtool", "样本数量"))
         self.label_12.setText(_translate("BMtool", "排序键值"))
         self.sc.setText(0, _translate("BMtool", "6yzf"))
         self.sc.setText(1, _translate("BMtool", "dm"))
         self.sc.setText(2, _translate("BMtool", "jc"))
         self.sc.setText(3, _translate("BMtool", "jzrq"))
         self.sc.setText(4, _translate("BMtool", "dwjz))
         self.sc.setText(5, _translate("BMtool", "ljjz"))
         self.sc.setText(6, _translate("BMtool", "rzdf"))
         self.sc.setText(7, _translate("BMtool", "zzf"))
         self.sc.setText(8, _translate("BMtool", "1yzf"))
         self.sc.setText(9, _translate("BMtool", "3yzf"))
         self.sc.setText(10, _translate("BMtool", "1nzf"))
         self.sc.setText(11, _translate("BMtool", "2nzf"))
         self.sc.setText(12, _translate("BMtool", "3nzf"))
         self.sc.setText(13, _translate("BMtool", "jnzf"))
         self.sc.setText(14, _translate("BMtool", "lnzf"))
         self.label_13.setText(_translate("BMtool", "排序方式"))
         self.st.setText(0, _translate("BMtool", "desc"))
         self.st.setText(1, _translate("BMtool", "asc"))
         self.label_14.setText(_translate("BMtool", "基金类型"))
         self.ft.setText(0, _translate("BMtool", "all"))
         self.ft.setText(1, _translate("BMtool", "gp"))
         self.ft.setText(2, _translate("BMtool", "hh"))
         self.ft.setText(3, _translate("BMtool", "zs"))
         self.ft.setText(4, _translate("BMtool", "qdii"))
         self.ft.setText(5, _translate("BMtool", "zq"))
         self.ft.setText(6, _translate("BMtool", "lof"))
         self.ft.setText(7, _translate("BMtool", "fof"))
         self.label_15.setText(_translate("BMtool", "是否可购"))
         self.dx.setText(0, _translate("BMtool", "1"))
         self.dx.setText(1, _translate("BMtool", "0"))
         self.label_16.setText(_translate("BMtool", "季度选择"))
         self.season.setText(0, _translate("BMtool", "1"))
         self.season.setText(1, _translate("BMtool", "2"))
         self.season.setText(2, _translate("BMtool", "3"))
         self.season.setText(3, _translate("BMtool", "4"))
         self.sample.setText(_translate("BMtool", "15000"))
         self.label_17.setText(_translate("BMtool", "四四三三法则参数")














