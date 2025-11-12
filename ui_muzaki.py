# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'muzaki.ui'
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
        Form.resize(1008, 409)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 321, 206))
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

        self.lblTempat = QLabel(self.formLayoutWidget)
        self.lblTempat.setObjectName(u"lblTempat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblTempat)

        self.editTempat = QLineEdit(self.formLayoutWidget)
        self.editTempat.setObjectName(u"editTempat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editTempat)

        self.lblTgl = QLabel(self.formLayoutWidget)
        self.lblTgl.setObjectName(u"lblTgl")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTgl)

        self.dateTgl = QDateEdit(self.formLayoutWidget)
        self.dateTgl.setObjectName(u"dateTgl")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateTgl)

        self.lblAlamat = QLabel(self.formLayoutWidget)
        self.lblAlamat.setObjectName(u"lblAlamat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblAlamat)

        self.lblJK = QLabel(self.formLayoutWidget)
        self.lblJK.setObjectName(u"lblJK")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblJK)

        self.cmbJK = QComboBox(self.formLayoutWidget)
        self.cmbJK.addItem("")
        self.cmbJK.addItem("")
        self.cmbJK.setObjectName(u"cmbJK")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbJK)

        self.lblNik = QLabel(self.formLayoutWidget)
        self.lblNik.setObjectName(u"lblNik")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblNik)

        self.editNik = QLineEdit(self.formLayoutWidget)
        self.editNik.setObjectName(u"editNik")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editNik)

        self.txtAlamat = QTextEdit(self.formLayoutWidget)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtAlamat)

        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(340, 10, 581, 171))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblPekerjaan = QLabel(self.formLayoutWidget_2)
        self.lblPekerjaan.setObjectName(u"lblPekerjaan")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPekerjaan)

        self.editPekerjaan = QLineEdit(self.formLayoutWidget_2)
        self.editPekerjaan.setObjectName(u"editPekerjaan")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editPekerjaan)

        self.lblStatus = QLabel(self.formLayoutWidget_2)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.formLayoutWidget_2)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.lblPenghasilan = QLabel(self.formLayoutWidget_2)
        self.lblPenghasilan.setObjectName(u"lblPenghasilan")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPenghasilan)

        self.editPenghasilan = QLineEdit(self.formLayoutWidget_2)
        self.editPenghasilan.setObjectName(u"editPenghasilan")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editPenghasilan)

        self.lblTelp = QLabel(self.formLayoutWidget_2)
        self.lblTelp.setObjectName(u"lblTelp")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTelp)

        self.editTelp = QLineEdit(self.formLayoutWidget_2)
        self.editTelp.setObjectName(u"editTelp")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTelp)

        self.lblEmail = QLabel(self.formLayoutWidget_2)
        self.lblEmail.setObjectName(u"lblEmail")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblEmail)

        self.editEmail = QLineEdit(self.formLayoutWidget_2)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editEmail)

        self.lblUser = QLabel(self.formLayoutWidget_2)
        self.lblUser.setObjectName(u"lblUser")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblUser)

        self.editUser = QLineEdit(self.formLayoutWidget_2)
        self.editUser.setObjectName(u"editUser")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editUser)

        self.lblPass = QLabel(self.formLayoutWidget_2)
        self.lblPass.setObjectName(u"lblPass")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblPass)

        self.editPass = QLineEdit(self.formLayoutWidget_2)
        self.editPass.setObjectName(u"editPass")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editPass)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(340, 190, 171, 20))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(520, 190, 191, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(725, 190, 191, 20))
        self.tblMuzaki = QTableWidget(Form)
        if (self.tblMuzaki.columnCount() < 14):
            self.tblMuzaki.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblMuzaki.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tblMuzaki.setObjectName(u"tblMuzaki")
        self.tblMuzaki.setGeometry(QRect(10, 280, 911, 101))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 250, 911, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 230, 61, 16))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(340, 220, 581, 18))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblKode.setText(QCoreApplication.translate("Form", u"KODE MUZAKI", None))
        self.lblNama.setText(QCoreApplication.translate("Form", u"NAMA MUZAKI", None))
        self.lblTempat.setText(QCoreApplication.translate("Form", u"TEMPAT LAHIR", None))
        self.lblTgl.setText(QCoreApplication.translate("Form", u"TANGGAL LAHIR", None))
        self.lblAlamat.setText(QCoreApplication.translate("Form", u"ALAMAT", None))
        self.lblJK.setText(QCoreApplication.translate("Form", u"JENIS KELAMIN", None))
        self.cmbJK.setItemText(0, QCoreApplication.translate("Form", u"Perempuan", None))
        self.cmbJK.setItemText(1, QCoreApplication.translate("Form", u"Laki - Laki", None))

        self.lblNik.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.lblPekerjaan.setText(QCoreApplication.translate("Form", u"PEKERJAAN", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"STATUS PERKAWINAN", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("Form", u"Kawin", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("Form", u"Belum Kawin", None))

        self.lblPenghasilan.setText(QCoreApplication.translate("Form", u"PENGHASILAN", None))
        self.lblTelp.setText(QCoreApplication.translate("Form", u"NO TELEPON", None))
        self.lblEmail.setText(QCoreApplication.translate("Form", u"EMAIL", None))
        self.lblUser.setText(QCoreApplication.translate("Form", u"USERNAME", None))
        self.lblPass.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblMuzaki.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Nama Muzaki", None));
        ___qtablewidgetitem1 = self.tblMuzaki.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None));
        ___qtablewidgetitem2 = self.tblMuzaki.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None));
        ___qtablewidgetitem3 = self.tblMuzaki.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kode Muzaki", None));
        ___qtablewidgetitem4 = self.tblMuzaki.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem5 = self.tblMuzaki.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem6 = self.tblMuzaki.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"NIK", None));
        ___qtablewidgetitem7 = self.tblMuzaki.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Pekerjaan", None));
        ___qtablewidgetitem8 = self.tblMuzaki.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Status Perkawinan", None));
        ___qtablewidgetitem9 = self.tblMuzaki.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Penghasilan", None));
        ___qtablewidgetitem10 = self.tblMuzaki.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"No Telepon", None));
        ___qtablewidgetitem11 = self.tblMuzaki.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem12 = self.tblMuzaki.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem13 = self.tblMuzaki.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Password", None));
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
    # retranslateUi

