# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionMustahik = QAction(Main)
        self.actionMustahik.setObjectName(u"actionMustahik")
        self.actionMuzaki = QAction(Main)
        self.actionMuzaki.setObjectName(u"actionMuzaki")
        self.actionZakat = QAction(Main)
        self.actionZakat.setObjectName(u"actionZakat")
        self.actionZakat_Keluar = QAction(Main)
        self.actionZakat_Keluar.setObjectName(u"actionZakat_Keluar")
        self.actionZakat_Masuk = QAction(Main)
        self.actionZakat_Masuk.setObjectName(u"actionZakat_Masuk")
        self.actionAdmin = QAction(Main)
        self.actionAdmin.setObjectName(u"actionAdmin")
        self.actionbayar = QAction(Main)
        self.actionbayar.setObjectName(u"actionbayar")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addAction(self.actionMustahik)
        self.menuMenu_Utama.addAction(self.actionMuzaki)
        self.menuMenu_Utama.addAction(self.actionZakat)
        self.menuMenu_Utama.addAction(self.actionZakat_Keluar)
        self.menuMenu_Utama.addAction(self.actionZakat_Masuk)
        self.menuMenu_Utama.addAction(self.actionAdmin)
        self.menuMenu_Utama.addAction(self.actionbayar)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.actionMustahik.setText(QCoreApplication.translate("Main", u"Mustahik", None))
        self.actionMuzaki.setText(QCoreApplication.translate("Main", u"Muzaki", None))
        self.actionZakat.setText(QCoreApplication.translate("Main", u"Zakat", None))
        self.actionZakat_Keluar.setText(QCoreApplication.translate("Main", u"Zakat Keluar", None))
        self.actionZakat_Masuk.setText(QCoreApplication.translate("Main", u"Zakat Masuk", None))
        self.actionAdmin.setText(QCoreApplication.translate("Main", u"Admin", None))
        self.actionbayar.setText(QCoreApplication.translate("Main", u"Bayar", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("Main", u"Menu Utama", None))
    # retranslateUi

