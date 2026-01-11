# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# Import semua form
from admin import Admin
from mustahik import Mustahik
from muzaki import Muzaki
from zakat import Zakat
from zakatkeluar import ZakatKeluar
from zakatmasuk import ZakatMasuk
from bayar import bayar

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        fileformutama = QFile("main.ui")
        fileformutama.open(QFile.ReadOnly)
        formloader = QUiLoader()
        self.formutama = formloader.load(fileformutama,self)
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())


        # Hubungkan menu ke form
        self.formutama.actionAdmin.triggered.connect(self.buka_admin)
        self.formutama.actionMustahik.triggered.connect(self.buka_mustahik)
        self.formutama.actionMuzaki.triggered.connect(self.buka_muzaki)
        self.formutama.actionZakat.triggered.connect(self.buka_zakat)
        self.formutama.actionZakat_Keluar.triggered.connect(self.buka_zakatkeluar)
        self.formutama.actionZakat_Masuk.triggered.connect(self.buka_zakatmasuk)
        self.formutama.actionbayar.triggered.connect(self.buka_bayar)

    def buka_admin(self):
        self.admin = Admin()
        self.admin.show()


    def buka_mustahik(self):
        self.mustahik = Mustahik()
        self.mustahik.show()

    def buka_muzaki(self):
        self.muzaki = Muzaki()
        self.muzaki.show()

    def buka_zakat(self):
        self.zakat = Zakat()
        self.zakat.show()

    def buka_zakatkeluar(self):
        self.zakatkeluar = ZakatKeluar()
        self.zakatkeluar.show()

    def buka_zakatmasuk(self):
        self.zakatmasuk = ZakatMasuk()
        self.zakatmasuk.show()

    def buka_bayar(self):
        self.bayar = bayar()
        self.bayar.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
