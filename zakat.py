# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb

class Zakat(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("zakat.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formZakat = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formZakat.size())
        self.crud = my_cruddb()
        self.formZakat.btnSimpan.clicked.connect(self.doSimpanZakat)
        self.formZakat.btnUbah.clicked.connect(self.doUbahZakat)
        self.formZakat.btnHapus.clicked.connect(self.doHapusZakat)
        self.formZakat.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.formZakat.editCari.textChanged.connect(self.doCariZakat)


    def doSimpanZakat(self):
        if not self.formZakat.editKode.text().strip():
            QMessageBox.information(None,"Informasi","Kode Zakat belum di isi")
            self.formZakat.editKode.setFocus()
        elif not self.formZakat.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Zakat belum di isi")
            self.formZakat.editNama.setFocus()
        elif not self.formZakat.cmbBentuk.currentText().strip():
            QMessageBox.information(None,"Informasi","Bentuk Zakat belum di isi")
            self.formZakat.cmbBentuk.setFocus()
        elif not self.formZakat.editSaldo.text().strip():
            QMessageBox.information(None,"Informasi","Saldo belum di isi")
            self.formZakat.editSaldo.setFocus()
        elif not self.formZakat.txtKet.toPlainText().strip():
            QMessageBox.information(None,"Informasi","Keterangan belum di isi")
            self.formZakat.txtKet.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempKD = self.formZakat.editKode.text()
                tempNama = self.formZakat.editNama.text()
                tempBentuk = self.formZakat.cmbBentuk.currentText()
                tempSaldo = self.formZakat.editSaldo.text()
                tempKet = self.formZakat.txtKet.toPlainText()
                self.crud.simpanZakat(tempKD, tempNama, tempBentuk, tempSaldo, tempKet)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass

    def doUbahZakat(self):
        tempKD = self.formZakat.editKode.text()
        tempNama = self.formZakat.editNama.text()
        tempBentuk = self.formZakat.cmbBentuk.currentText()
        tempSaldo = self.formZakat.editSaldo.text()
        tempKet = self.formZakat.txtKet.toPlainText()
        self.crud.ubahZakat(tempKD, tempNama, tempBentuk, tempSaldo, tempKet)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusZakat(self):
        tempKD = self.formZakat.editKode.text()
        self.crud.hapusZakat(tempKD)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formZakat.editKode.clear()
        self.formZakat.editNama.clear()
        self.formZakat.cmbBentuk.setFocus()
        self.formZakat.editSaldo.clear()
        self.formZakat.txtKet.clear()

    def tampilData(self):
        baris = self.crud.dataZakat()
        print(baris)
        self.formZakat.tblZakat.setRowCount(0)
        for r in baris:
            i = self.formZakat.tblZakat.rowCount()
            self.formZakat.tblZakat.insertRow(i)
            self.formZakat.tblZakat.setItem(i,0,QTableWidgetItem(r["kdZakat"]))
            self.formZakat.tblZakat.setItem(i,1,QTableWidgetItem(r["NamaZakat"]))
            self.formZakat.tblZakat.setItem(i,2,QTableWidgetItem(r["bentuk"]))
            self.formZakat.tblZakat.setItem(i,3,QTableWidgetItem(str(r["saldo"])))
            self.formZakat.tblZakat.setItem(i,4,QTableWidgetItem(r["ket"]))

    def doCariZakat(self):
        cari = self.formZakat.editCari.text()
        baris = self.crud.CariZakat(cari)
        self.formZakat.tblZakat.setRowCount(0)
        for r in baris:
            i = self.formZakat.tblZakat.rowCount()
            self.formZakat.tblZakat.insertRow(i)
            self.formZakat.tblZakat.setItem(i,0,QTableWidgetItem(r["kdZakat"]))
            self.formZakat.tblZakat.setItem(i,1,QTableWidgetItem(r["NamaZakat"]))
            self.formZakat.tblZakat.setItem(i,2,QTableWidgetItem(r["bentuk"]))
            self.formZakat.tblZakat.setItem(i,3,QTableWidgetItem(str(r["saldo"])))
            self.formZakat.tblZakat.setItem(i,4,QTableWidgetItem(r["ket"]))

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = Zakat()
    #window.show()
    #sys.exit(app.exec())
