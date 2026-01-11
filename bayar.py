# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb

class bayar(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("bayar.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formBayar = loader.load(file_ui, self)
        file_ui.close
        self.resize(self.formBayar.size())
        self.crud = my_cruddb()
        self.formBayar.btnSimpan.clicked.connect(self.doSimpanBayar)
        self.formBayar.btnHapus.clicked.connect(self.doHapusBayar)
        self.tampilData()


    def doSimpanBayar(self):
        tempKode = self.formBayar.editKode.text()
        tempNama = self.formBayar.editNama.text()
        tempHarga = self.formBayar.editHarga.text()
        tempJumlah = self.formBayar.editJumlah.text()
        tempTotal = self.formBayar.editTotal.text()
        self.crud.simpanBayar(tempKode,tempNama,tempHarga,tempJumlah,tempTotal)
        tempTotal = ("diskon 0.9%")
        self.tampilData()

    def doHapusBayar(self):
        tempKode = self.formBayar.editKode.text()
        self.crud.hapusBayar(tempKode)
        self.tampilData

    def tampilData(self):
        baris = self.crud.dataBayar()
        print(baris)
        self.formBayar.tblBayar.setRowCount(0)
        for r in baris:
            i = self.formBayar.tblBayar.rowCount()
            self.formBayar.tblBayar.insertRow(i)
            self.formBayar.tblBayar.setItem(i,0,QTableWidgetItem(str(r["kode"])))
            self.formBayar.tblBayar.setItem(i,1,QTableWidgetItem(r["namaBarang"]))
            self.formBayar.tblBayar.setItem(i,2,QTableWidgetItem(r["harga"]))
            self.formBayar.tblBayar.setItem(i,3,QTableWidgetItem(r["jumlah"]))
            self.formBayar.tblBayar.setItem(i,4,QTableWidgetItem(r["total"]))


