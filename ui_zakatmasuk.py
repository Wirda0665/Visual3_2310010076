# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zakatmasuk.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(718, 583)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 701, 251))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblNoTrans = QLabel(self.formLayoutWidget)
        self.lblNoTrans.setObjectName(u"lblNoTrans")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNoTrans)

        self.editNotrans = QLineEdit(self.formLayoutWidget)
        self.editNotrans.setObjectName(u"editNotrans")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNotrans)

        self.lblKdZakat = QLabel(self.formLayoutWidget)
        self.lblKdZakat.setObjectName(u"lblKdZakat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblKdZakat)

        self.cmbKdZakat = QComboBox(self.formLayoutWidget)
        self.cmbKdZakat.setObjectName(u"cmbKdZakat")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbKdZakat)

        self.lblKdMuzaki = QLabel(self.formLayoutWidget)
        self.lblKdMuzaki.setObjectName(u"lblKdMuzaki")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblKdMuzaki)

        self.cmbKdMuzaki = QComboBox(self.formLayoutWidget)
        self.cmbKdMuzaki.setObjectName(u"cmbKdMuzaki")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbKdMuzaki)

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

        self.lblTglMsk = QLabel(self.formLayoutWidget)
        self.lblTglMsk.setObjectName(u"lblTglMsk")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblTglMsk)

        self.editTglMsk = QDateEdit(self.formLayoutWidget)
        self.editTglMsk.setObjectName(u"editTglMsk")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editTglMsk)

        self.lblNorek = QLabel(self.formLayoutWidget)
        self.lblNorek.setObjectName(u"lblNorek")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblNorek)

        self.editNorek = QLineEdit(self.formLayoutWidget)
        self.editNorek.setObjectName(u"editNorek")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editNorek)

        self.lblBukti = QLabel(self.formLayoutWidget)
        self.lblBukti.setObjectName(u"lblBukti")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblBukti)

        self.editBukti = QLineEdit(self.formLayoutWidget)
        self.editBukti.setObjectName(u"editBukti")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.editBukti)

        self.lblKet = QLabel(self.formLayoutWidget)
        self.lblKet.setObjectName(u"lblKet")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblKet)

        self.txtKet = QLineEdit(self.formLayoutWidget)
        self.txtKet.setObjectName(u"txtKet")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.txtKet)

        self.cmbStatus = QComboBox(self.formLayoutWidget)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.lblidAdmin = QLabel(self.formLayoutWidget)
        self.lblidAdmin.setObjectName(u"lblidAdmin")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.lblidAdmin)

        self.cmbIdAdmin = QComboBox(self.formLayoutWidget)
        self.cmbIdAdmin.setObjectName(u"cmbIdAdmin")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.cmbIdAdmin)

        self.lblStatus = QLabel(self.formLayoutWidget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 270, 211, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(230, 270, 201, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(445, 270, 261, 20))
        self.tblZakatMasuk = QTableWidget(Form)
        if (self.tblZakatMasuk.columnCount() < 11):
            self.tblZakatMasuk.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblZakatMasuk.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tblZakatMasuk.setObjectName(u"tblZakatMasuk")
        self.tblZakatMasuk.setGeometry(QRect(10, 380, 701, 181))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 350, 701, 20))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 300, 691, 18))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 330, 71, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblNoTrans.setText(QCoreApplication.translate("Form", u"NO. TRANSAKSI", None))
        self.lblKdZakat.setText(QCoreApplication.translate("Form", u"KODE ZAKAT", None))
        self.lblKdMuzaki.setText(QCoreApplication.translate("Form", u"KODE MUZAKI", None))
        self.lblJumlah.setText(QCoreApplication.translate("Form", u"JUMLAH", None))
        self.lblBentuk.setText(QCoreApplication.translate("Form", u"BENTUK", None))
        self.cmbBentuk.setItemText(0, QCoreApplication.translate("Form", u"Zakat Fitrah", None))
        self.cmbBentuk.setItemText(1, QCoreApplication.translate("Form", u"Zakat Mal", None))
        self.cmbBentuk.setItemText(2, QCoreApplication.translate("Form", u"Zakat Emas dan Perak", None))
        self.cmbBentuk.setItemText(3, QCoreApplication.translate("Form", u"Zakat Perdagangan", None))
        self.cmbBentuk.setItemText(4, QCoreApplication.translate("Form", u"Zakat Pertanian", None))
        self.cmbBentuk.setItemText(5, QCoreApplication.translate("Form", u"Zakat Peternakan", None))

        self.lblTglMsk.setText(QCoreApplication.translate("Form", u"TANGGAL MASUK", None))
        self.lblNorek.setText(QCoreApplication.translate("Form", u"NO REKENING", None))
        self.lblBukti.setText(QCoreApplication.translate("Form", u"BUKTI", None))
        self.lblKet.setText(QCoreApplication.translate("Form", u"KETERANGAN", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("Form", u"Berhasil", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("Form", u"Di Tolak", None))

        self.lblidAdmin.setText(QCoreApplication.translate("Form", u"ID ADMIN", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"STATUS", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblZakatMasuk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No Transaksi Masuk", None));
        ___qtablewidgetitem1 = self.tblZakatMasuk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Kode Zakat", None));
        ___qtablewidgetitem2 = self.tblZakatMasuk.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Kode Muzaki", None));
        ___qtablewidgetitem3 = self.tblZakatMasuk.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jumlah Masuk", None));
        ___qtablewidgetitem4 = self.tblZakatMasuk.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Bentuk", None));
        ___qtablewidgetitem5 = self.tblZakatMasuk.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None));
        ___qtablewidgetitem6 = self.tblZakatMasuk.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"No Rekening", None));
        ___qtablewidgetitem7 = self.tblZakatMasuk.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Bukti", None));
        ___qtablewidgetitem8 = self.tblZakatMasuk.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem9 = self.tblZakatMasuk.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem10 = self.tblZakatMasuk.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"ID Admin", None));
        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
    # retranslateUi

