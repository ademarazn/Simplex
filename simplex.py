# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.6

__author__ = "Ademar Zório Neto"
__copyright__ = "Copyright 2017"
__credits__ = ["Ademar Zório Neto", "Douglas Louvison Demarqui", "Carlos Felipe Almeida Gonçalo"]
__version__ = "1.0"
__status__ = "Development"

from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.optimize import linprog
from numpy import multiply


class Ui_MainWindow(object):

    def closeEvent(self, event):
        self.msg.setWindowTitle("Sair")
        self.msg.setText("Deseja realmente sair?")
        op = self.msg.exec_()
        if op == QtWidgets.QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()

    def novo(self):
        self.msg.setWindowTitle("Novo")
        self.msg.setText("Deseja realmente realizar um novo cálculo?")
        op = self.msg.exec_()
        if op == QtWidgets.QMessageBox.Ok:
            self.cbObjetivo.setCurrentIndex(0)
            self.txF1.clear()
            self.txF2.clear()
            self.txF3.clear()
            self.txF4.clear()
            self.txR11.clear()
            self.txR12.clear()
            self.txR13.clear()
            self.txR14.clear()
            self.cbS1.setCurrentIndex(0)
            self.txB1.clear()
            self.txR21.clear()
            self.txR22.clear()
            self.txR23.clear()
            self.txR24.clear()
            self.cbS2.setCurrentIndex(0)
            self.txB2.clear()
            self.txR31.clear()
            self.txR32.clear()
            self.txR33.clear()
            self.txR34.clear()
            self.cbS3.setCurrentIndex(0)
            self.txB3.clear()
            self.txResultado.clear()
            self.tabWidget.setCurrentIndex(0)
            self.statusbar.clearMessage()

    def calcular(self):
        try:
            self.txResultado.clear()

            c = [float(str(self.txF1.text()).replace(',', '.')), float(str(self.txF2.text()).replace(',', '.')),
                 float(str(self.txF3.text()).replace(',', '.')), float(str(self.txF4.text()).replace(',', '.'))]
            A = [[float(str(self.txR11.text()).replace(',', '.')), float(str(self.txR12.text()).replace(',', '.')),
                  float(str(self.txR13.text()).replace(',', '.')), float(str(self.txR14.text()).replace(',', '.'))],
                 [float(str(self.txR21.text()).replace(',', '.')), float(str(self.txR22.text()).replace(',', '.')),
                  float(str(self.txR23.text()).replace(',', '.')), float(str(self.txR24.text()).replace(',', '.'))],
                 [float(str(self.txR31.text()).replace(',', '.')), float(str(self.txR32.text()).replace(',', '.')),
                  float(str(self.txR33.text()).replace(',', '.')), float(str(self.txR34.text()).replace(',', '.'))]]
            b = [float(str(self.txB1.text()).replace(',', '.')), float(str(self.txB2.text()).replace(',', '.')),
                 float(str(self.txB3.text()).replace(',', '.'))]
            if self.cbObjetivo.currentIndex() == 0:
                c = multiply(c, -1)
            if self.cbS1.currentIndex() == 1:
                A[0] = multiply(A[0], -1)
                b[0] = multiply(b[0], -1)
            if self.cbS2.currentIndex() == 1:
                A[1] = multiply(A[1], -1)
                b[1] = multiply(b[1], -1)
            if self.cbS3.currentIndex() == 1:
                A[2] = multiply(A[2], -1)
                b[2] = multiply(b[2], -1)
            xi_bounds = (0, None)
            res = linprog(c, A, b, bounds=(xi_bounds), options={"disp": False})
            # print(str(res.fun * 100) + "g de Salada\n")
            # print(res)
            if res.status == 0:
                self.statusbar.showMessage("Modelo solucionado com sucesso.")
                if self.cbObjetivo.currentIndex() == 0:
                    self.txResultado.setText("Solução: " + str(res.fun*-1))
                else:
                    self.txResultado.setText("Solução: "+str(res.fun))
                # coloca o resultado na área de texto
                self.txResultado.append("\nX1 = "+str(res.x[0])+
                                        "\nX2 = "+str(res.x[1])+
                                        "\nX3 = "+str(res.x[2])+
                                        "\nX4 = "+str(res.x[3])+
                                        "\nX5 = "+str(res.slack[0])+
                                        "\nX6 = "+str(res.slack[1])+
                                        "\nX7 = "+str(res.slack[2]))
                self.tabWidget.setCurrentIndex(1)
            elif res.status == 1:
                self.statusbar.showMessage("Falha ao solucionar. Limite de iteração alcançado.")
                self.tabWidget.setCurrentIndex(0)
            elif res.status == 2:
                self.statusbar.showMessage("Falha ao solucionar. O problema parece ser inviável.")
                self.tabWidget.setCurrentIndex(0)
            else:
                self.statusbar.showMessage("Falha ao solucionar. O problema parece ser ilimitado.")
                self.tabWidget.setCurrentIndex(0)
        except ValueError:
            self.statusbar.showMessage("Falha. Preencha todos os campos com apenas números.")
        except Exception as erro:
            self.statusbar.showMessage("Falha: "+str(erro))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(667, 321)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 668, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tabModelo = QtWidgets.QWidget()
        self.tabModelo.setObjectName("tabModelo")
        self.cbObjetivo = QtWidgets.QComboBox(self.tabModelo)
        self.cbObjetivo.setGeometry(QtCore.QRect(370, 10, 71, 21))
        self.cbObjetivo.setAutoFillBackground(False)
        self.cbObjetivo.setObjectName("cbObjetivo")
        self.cbObjetivo.addItem("")
        self.cbObjetivo.addItem("")

        self.txF1 = QtWidgets.QLineEdit(self.tabModelo)
        self.txF1.setGeometry(QtCore.QRect(100, 40, 91, 20))
        self.txF1.setAutoFillBackground(False)
        self.txF1.setObjectName("txF1")
        self.txF2 = QtWidgets.QLineEdit(self.tabModelo)
        self.txF2.setGeometry(QtCore.QRect(230, 40, 91, 20))
        self.txF2.setAutoFillBackground(False)
        self.txF2.setObjectName("txF2")
        self.txF3 = QtWidgets.QLineEdit(self.tabModelo)
        self.txF3.setGeometry(QtCore.QRect(360, 40, 91, 20))
        self.txF3.setAutoFillBackground(False)
        self.txF3.setObjectName("txF3")
        self.txF4 = QtWidgets.QLineEdit(self.tabModelo)
        self.txF4.setGeometry(QtCore.QRect(490, 40, 91, 20))
        self.txF4.setAutoFillBackground(False)
        self.txF4.setObjectName("txF4")

        self.txR11 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR11.setGeometry(QtCore.QRect(10, 100, 91, 20))
        self.txR11.setAutoFillBackground(False)
        self.txR11.setObjectName("txR11")
        self.txR12 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR12.setGeometry(QtCore.QRect(140, 100, 91, 20))
        self.txR12.setAutoFillBackground(False)
        self.txR12.setObjectName("txR12")
        self.txR13 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR13.setGeometry(QtCore.QRect(270, 100, 91, 20))
        self.txR13.setAutoFillBackground(False)
        self.txR13.setObjectName("txR13")
        self.txR14 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR14.setGeometry(QtCore.QRect(400, 100, 91, 20))
        self.txR14.setAutoFillBackground(False)
        self.txR14.setObjectName("txR14")
        self.cbS1 = QtWidgets.QComboBox(self.tabModelo)
        self.cbS1.setGeometry(QtCore.QRect(520, 100, 31, 21))
        self.cbS1.setAutoFillBackground(False)
        self.cbS1.setObjectName("cbS1")
        self.cbS1.addItem("")
        self.cbS1.addItem("")
        self.cbS1.addItem("")
        self.txB1 = QtWidgets.QLineEdit(self.tabModelo)
        self.txB1.setGeometry(QtCore.QRect(560, 100, 91, 20))
        self.txB1.setAutoFillBackground(False)
        self.txB1.setObjectName("txB1")

        self.txR21 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR21.setGeometry(QtCore.QRect(10, 130, 91, 20))
        self.txR21.setAutoFillBackground(False)
        self.txR21.setObjectName("txR21")
        self.txR22 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR22.setGeometry(QtCore.QRect(140, 130, 91, 20))
        self.txR22.setAutoFillBackground(False)
        self.txR22.setObjectName("txR22")
        self.txR23 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR23.setGeometry(QtCore.QRect(270, 130, 91, 20))
        self.txR23.setAutoFillBackground(False)
        self.txR23.setObjectName("txR23")
        self.txR24 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR24.setGeometry(QtCore.QRect(400, 130, 91, 20))
        self.txR24.setAutoFillBackground(False)
        self.txR24.setObjectName("txR24")
        self.cbS2 = QtWidgets.QComboBox(self.tabModelo)
        self.cbS2.setGeometry(QtCore.QRect(520, 130, 31, 21))
        self.cbS2.setAutoFillBackground(False)
        self.cbS2.setObjectName("cbS2")
        self.cbS2.addItem("")
        self.cbS2.addItem("")
        self.cbS2.addItem("")
        self.txB2 = QtWidgets.QLineEdit(self.tabModelo)
        self.txB2.setGeometry(QtCore.QRect(560, 130, 91, 20))
        self.txB2.setAutoFillBackground(False)
        self.txB2.setObjectName("txB2")

        self.txR31 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR31.setGeometry(QtCore.QRect(10, 160, 91, 20))
        self.txR31.setAutoFillBackground(False)
        self.txR31.setObjectName("txR31")
        self.txR32 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR32.setGeometry(QtCore.QRect(140, 160, 91, 20))
        self.txR32.setAutoFillBackground(False)
        self.txR32.setObjectName("txR32")
        self.txR33 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR33.setGeometry(QtCore.QRect(270, 160, 91, 20))
        self.txR33.setAutoFillBackground(False)
        self.txR33.setObjectName("txR33")
        self.txR34 = QtWidgets.QLineEdit(self.tabModelo)
        self.txR34.setGeometry(QtCore.QRect(400, 160, 91, 20))
        self.txR34.setAutoFillBackground(False)
        self.txR34.setObjectName("txR34")
        self.cbS3 = QtWidgets.QComboBox(self.tabModelo)
        self.cbS3.setGeometry(QtCore.QRect(520, 160, 31, 21))
        self.cbS3.setAutoFillBackground(False)
        self.cbS3.setObjectName("cbS3")
        self.cbS3.addItem("")
        self.cbS3.addItem("")
        self.cbS3.addItem("")
        self.txB3 = QtWidgets.QLineEdit(self.tabModelo)
        self.txB3.setGeometry(QtCore.QRect(560, 160, 91, 20))
        self.txB3.setAutoFillBackground(False)
        self.txB3.setObjectName("txB3")


        self.label_20 = QtWidgets.QLabel(self.tabModelo)
        self.label_20.setGeometry(QtCore.QRect(10, 190, 641, 21))
        self.label_20.setAutoFillBackground(False)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_3 = QtWidgets.QLabel(self.tabModelo)
        self.label_3.setGeometry(QtCore.QRect(330, 40, 31, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.label_19 = QtWidgets.QLabel(self.tabModelo)
        self.label_19.setGeometry(QtCore.QRect(10, 70, 641, 21))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label = QtWidgets.QLabel(self.tabModelo)
        self.label.setGeometry(QtCore.QRect(220, 10, 141, 21))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tabModelo)
        self.label_4.setGeometry(QtCore.QRect(460, 40, 31, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.tabModelo)
        self.label_10.setGeometry(QtCore.QRect(500, 100, 21, 21))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabModelo)
        self.label_11.setGeometry(QtCore.QRect(110, 130, 31, 21))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.tabModelo)
        self.label_6.setGeometry(QtCore.QRect(50, 40, 41, 21))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tabModelo)
        self.label_5.setGeometry(QtCore.QRect(590, 40, 21, 21))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.tabModelo)
        self.label_9.setGeometry(QtCore.QRect(240, 100, 31, 21))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.tabModelo)
        self.label_7.setGeometry(QtCore.QRect(370, 100, 31, 21))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.tabModelo)
        self.label_12.setGeometry(QtCore.QRect(240, 130, 31, 21))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.tabModelo)
        self.label_15.setGeometry(QtCore.QRect(110, 160, 31, 21))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.tabModelo)
        self.label_18.setGeometry(QtCore.QRect(500, 160, 21, 21))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.tabModelo)
        self.label_17.setGeometry(QtCore.QRect(370, 160, 31, 21))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.tabModelo)
        self.label_16.setGeometry(QtCore.QRect(240, 160, 31, 21))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(self.tabModelo)
        self.label_13.setGeometry(QtCore.QRect(370, 130, 31, 21))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabModelo)
        self.label_14.setGeometry(QtCore.QRect(500, 130, 21, 21))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setObjectName("label_14")
        self.label_2 = QtWidgets.QLabel(self.tabModelo)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 31, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.tabModelo)
        self.label_8.setGeometry(QtCore.QRect(110, 100, 31, 21))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setObjectName("label_8")

        self.btCalcular = QtWidgets.QPushButton(self.tabModelo)
        self.btCalcular.setGeometry(QtCore.QRect(290, 220, 81, 23))
        self.btCalcular.setObjectName("btCalcular")
        self.tabWidget.addTab(self.tabModelo, "")
        self.tabResultado = QtWidgets.QWidget()
        self.tabResultado.setObjectName("tabResultado")
        self.txResultado = QtWidgets.QTextEdit(self.tabResultado)
        self.txResultado.setGeometry(QtCore.QRect(0, 0, 661, 251))
        self.txResultado.setObjectName("txResultado")
        self.txResultado.setReadOnly(True)
        self.txResultado.setFontPointSize(16)
        self.tabWidget.addTab(self.tabResultado, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo = QtWidgets.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.msg = QtWidgets.QMessageBox(MainWindow)
        self.msg.setIcon(QtWidgets.QMessageBox.Question)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionSair.triggered.connect(lambda : MainWindow.close())
        self.actionNovo.triggered.connect(lambda : self.novo())
        self.btCalcular.clicked.connect(lambda : self.calcular())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplex"))
        self.label_20.setText(_translate("MainWindow", "X1, X2, X3, X4 ≥ 0"))
        self.label_3.setText(_translate("MainWindow", "X2 +"))
        self.label_19.setText(_translate("MainWindow", "Restrições:"))
        self.cbS3.setItemText(0, _translate("MainWindow", "≤"))
        self.cbS3.setItemText(1, _translate("MainWindow", "≥"))
        self.cbS3.setItemText(2, _translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", "Qual é o objetivo da função?"))
        self.label_4.setText(_translate("MainWindow", "X3 +"))
        self.cbS1.setItemText(0, _translate("MainWindow", "≤"))
        self.cbS1.setItemText(1, _translate("MainWindow", "≥"))
        self.cbS1.setItemText(2, _translate("MainWindow", "="))
        self.label_10.setText(_translate("MainWindow", "X4"))
        self.label_11.setText(_translate("MainWindow", "X1 +"))
        self.label_6.setText(_translate("MainWindow", "Função:"))
        self.label_5.setText(_translate("MainWindow", "X4"))
        self.label_9.setText(_translate("MainWindow", "X2 +"))
        self.label_7.setText(_translate("MainWindow", "X3 +"))
        self.cbObjetivo.setItemText(0, _translate("MainWindow", "Maximizar"))
        self.cbObjetivo.setItemText(1, _translate("MainWindow", "Minimizar"))
        self.label_12.setText(_translate("MainWindow", "X2 +"))
        self.label_15.setText(_translate("MainWindow", "X1 +"))
        self.cbS2.setItemText(0, _translate("MainWindow", "≤"))
        self.cbS2.setItemText(1, _translate("MainWindow", "≥"))
        self.cbS2.setItemText(2, _translate("MainWindow", "="))
        self.label_18.setText(_translate("MainWindow", "X4"))
        self.label_17.setText(_translate("MainWindow", "X3 +"))
        self.label_16.setText(_translate("MainWindow", "X2 +"))
        self.label_14.setText(_translate("MainWindow", "X4"))
        self.label_2.setText(_translate("MainWindow", "X1 +"))
        self.label_8.setText(_translate("MainWindow", "X1 +"))
        self.label_13.setText(_translate("MainWindow", "X3 +"))
        self.btCalcular.setText(_translate("MainWindow", "Calcular"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModelo), _translate("MainWindow", "Modelo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResultado), _translate("MainWindow", "Resultado"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionNovo.setText(_translate("MainWindow", "Novo"))
        self.actionNovo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("python.ico"))

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.closeEvent = ui.closeEvent

    MainWindow.show()
    sys.exit(app.exec_())

