# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zakatkeluar.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(622, 499)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 601, 231))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTrans = QLabel(self.formLayoutWidget)
        self.lblTrans.setObjectName(u"lblTrans")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTrans)

        self.editTrans = QLineEdit(self.formLayoutWidget)
        self.editTrans.setObjectName(u"editTrans")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editTrans)

        self.lblKdZakat = QLabel(self.formLayoutWidget)
        self.lblKdZakat.setObjectName(u"lblKdZakat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblKdZakat)

        self.lblKdMuztahik = QLabel(self.formLayoutWidget)
        self.lblKdMuztahik.setObjectName(u"lblKdMuztahik")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKdMuztahik)

        self.lblJumlah = QLabel(self.formLayoutWidget)
        self.lblJumlah.setObjectName(u"lblJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblJumlah)

        self.editJumlah = QLineEdit(self.formLayoutWidget)
        self.editJumlah.setObjectName(u"editJumlah")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editJumlah)

        self.lblBentuk = QLabel(self.formLayoutWidget)
        self.lblBentuk.setObjectName(u"lblBentuk")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblBentuk)

        self.cmbBentuk = QComboBox(self.formLayoutWidget)
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.addItem("")
        self.cmbBentuk.setObjectName(u"cmbBentuk")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmbBentuk)

        self.lblTglKel = QLabel(self.formLayoutWidget)
        self.lblTglKel.setObjectName(u"lblTglKel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblTglKel)

        self.editTglKel = QDateEdit(self.formLayoutWidget)
        self.editTglKel.setObjectName(u"editTglKel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editTglKel)

        self.lblIdAdmin = QLabel(self.formLayoutWidget)
        self.lblIdAdmin.setObjectName(u"lblIdAdmin")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblIdAdmin)

        self.lblKet = QLabel(self.formLayoutWidget)
        self.lblKet.setObjectName(u"lblKet")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblKet)

        self.txtKet = QTextEdit(self.formLayoutWidget)
        self.txtKet.setObjectName(u"txtKet")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.txtKet)

        self.cmbKdZakat = QComboBox(self.formLayoutWidget)
        self.cmbKdZakat.setObjectName(u"cmbKdZakat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbKdZakat)

        self.cmbKdMustahik = QComboBox(self.formLayoutWidget)
        self.cmbKdMustahik.setObjectName(u"cmbKdMustahik")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbKdMustahik)

        self.cmbIdAdmin = QComboBox(self.formLayoutWidget)
        self.cmbIdAdmin.setObjectName(u"cmbIdAdmin")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbIdAdmin)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 250, 191, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(215, 250, 201, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(425, 250, 181, 20))
        self.tblZakatKeluar = QTableWidget(Form)
        if (self.tblZakatKeluar.columnCount() < 8):
            self.tblZakatKeluar.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblZakatKeluar.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblZakatKeluar.setObjectName(u"tblZakatKeluar")
        self.tblZakatKeluar.setGeometry(QRect(10, 350, 601, 141))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 320, 601, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 300, 61, 16))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 280, 591, 18))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblTrans.setText(QCoreApplication.translate("Form", u"NO TRANSAKSI", None))
        self.lblKdZakat.setText(QCoreApplication.translate("Form", u"KODE ZAKAT", None))
        self.lblKdMuztahik.setText(QCoreApplication.translate("Form", u"KODE MUSTAHIK", None))
        self.lblJumlah.setText(QCoreApplication.translate("Form", u"JUMLAH", None))
        self.lblBentuk.setText(QCoreApplication.translate("Form", u"BENTUK", None))
        self.cmbBentuk.setItemText(0, QCoreApplication.translate("Form", u"Zakat Fitrah", None))
        self.cmbBentuk.setItemText(1, QCoreApplication.translate("Form", u"Zakat Mal", None))
        self.cmbBentuk.setItemText(2, QCoreApplication.translate("Form", u"Zakat Emas dan Perak", None))
        self.cmbBentuk.setItemText(3, QCoreApplication.translate("Form", u"Zakat Perdagangan", None))
        self.cmbBentuk.setItemText(4, QCoreApplication.translate("Form", u"Zakat Pertanian", None))
        self.cmbBentuk.setItemText(5, QCoreApplication.translate("Form", u"Zakat Peternakan", None))

        self.lblTglKel.setText(QCoreApplication.translate("Form", u"TANGGAL KELUAR", None))
        self.lblIdAdmin.setText(QCoreApplication.translate("Form", u"ID ADMIN", None))
        self.lblKet.setText(QCoreApplication.translate("Form", u"KETERANGAN", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblZakatKeluar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Zakat", None));
        ___qtablewidgetitem1 = self.tblZakatKeluar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Kode Mustahik", None));
        ___qtablewidgetitem2 = self.tblZakatKeluar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"No Transaksi", None));
        ___qtablewidgetitem3 = self.tblZakatKeluar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jumlah", None));
        ___qtablewidgetitem4 = self.tblZakatKeluar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Bentuk", None));
        ___qtablewidgetitem5 = self.tblZakatKeluar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None));
        ___qtablewidgetitem6 = self.tblZakatKeluar.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"ID Admin", None));
        ___qtablewidgetitem7 = self.tblZakatKeluar.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
    # retranslateUi

