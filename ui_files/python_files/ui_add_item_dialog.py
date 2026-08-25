# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_item_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_AddItem(object):
    def setupUi(self, AddItem):
        if not AddItem.objectName():
            AddItem.setObjectName(u"AddItem")
        AddItem.resize(421, 377)
        self.gridLayout_4 = QGridLayout(AddItem)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(AddItem)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(AddItem)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(175, 175))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_item_type = QLabel(self.frame_5)
        self.label_item_type.setObjectName(u"label_item_type")
        self.label_item_type.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_item_type, 0, 1, 1, 1)

        self.label_material = QLabel(self.frame_5)
        self.label_material.setObjectName(u"label_material")

        self.gridLayout.addWidget(self.label_material, 5, 1, 1, 1)

        self.label_quantity = QLabel(self.frame_5)
        self.label_quantity.setObjectName(u"label_quantity")

        self.gridLayout.addWidget(self.label_quantity, 7, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_quantity = QLineEdit(self.frame_6)
        self.lineEdit_quantity.setObjectName(u"lineEdit_quantity")
        self.lineEdit_quantity.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_7.addWidget(self.lineEdit_quantity, 0, 0, 1, 1)

        self.comboBox_quatity_type = QComboBox(self.frame_6)
        self.comboBox_quatity_type.addItem("")
        self.comboBox_quatity_type.addItem("")
        self.comboBox_quatity_type.setObjectName(u"comboBox_quatity_type")

        self.gridLayout_7.addWidget(self.comboBox_quatity_type, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 8, 1, 1, 1)

        self.lineEdit_item_type = QLineEdit(self.frame_5)
        self.lineEdit_item_type.setObjectName(u"lineEdit_item_type")
        self.lineEdit_item_type.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.lineEdit_item_type, 2, 1, 1, 1)

        self.lineEdit_material = QLineEdit(self.frame_5)
        self.lineEdit_material.setObjectName(u"lineEdit_material")
        self.lineEdit_material.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.lineEdit_material, 6, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(AddItem)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_clear = QPushButton(self.frame_3)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.pushButton_clear, 0, 0, 1, 1)

        self.pushButton_add = QPushButton(self.frame_3)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.pushButton_add, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)

        QWidget.setTabOrder(self.lineEdit_item_type, self.lineEdit_material)
        QWidget.setTabOrder(self.lineEdit_material, self.lineEdit_quantity)
        QWidget.setTabOrder(self.lineEdit_quantity, self.comboBox_quatity_type)
        QWidget.setTabOrder(self.comboBox_quatity_type, self.pushButton_add)
        QWidget.setTabOrder(self.pushButton_add, self.pushButton_clear)

        self.retranslateUi(AddItem)

        QMetaObject.connectSlotsByName(AddItem)
    # setupUi

    def retranslateUi(self, AddItem):
        AddItem.setWindowTitle(QCoreApplication.translate("AddItem", u"Add Item", None))
        self.label.setText(QCoreApplication.translate("AddItem", u"Add Item", None))
        self.label_item_type.setText(QCoreApplication.translate("AddItem", u"Item type:", None))
        self.label_material.setText(QCoreApplication.translate("AddItem", u"Material", None))
        self.label_quantity.setText(QCoreApplication.translate("AddItem", u"Quantity:", None))
        self.comboBox_quatity_type.setItemText(0, QCoreApplication.translate("AddItem", u"items", None))
        self.comboBox_quatity_type.setItemText(1, QCoreApplication.translate("AddItem", u"stacks", None))

        self.pushButton_clear.setText(QCoreApplication.translate("AddItem", u"Clear", None))
        self.pushButton_add.setText(QCoreApplication.translate("AddItem", u"Add", None))
    # retranslateUi

