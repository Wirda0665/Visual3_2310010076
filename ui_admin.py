# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(547, 367)
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(10, 150, 151, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 150, 151, 20))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(330, 150, 171, 20))
        self.tblAdmin = QTableWidget(Form)
        if (self.tblAdmin.columnCount() < 6):
            self.tblAdmin.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblAdmin.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblAdmin.setObjectName(u"tblAdmin")
        self.tblAdmin.setGeometry(QRect(10, 250, 491, 131))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 491, 136))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblIdAdmin = QLabel(self.formLayoutWidget)
        self.lblIdAdmin.setObjectName(u"lblIdAdmin")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblIdAdmin)

        self.editIdAdmin = QLineEdit(self.formLayoutWidget)
        self.editIdAdmin.setObjectName(u"editIdAdmin")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editIdAdmin)

        self.lblNama = QLabel(self.formLayoutWidget)
        self.lblNama.setObjectName(u"lblNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNama)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.lblJK = QLabel(self.formLayoutWidget)
        self.lblJK.setObjectName(u"lblJK")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblJK)

        self.cmbJK = QComboBox(self.formLayoutWidget)
        self.cmbJK.addItem("")
        self.cmbJK.addItem("")
        self.cmbJK.setObjectName(u"cmbJK")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbJK)

        self.lblUser = QLabel(self.formLayoutWidget)
        self.lblUser.setObjectName(u"lblUser")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblUser)

        self.editUser = QLineEdit(self.formLayoutWidget)
        self.editUser.setObjectName(u"editUser")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editUser)

        self.lblPass = QLabel(self.formLayoutWidget)
        self.lblPass.setObjectName(u"lblPass")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblPass)

        self.editPass = QLineEdit(self.formLayoutWidget)
        self.editPass.setObjectName(u"editPass")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editPass)

        self.lblStatus = QLabel(self.formLayoutWidget)
        self.lblStatus.setObjectName(u"lblStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblStatus)

        self.cmbStatus = QComboBox(self.formLayoutWidget)
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.cmbStatus.setObjectName(u"cmbStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbStatus)

        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 220, 491, 20))
        self.btnClear = QPushButton(Form)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(10, 180, 491, 18))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 200, 71, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tblAdmin.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Admin", None));
        ___qtablewidgetitem1 = self.tblAdmin.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Admin", None));
        ___qtablewidgetitem2 = self.tblAdmin.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem3 = self.tblAdmin.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem4 = self.tblAdmin.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Password", None));
        ___qtablewidgetitem5 = self.tblAdmin.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Status", None));
        self.lblIdAdmin.setText(QCoreApplication.translate("Form", u"ID Admin", None))
        self.lblNama.setText(QCoreApplication.translate("Form", u"Nama Admin", None))
        self.lblJK.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.cmbJK.setItemText(0, QCoreApplication.translate("Form", u"Laki - Laki", None))
        self.cmbJK.setItemText(1, QCoreApplication.translate("Form", u"Perempuan", None))

        self.lblUser.setText(QCoreApplication.translate("Form", u"Username", None))
        self.lblPass.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"Status", None))
        self.cmbStatus.setItemText(0, QCoreApplication.translate("Form", u"PNS", None))
        self.cmbStatus.setItemText(1, QCoreApplication.translate("Form", u"Pelajar", None))
        self.cmbStatus.setItemText(2, QCoreApplication.translate("Form", u"Mahasiswa", None))
        self.cmbStatus.setItemText(3, QCoreApplication.translate("Form", u"Wiraswasta", None))
        self.cmbStatus.setItemText(4, QCoreApplication.translate("Form", u"Guru / Dosen", None))
        self.cmbStatus.setItemText(5, QCoreApplication.translate("Form", u"TNI / POLRI", None))
        self.cmbStatus.setItemText(6, QCoreApplication.translate("Form", u"Dokter / Perawat", None))
        self.cmbStatus.setItemText(7, QCoreApplication.translate("Form", u"Ibu Rumah Tangga", None))
        self.cmbStatus.setItemText(8, QCoreApplication.translate("Form", u"Lainnya", None))

        self.btnClear.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"CARI DATA", None))
    # retranslateUi

