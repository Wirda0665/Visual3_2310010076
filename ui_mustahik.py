# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mustahik.ui'
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
        Form.resize(696, 561)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 681, 251))
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

        self.lblNik = QLabel(self.formLayoutWidget)
        self.lblNik.setObjectName(u"lblNik")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblNik)

        self.editNik = QLineEdit(self.formLayoutWidget)
        self.editNik.setObjectName(u"editNik")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNik)

        self.lblTempat = QLabel(self.formLayoutWidget)
        self.lblTempat.setObjectName(u"lblTempat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTempat)

        self.editTempat = QLineEdit(self.formLayoutWidget)
        self.editTempat.setObjectName(u"editTempat")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTempat)

        self.lblTgl = QLabel(self.formLayoutWidget)
        self.lblTgl.setObjectName(u"lblTgl")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblTgl)

        self.dateTgl = QDateEdit(self.formLayoutWidget)
        self.dateTgl.setObjectName(u"dateTgl")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateTgl)

        self.lblAlamat = QLabel(self.formLayoutWidget)
        self.lblAlamat.setObjectName(u"lblAlamat")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblAlamat)

        self.lblJK = QLabel(self.formLayoutWidget)
        self.lblJK.setObjectName(u"lblJK")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblJK)

        self.cmbJK = QComboBox(self.formLayoutWidget)
        self.cmbJK.addItem("")
        self.cmbJK.addItem("")
        self.cmbJK.setObjectName(u"cmbJK")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cmbJK)

        self.lblGol = QLabel(self.formLayoutWidget)
        self.lblGol.setObjectName(u"lblGol")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblGol)

        self.cmbGol = QComboBox(self.formLayoutWidget)
        self.cmbGol.addItem("")
        self.cmbGol.addItem("")
        self.cmbGol.addItem("")
        self.cmbGol.addItem("")
        self.cmbGol.setObjectName(u"cmbGol")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cmbGol)

        self.txtAlamat = QTextEdit(self.formLayoutWidget)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 270, 201, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(220, 270, 221, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(450, 270, 241, 20))
        self.tblMustahik = QTableWidget(Form)
        if (self.tblMustahik.columnCount() < 8):
            self.tblMustahik.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblMustahik.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tblMustahik.setObjectName(u"tblMustahik")
        self.tblMustahik.setGeometry(QRect(10, 380, 681, 181))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 350, 681, 20))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 300, 681, 18))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 330, 61, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblKode.setText(QCoreApplication.translate("Form", u"KODE MUSTAHIK", None))
        self.lblNama.setText(QCoreApplication.translate("Form", u"NAMA MUSTAHIK", None))
        self.lblNik.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.lblTempat.setText(QCoreApplication.translate("Form", u"TEMPAT LAHIR", None))
        self.lblTgl.setText(QCoreApplication.translate("Form", u"TANGGAL LAHIR", None))
        self.lblAlamat.setText(QCoreApplication.translate("Form", u"ALAMAT", None))
        self.lblJK.setText(QCoreApplication.translate("Form", u"JENIS KELAMIN", None))
        self.cmbJK.setItemText(0, QCoreApplication.translate("Form", u"Perempuan", None))
        self.cmbJK.setItemText(1, QCoreApplication.translate("Form", u"Laki - Laki", None))

        self.lblGol.setText(QCoreApplication.translate("Form", u"GOLONGAN", None))
        self.cmbGol.setItemText(0, QCoreApplication.translate("Form", u"Fakir", None))
        self.cmbGol.setItemText(1, QCoreApplication.translate("Form", u"Muallaf", None))
        self.cmbGol.setItemText(2, QCoreApplication.translate("Form", u"Miskin", None))
        self.cmbGol.setItemText(3, QCoreApplication.translate("Form", u"Gharim", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblMustahik.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Mustahik", None));
        ___qtablewidgetitem1 = self.tblMustahik.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Mustahik", None));
        ___qtablewidgetitem2 = self.tblMustahik.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"NIK", None));
        ___qtablewidgetitem3 = self.tblMustahik.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None));
        ___qtablewidgetitem4 = self.tblMustahik.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None));
        ___qtablewidgetitem5 = self.tblMustahik.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem6 = self.tblMustahik.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem7 = self.tblMustahik.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Golongan", None));
        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
    # retranslateUi

