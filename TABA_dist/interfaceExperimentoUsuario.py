# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceExperimentoUsuario.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindowExperimento(object):
    def setupUi(self, MainWindowExperimento):
        MainWindowExperimento.setObjectName(_fromUtf8("MainWindowExperimento"))
        MainWindowExperimento.setWindowModality(QtCore.Qt.WindowModal)
        MainWindowExperimento.resize(900, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        MainWindowExperimento.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/beagle3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowExperimento.setWindowIcon(icon)
        MainWindowExperimento.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(MainWindowExperimento)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 0, 811, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.toolButton_iniciar = QtGui.QToolButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(52)
        sizePolicy.setVerticalStretch(65)
        sizePolicy.setHeightForWidth(self.toolButton_iniciar.sizePolicy().hasHeightForWidth())
        self.toolButton_iniciar.setSizePolicy(sizePolicy)
        self.toolButton_iniciar.setMinimumSize(QtCore.QSize(52, 65))
        self.toolButton_iniciar.setMaximumSize(QtCore.QSize(80, 65))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.toolButton_iniciar.setFont(font)
        self.toolButton_iniciar.setAccessibleDescription(_fromUtf8(""))
        self.toolButton_iniciar.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/iniciar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_iniciar.setIcon(icon1)
        self.toolButton_iniciar.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_iniciar.setAutoRepeatDelay(300)
        self.toolButton_iniciar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_iniciar.setAutoRaise(False)
        self.toolButton_iniciar.setObjectName(_fromUtf8("toolButton_iniciar"))
        self.horizontalLayout_2.addWidget(self.toolButton_iniciar)
        self.toolButton_exit = QtGui.QToolButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(52)
        sizePolicy.setVerticalStretch(65)
        sizePolicy.setHeightForWidth(self.toolButton_exit.sizePolicy().hasHeightForWidth())
        self.toolButton_exit.setSizePolicy(sizePolicy)
        self.toolButton_exit.setMinimumSize(QtCore.QSize(52, 65))
        self.toolButton_exit.setMaximumSize(QtCore.QSize(80, 65))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.toolButton_exit.setFont(font)
        self.toolButton_exit.setAccessibleDescription(_fromUtf8(""))
        self.toolButton_exit.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_exit.setIcon(icon2)
        self.toolButton_exit.setIconSize(QtCore.QSize(35, 35))
        self.toolButton_exit.setAutoRepeatDelay(300)
        self.toolButton_exit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_exit.setAutoRaise(False)
        self.toolButton_exit.setObjectName(_fromUtf8("toolButton_exit"))
        self.horizontalLayout_2.addWidget(self.toolButton_exit)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 70, 900, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtGui.QFrame.Raised)
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(15, 170, 870, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_editPdb = QtGui.QLabel(self.frame)
        self.label_editPdb.setGeometry(QtCore.QRect(20, 11, 285, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_editPdb.sizePolicy().hasHeightForWidth())
        self.label_editPdb.setSizePolicy(sizePolicy)
        self.label_editPdb.setMinimumSize(QtCore.QSize(285, 0))
        self.label_editPdb.setMaximumSize(QtCore.QSize(250, 40))
        self.label_editPdb.setBaseSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_editPdb.setFont(font)
        self.label_editPdb.setObjectName(_fromUtf8("label_editPdb"))
        self.lineEdit_estrutura = QtGui.QLineEdit(self.frame)
        self.lineEdit_estrutura.setGeometry(QtCore.QRect(89, 33, 281, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit_estrutura.setFont(font)
        self.lineEdit_estrutura.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_estrutura.setObjectName(_fromUtf8("lineEdit_estrutura"))
        self.label_editPdb_2 = QtGui.QLabel(self.frame)
        self.label_editPdb_2.setGeometry(QtCore.QRect(400, 11, 61, 20))
        self.label_editPdb_2.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_editPdb_2.setFont(font)
        self.label_editPdb_2.setObjectName(_fromUtf8("label_editPdb_2"))
        self.lineEdit_Ligante = QtGui.QLineEdit(self.frame)
        self.lineEdit_Ligante.setGeometry(QtCore.QRect(400, 33, 81, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit_Ligante.setFont(font)
        self.lineEdit_Ligante.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_Ligante.setObjectName(_fromUtf8("lineEdit_Ligante"))
        self.toolButton_escolhe = QtGui.QToolButton(self.frame)
        self.toolButton_escolhe.setGeometry(QtCore.QRect(20, 33, 52, 52))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(52)
        sizePolicy.setVerticalStretch(52)
        sizePolicy.setHeightForWidth(self.toolButton_escolhe.sizePolicy().hasHeightForWidth())
        self.toolButton_escolhe.setSizePolicy(sizePolicy)
        self.toolButton_escolhe.setMinimumSize(QtCore.QSize(52, 52))
        self.toolButton_escolhe.setMaximumSize(QtCore.QSize(52, 52))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.toolButton_escolhe.setFont(font)
        self.toolButton_escolhe.setAccessibleDescription(_fromUtf8(""))
        self.toolButton_escolhe.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_escolhe.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/pasta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_escolhe.setIcon(icon3)
        self.toolButton_escolhe.setIconSize(QtCore.QSize(28, 28))
        self.toolButton_escolhe.setAutoRepeatDelay(300)
        self.toolButton_escolhe.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_escolhe.setAutoRaise(False)
        self.toolButton_escolhe.setObjectName(_fromUtf8("toolButton_escolhe"))
        self.listView_modelo = QtGui.QListView(self.frame)
        self.listView_modelo.setGeometry(QtCore.QRect(570, 30, 290, 111))
        self.listView_modelo.setObjectName(_fromUtf8("listView_modelo"))
        self.label_coef_4 = QtGui.QLabel(self.frame)
        self.label_coef_4.setGeometry(QtCore.QRect(570, 14, 290, 17))
        self.label_coef_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_coef_4.setFont(font)
        self.label_coef_4.setStyleSheet(_fromUtf8("background-color: rgb(193, 193, 193);"))
        self.label_coef_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_coef_4.setIndent(3)
        self.label_coef_4.setObjectName(_fromUtf8("label_coef_4"))
        self.checkBox_aceitaNomeLongo = QtGui.QCheckBox(self.frame)
        self.checkBox_aceitaNomeLongo.setGeometry(QtCore.QRect(91, 60, 171, 23))
        self.checkBox_aceitaNomeLongo.setObjectName(_fromUtf8("checkBox_aceitaNomeLongo"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 90, 551, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(27, 107, 11);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 38, 17, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(27, 107, 11);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(15, 90, 870, 74))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_10 = QtGui.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(450, 6, 61, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_afinidade = QtGui.QLabel(self.frame_3)
        self.label_afinidade.setGeometry(QtCore.QRect(448, 48, 71, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_afinidade.setFont(font)
        self.label_afinidade.setObjectName(_fromUtf8("label_afinidade"))
        self.label_quantia = QtGui.QLabel(self.frame_3)
        self.label_quantia.setGeometry(QtCore.QRect(550, 48, 71, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_quantia.setFont(font)
        self.label_quantia.setObjectName(_fromUtf8("label_quantia"))
        self.label_system = QtGui.QLabel(self.frame_3)
        self.label_system.setGeometry(QtCore.QRect(20, 48, 321, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_system.setFont(font)
        self.label_system.setObjectName(_fromUtf8("label_system"))
        self.label_tipoMedia = QtGui.QLabel(self.frame_3)
        self.label_tipoMedia.setGeometry(QtCore.QRect(350, 48, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_tipoMedia.setFont(font)
        self.label_tipoMedia.setObjectName(_fromUtf8("label_tipoMedia"))
        self.label_outliers = QtGui.QLabel(self.frame_3)
        self.label_outliers.setGeometry(QtCore.QRect(800, 48, 50, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label_outliers.setFont(font)
        self.label_outliers.setStyleSheet(_fromUtf8(""))
        self.label_outliers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_outliers.setWordWrap(True)
        self.label_outliers.setObjectName(_fromUtf8("label_outliers"))
        self.label_estruturaInicial = QtGui.QLabel(self.frame_3)
        self.label_estruturaInicial.setGeometry(QtCore.QRect(660, 48, 61, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_estruturaInicial.setFont(font)
        self.label_estruturaInicial.setStyleSheet(_fromUtf8(""))
        self.label_estruturaInicial.setObjectName(_fromUtf8("label_estruturaInicial"))
        self.label_11 = QtGui.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 6, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(350, 6, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(448, 6, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(550, 6, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(660, 6, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(799, 6, 71, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(15, 328, 870, 176))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_log = QtGui.QLabel(self.frame_2)
        self.label_log.setGeometry(QtCore.QRect(10, 14, 180, 60))
        self.label_log.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_log.setFont(font)
        self.label_log.setStyleSheet(_fromUtf8("background-color: rgb(193, 193, 193);"))
        self.label_log.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_log.setIndent(3)
        self.label_log.setObjectName(_fromUtf8("label_log"))
        self.label_logTeorico = QtGui.QLabel(self.frame_2)
        self.label_logTeorico.setGeometry(QtCore.QRect(10, 74, 180, 91))
        self.label_logTeorico.setMinimumSize(QtCore.QSize(0, 0))
        self.label_logTeorico.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_logTeorico.setFont(font)
        self.label_logTeorico.setStyleSheet(_fromUtf8("background-color: rgb(252, 236, 142);\n"
"color: rgb(0, 0, 149);"))
        self.label_logTeorico.setIndent(10)
        self.label_logTeorico.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_logTeorico.setObjectName(_fromUtf8("label_logTeorico"))
        self.label_modelo = QtGui.QLabel(self.frame_2)
        self.label_modelo.setGeometry(QtCore.QRect(200, 13, 660, 20))
        self.label_modelo.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_modelo.setFont(font)
        self.label_modelo.setStyleSheet(_fromUtf8("background-color: rgb(193, 193, 193);"))
        self.label_modelo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_modelo.setIndent(3)
        self.label_modelo.setObjectName(_fromUtf8("label_modelo"))
        self.plainTextEdit_modelo = QtGui.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_modelo.setEnabled(True)
        self.plainTextEdit_modelo.setGeometry(QtCore.QRect(200, 30, 660, 135))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit_modelo.setFont(font)
        self.plainTextEdit_modelo.setStyleSheet(_fromUtf8("color: rgb(32, 74, 135);\n"
"font: 11pt \"Ubuntu\";\n"
""))
        self.plainTextEdit_modelo.setReadOnly(True)
        self.plainTextEdit_modelo.setPlainText(_fromUtf8(""))
        self.plainTextEdit_modelo.setObjectName(_fromUtf8("plainTextEdit_modelo"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(15, 510, 870, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.progressBar = QtGui.QProgressBar(self.frame_4)
        self.progressBar.setGeometry(QtCore.QRect(20, 13, 841, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_relogio = QtGui.QLabel(self.centralwidget)
        self.label_relogio.setGeometry(QtCore.QRect(869, 497, 32, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_relogio.setFont(font)
        self.label_relogio.setAutoFillBackground(False)
        self.label_relogio.setText(_fromUtf8(""))
        self.label_relogio.setPixmap(QtGui.QPixmap(_fromUtf8("img/relogio.png")))
        self.label_relogio.setScaledContents(True)
        self.label_relogio.setObjectName(_fromUtf8("label_relogio"))
        self.label_27 = QtGui.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(0, 0, 90, 65))
        self.label_27.setMaximumSize(QtCore.QSize(90, 65))
        self.label_27.setText(_fromUtf8(""))
        self.label_27.setPixmap(QtGui.QPixmap(_fromUtf8("img/TabaComLetras.png")))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.frame_2.raise_()
        self.frame.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.line_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.label_relogio.raise_()
        self.label_27.raise_()
        MainWindowExperimento.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowExperimento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowExperimento.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowExperimento)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowExperimento.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowExperimento)
        QtCore.QObject.connect(self.toolButton_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindowExperimento.sair)
        QtCore.QObject.connect(self.toolButton_iniciar, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindowExperimento.experimentar)
        QtCore.QObject.connect(self.toolButton_escolhe, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindowExperimento.escolheArquivo)
        QtCore.QObject.connect(self.listView_modelo, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), MainWindowExperimento.selecionaModelo)
        QtCore.QObject.connect(self.checkBox_aceitaNomeLongo, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindowExperimento.aceitaNomeLongo)
        QtCore.QMetaObject.connectSlotsByName(MainWindowExperimento)

    def retranslateUi(self, MainWindowExperimento):
        MainWindowExperimento.setWindowTitle(_translate("MainWindowExperimento", "User Experiment", None))
        MainWindowExperimento.setStatusTip(_translate("MainWindowExperimento", "User Experiment", None))
        MainWindowExperimento.setWhatsThis(_translate("MainWindowExperimento", "User Experiment", None))
        MainWindowExperimento.setAccessibleName(_translate("MainWindowExperimento", "experiment", None))
        MainWindowExperimento.setAccessibleDescription(_translate("MainWindowExperimento", "User Experiment", None))
        self.toolButton_iniciar.setToolTip(_translate("MainWindowExperimento", "Start experiment", None))
        self.toolButton_iniciar.setStatusTip(_translate("MainWindowExperimento", "Start experiment", None))
        self.toolButton_iniciar.setWhatsThis(_translate("MainWindowExperimento", "Start experiment", None))
        self.toolButton_iniciar.setAccessibleName(_translate("MainWindowExperimento", "start", None))
        self.toolButton_iniciar.setText(_translate("MainWindowExperimento", "&Start", None))
        self.toolButton_exit.setToolTip(_translate("MainWindowExperimento", "Exit Experiment", None))
        self.toolButton_exit.setStatusTip(_translate("MainWindowExperimento", "Exit Experiment", None))
        self.toolButton_exit.setWhatsThis(_translate("MainWindowExperimento", "Exit", None))
        self.toolButton_exit.setAccessibleName(_translate("MainWindowExperimento", "Save", None))
        self.toolButton_exit.setText(_translate("MainWindowExperimento", "&Exit", None))
        self.frame.setToolTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.frame.setStatusTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.frame.setWhatsThis(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.label_editPdb.setText(_translate("MainWindowExperimento", "<html><head/><body><p>PDB for Analysis of the Binding Affinity</p></body></html>", None))
        self.lineEdit_estrutura.setToolTip(_translate("MainWindowExperimento", "You can choose a PDB file on your computer or enter a valid PDB name to download (eg. 2A4L)", None))
        self.label_editPdb_2.setText(_translate("MainWindowExperimento", "<html><head/><body><p>Ligand</p></body></html>", None))
        self.lineEdit_Ligante.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>eg. rrc</p></body></html>", None))
        self.toolButton_escolhe.setToolTip(_translate("MainWindowExperimento", "Choose a PDB file on your computer.", None))
        self.toolButton_escolhe.setStatusTip(_translate("MainWindowExperimento", "Choose user\'s PDB file.", None))
        self.toolButton_escolhe.setWhatsThis(_translate("MainWindowExperimento", "Choose user\'s PDB file.", None))
        self.toolButton_escolhe.setAccessibleName(_translate("MainWindowExperimento", "Import user\'s PDB file", None))
        self.toolButton_escolhe.setText(_translate("MainWindowExperimento", "&Choose", None))
        self.listView_modelo.setToolTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.listView_modelo.setStatusTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.listView_modelo.setWhatsThis(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.label_coef_4.setToolTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.label_coef_4.setStatusTip(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.label_coef_4.setWhatsThis(_translate("MainWindowExperimento", "Click on the model to show the description.", None))
        self.label_coef_4.setText(_translate("MainWindowExperimento", "Good Models to Apply", None))
        self.checkBox_aceitaNomeLongo.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>Accepts long, non-standard PDB names.</p><p>Be careful to use this option.</p></body></html>", None))
        self.checkBox_aceitaNomeLongo.setStatusTip(_translate("MainWindowExperimento", "Accepts long names", None))
        self.checkBox_aceitaNomeLongo.setWhatsThis(_translate("MainWindowExperimento", "Accepts long names", None))
        self.checkBox_aceitaNomeLongo.setText(_translate("MainWindowExperimento", "Accepts Long Names", None))
        self.label.setToolTip(_translate("MainWindowExperimento", "You can choose a PDB file on your computer or you can enter a valid pdb name to download (eg 2A4L)", None))
        self.label.setText(_translate("MainWindowExperimento", "* You can choose a PDB file on your computer or enter a valid PDB name to download (eg 2A4L)", None))
        self.label_2.setText(_translate("MainWindowExperimento", "*", None))
        self.label_afinidade.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_quantia.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_system.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_tipoMedia.setToolTip(_translate("MainWindowExperimento", "Average Type", None))
        self.label_tipoMedia.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_outliers.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>If &quot;yes&quot;, the outliers have already been deleted</p></body></html>", None))
        self.label_outliers.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_estruturaInicial.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_11.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value after the outliers are deleted.</p></body></html>", None))
        self.label_11.setText(_translate("MainWindowExperimento", "Protein System Name", None))
        self.label_13.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value after the outliers are deleted.</p></body></html>", None))
        self.label_13.setText(_translate("MainWindowExperimento", "Average Type", None))
        self.label_14.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value after the outliers are deleted.</p></body></html>", None))
        self.label_14.setText(_translate("MainWindowExperimento", "Affinity Type", None))
        self.label_15.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value after the outliers and repeated ligands are deleted.</p></body></html>", None))
        self.label_15.setText(_translate("MainWindowExperimento", "Number of Structures", None))
        self.label_16.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value before the outliers and repeated ligands are deleted.</p></body></html>", None))
        self.label_16.setText(_translate("MainWindowExperimento", "Initial Number Structures", None))
        self.label_17.setToolTip(_translate("MainWindowExperimento", "<html><head/><body><p>This is the value after the outliers are deleted.</p></body></html>", None))
        self.label_17.setText(_translate("MainWindowExperimento", "Deleted Outliers", None))
        self.label_log.setText(_translate("MainWindowExperimento", "The theoretical log (nM)", None))
        self.label_logTeorico.setText(_translate("MainWindowExperimento", "TextLabel", None))
        self.label_modelo.setText(_translate("MainWindowExperimento", "Model", None))
        self.label_relogio.setToolTip(_translate("MainWindowExperimento", "Operation in progress. Wait please !", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindowExperimento = QtGui.QMainWindow()
    ui = Ui_MainWindowExperimento()
    ui.setupUi(MainWindowExperimento)
    MainWindowExperimento.show()
    sys.exit(app.exec_())

