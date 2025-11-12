# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zakat.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(494, 431)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 461, 160))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblZakat = QLabel(self.formLayoutWidget)
        self.lblZakat.setObjectName(u"lblZakat")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblZakat)

        self.editKode = QLineEdit(self.formLayoutWidget)
        self.editKode.setObjectName(u"editKode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editKode)

        self.lblZakat_2 = QLabel(self.formLayoutWidget)
        self.lblZakat_2.setObjectName(u"lblZakat_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblZakat_2)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.lblBentuk = QLabel(self.formLayoutWidget)
        self.lblBentuk.setObjectName(u"lblBentuk")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblBentuk)

        self.cmbBentuk = QComboBox(self.formLayoutWidget)
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.setObjectName(u"cmbBentuk")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbBentuk)

        self.lblSaldo = QLabel(self.formLayoutWidget)
        self.lblSaldo.setObjectName(u"lblSaldo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblSaldo)

        self.editSaldo = QLineEdit(self.formLayoutWidget)
        self.editSaldo.setObjectName(u"editSaldo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editSaldo)

        self.lblKet = QLabel(self.formLayoutWidget)
        self.lblKet.setObjectName(u"lblKet")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblKet)

        self.txtKet = QTextEdit(self.formLayoutWidget)
        self.txtKet.setObjectName(u"txtKet")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtKet)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 180, 141, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(155, 180, 151, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(310, 180, 161, 20))
        self.tblZakat = QTableWidget(Form)
        if (self.tblZakat.columnCount() < 5):
            self.tblZakat.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblZakat.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblZakat.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblZakat.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblZakat.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblZakat.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblZakat.setObjectName(u"tblZakat")
        self.tblZakat.setGeometry(QRect(10, 280, 461, 141))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 250, 461, 20))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 210, 461, 18))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 230, 61, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblZakat.setText(QCoreApplication.translate("Form", u"KODE ZAKAT", None))
        self.lblZakat_2.setText(QCoreApplication.translate("Form", u"NAMA ZAKAT", None))
        self.lblBentuk.setText(QCoreApplication.translate("Form", u"BENTUK", None))
        self.cmbBentuk.setItemText(0, QCoreApplication.translate("Form", u"Zakat Fitrah", None))
        self.cmbBentuk.setItemText(1, QCoreApplication.translate("Form", u"Zakat Mal", None))
        self.cmbBentuk.setItemText(2, QCoreApplication.translate("Form", u"Zakat Emas dan Perak", None))
        self.cmbBentuk.setItemText(3, QCoreApplication.translate("Form", u"Zakat Perdagangan", None))
        self.cmbBentuk.setItemText(4, QCoreApplication.translate("Form", u"Zakat Pertanian", None))
        self.cmbBentuk.setItemText(5, QCoreApplication.translate("Form", u"Zakat Peternakan", None))

        self.lblSaldo.setText(QCoreApplication.translate("Form", u"SALDO", None))
        self.lblKet.setText(QCoreApplication.translate("Form", u"KETERANGAN", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblZakat.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Zakat", None));
        ___qtablewidgetitem1 = self.tblZakat.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Zakat", None));
        ___qtablewidgetitem2 = self.tblZakat.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Bentuk", None));
        ___qtablewidgetitem3 = self.tblZakat.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Saldo", None));
        ___qtablewidgetitem4 = self.tblZakat.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
    # retranslateUi

