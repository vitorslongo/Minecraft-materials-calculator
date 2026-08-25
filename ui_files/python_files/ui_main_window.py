# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 744)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 75))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_project_title = QLabel(self.frame_8)
        self.label_project_title.setObjectName(u"label_project_title")
        self.label_project_title.setMaximumSize(QSize(16777215, 180))

        self.gridLayout.addWidget(self.label_project_title, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.frame_10)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_3, 0, 0, 1, 1)

        self.tableWidget_calculator = QTableWidget(self.frame)
        if (self.tableWidget_calculator.columnCount() < 5):
            self.tableWidget_calculator.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_calculator.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_calculator.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_calculator.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_calculator.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_calculator.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_calculator.setObjectName(u"tableWidget_calculator")

        self.gridLayout_8.addWidget(self.tableWidget_calculator, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_delete = QPushButton(self.frame_2)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.gridLayout_6.addWidget(self.pushButton_delete, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.pushButton_reset = QPushButton(self.frame_2)
        self.pushButton_reset.setObjectName(u"pushButton_reset")

        self.gridLayout_6.addWidget(self.pushButton_reset, 0, 0, 1, 1)

        self.pushButton_add = QPushButton(self.frame_2)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout_6.addWidget(self.pushButton_add, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.pushButton_add_batch = QPushButton(self.frame_2)
        self.pushButton_add_batch.setObjectName(u"pushButton_add_batch")

        self.gridLayout_6.addWidget(self.pushButton_add_batch, 0, 5, 1, 1)


        self.gridLayout_8.addWidget(self.frame_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_10)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 75))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_7, 0, 0, 1, 1)

        self.tableWidget_results = QTableWidget(self.frame_4)
        if (self.tableWidget_results.columnCount() < 2):
            self.tableWidget_results.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tableWidget_results.setObjectName(u"tableWidget_results")
        self.tableWidget_results.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.tableWidget_results, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 75))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_open_project = QPushButton(self.frame_9)
        self.pushButton_open_project.setObjectName(u"pushButton_open_project")

        self.gridLayout_3.addWidget(self.pushButton_open_project, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.pushButton_close = QPushButton(self.frame_9)
        self.pushButton_close.setObjectName(u"pushButton_close")

        self.gridLayout_3.addWidget(self.pushButton_close, 0, 0, 1, 1)

        self.pushButton_export_project = QPushButton(self.frame_9)
        self.pushButton_export_project.setObjectName(u"pushButton_export_project")

        self.gridLayout_3.addWidget(self.pushButton_export_project, 0, 3, 1, 1)

        self.pushButton_save_project = QPushButton(self.frame_9)
        self.pushButton_save_project.setObjectName(u"pushButton_save_project")

        self.gridLayout_3.addWidget(self.pushButton_save_project, 0, 5, 1, 1)


        self.gridLayout_2.addWidget(self.frame_9, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 991, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_project_title.setText(QCoreApplication.translate("MainWindow", u"Project Title", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Item Requirements", None))
        ___qtablewidgetitem = self.tableWidget_calculator.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Number of items", None))
        ___qtablewidgetitem1 = self.tableWidget_calculator.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Stacks", None))
        ___qtablewidgetitem2 = self.tableWidget_calculator.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        ___qtablewidgetitem3 = self.tableWidget_calculator.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Base item", None))
        ___qtablewidgetitem4 = self.tableWidget_calculator.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Number of base items", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_add_batch.setText(QCoreApplication.translate("MainWindow", u"Add batch", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        ___qtablewidgetitem5 = self.tableWidget_results.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Stacks", None))
        ___qtablewidgetitem6 = self.tableWidget_results.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total base items", None))
        self.pushButton_open_project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_export_project.setText(QCoreApplication.translate("MainWindow", u"Export project", None))
        self.pushButton_save_project.setText(QCoreApplication.translate("MainWindow", u"Save project", None))
    # retranslateUi
