# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bayar.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 266)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 381, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblKode = QLabel(self.formLayoutWidget)
        self.lblKode.setObjectName(u"lblKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblKode)

        self.editKode = QLineEdit(self.formLayoutWidget)
        self.editKode.setObjectName(u"editKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKode)

        self.lblNama = QLabel(self.formLayoutWidget)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.lblHarga = QLabel(self.formLayoutWidget)
        self.lblHarga.setObjectName(u"lblHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblHarga)

        self.editHarga = QLineEdit(self.formLayoutWidget)
        self.editHarga.setObjectName(u"editHarga")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editHarga)

        self.lblJumlah = QLabel(self.formLayoutWidget)
        self.lblJumlah.setObjectName(u"lblJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblJumlah)

        self.editJumlah = QLineEdit(self.formLayoutWidget)
        self.editJumlah.setObjectName(u"editJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editJumlah)

        self.lblTotal = QLabel(self.formLayoutWidget)
        self.lblTotal.setObjectName(u"lblTotal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblTotal)

        self.editTotal = QLineEdit(self.formLayoutWidget)
        self.editTotal.setObjectName(u"editTotal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTotal)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 140, 191, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(205, 140, 181, 20))
        self.tblBayar = QTableWidget(Form)
        if (self.tblBayar.columnCount() < 5):
            self.tblBayar.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblBayar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblBayar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblBayar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblBayar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblBayar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblBayar.setObjectName(u"tblBayar")
        self.tblBayar.setGeometry(QRect(10, 170, 381, 81))
        self.tblBayar.setColumnCount(5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblKode.setText(QCoreApplication.translate("Form", u"Kode", None))
        self.lblNama.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.lblHarga.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.lblJumlah.setText(QCoreApplication.translate("Form", u"Jumlah", None))
        self.lblTotal.setText(QCoreApplication.translate("Form", u"Total", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tblBayar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode", None));
        ___qtablewidgetitem1 = self.tblBayar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Barang", None));
        ___qtablewidgetitem2 = self.tblBayar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Harga", None));
        ___qtablewidgetitem3 = self.tblBayar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jumlah", None));
        ___qtablewidgetitem4 = self.tblBayar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Total", None));
    # retranslateUi

