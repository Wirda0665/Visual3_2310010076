# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb


class Mustahik(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("mustahik.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formMustahik = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formMustahik.size())
        self.crud = my_cruddb()
        self.formMustahik.btnSimpan.clicked.connect(self.doSimpanMustahik)
        self.formMustahik.btnUbah.clicked.connect(self.doUbahMustahik)
        self.formMustahik.btnHapus.clicked.connect(self.doHapusMustahik)
        self.formMustahik.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.formMustahik.editCari.textChanged.connect(self.doCariMustahik)


    def doSimpanMustahik(self):    
        if not self.formMustahik.editKode.text().strip():
            QMessageBox.information(None,"Informasi","Kode Mustahik belum di isi")
            self.formMustahik.editKode.setFocus()
        elif not self.formMustahik.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Mustahik belum di isi")
            self.formMustahik.editNama.setFocus()
        elif not self.formMustahik.editNik.text().strip():
            QMessageBox.information(None,"Informasi","NIK belum di isi")
            self.formMustahik.editNik.setFocus()
        elif not self.formMustahik.editTempat.text().strip():
            QMessageBox.information(None,"Informasi","Tempat belum di isi")
            self.formMustahik.editTempat.setFocus()
        elif not self.formMustahik.dateTgl.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None,"Informasi","Tanggal belum di isi")
            self.formMustahik.dateTgl.setFocus()
        elif not self.formMustahik.txtAlamat.toPlainText().strip():
            QMessageBox.information(None,"Informasi","Alamat belum di isi")
            self.formMustahik.txtAlamat.setFocus()
        elif not self.formMustahik.cmbJK.currentText().strip():
            QMessageBox.information(None,"Informasi","Jenis Kelamin belum di isi")
            self.formMustahik.cmbStatus.setFocus()
        elif not self.formMustahik.cmbGol.currentText().strip():
            QMessageBox.information(None,"Informasi","Golongan belum di isi")
            self.formMustahik.cmbGol.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempKD = self.formMustahik.editKode.text()
                tempNama = self.formMustahik.editNama.text()
                tempNik = self.formMustahik.editNik.text()
                tempTempat = self.formMustahik.editTempat.text()
                tempTglLahir = self.formMustahik.dateTgl.date().toString("yyyy-MM-dd")
                tempAlamat = self.formMustahik.txtAlamat.toPlainText()
                tempJK = self.formMustahik.cmbJK.currentText()
                tempGolongan = self.formMustahik.cmbGol.currentText()
                self.crud.simpanMustahik(tempKD, tempNama, tempNik, tempTempat, tempTglLahir, tempAlamat, tempJK, tempGolongan)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass


    def doUbahMustahik(self):
        tempKD = self.formMustahik.editKode.text()
        tempNama = self.formMustahik.editNama.text()
        tempNik = self.formMustahik.editNik.text()
        tempTempat = self.formMustahik.editTempat.text()
        tempTglLahir = self.formMustahik.dateTgl.date().toString("yyyy-MM-dd")
        tempAlamat = self.formMustahik.txtAlamat.toPlainText()
        tempJK = self.formMustahik.cmbJK.currentText()
        tempGolongan = self.formMustahik.cmbGol.currentText()
        self.crud.ubahMustahik(tempKD, tempNama, tempNik, tempTempat, tempTglLahir, tempAlamat, tempJK, tempGolongan)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusMustahik(self):
        tempKD = self.formMustahik.editKode.text()
        self.crud.hapusMustahik(tempKD)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formMustahik.editKode.clear()
        self.formMustahik.editNama.clear()
        self.formMustahik.editNik.clear()
        self.formMustahik.editTempat.clear()
        self.formMustahik.dateTgl.setFocus()
        self.formMustahik.txtAlamat.clear()
        self.formMustahik.cmbJK.setFocus()
        self.formMustahik.cmbGol.setFocus()

    def tampilData(self):
        baris = self.crud.dataMustahik()
        print(baris)
        self.formMustahik.tblMustahik.setRowCount(0)
        for r in baris:
            i = self.formMustahik.tblMustahik.rowCount()
            self.formMustahik.tblMustahik.insertRow(i)
            self.formMustahik.tblMustahik.setItem(i,0,QTableWidgetItem(r["kdMustahik"]))
            self.formMustahik.tblMustahik.setItem(i,1,QTableWidgetItem(r["NamaMustahik"]))
            self.formMustahik.tblMustahik.setItem(i,2,QTableWidgetItem(r["NIK"]))
            self.formMustahik.tblMustahik.setItem(i,3,QTableWidgetItem(r["Tempat"]))
            self.formMustahik.tblMustahik.setItem(i,4,QTableWidgetItem(r["tglLahir"]))
            self.formMustahik.tblMustahik.setItem(i,5,QTableWidgetItem(r["Alamat"]))
            self.formMustahik.tblMustahik.setItem(i,6,QTableWidgetItem(r["Jk"]))
            self.formMustahik.tblMustahik.setItem(i,7,QTableWidgetItem(r["golongan"]))

    def doCariMustahik(self):
        cari = self.formMustahik.editCari.text()
        baris = self.crud.CariMustahik(cari)
        self.formMustahik.tblMustahik.setRowCount(0)
        for r in baris:
            i = self.formMustahik.tblMustahik.rowCount()
            self.formMustahik.tblMustahik.insertRow(i)
            self.formMustahik.tblMustahik.setItem(i,0,QTableWidgetItem(r["kdMustahik"]))
            self.formMustahik.tblMustahik.setItem(i,1,QTableWidgetItem(r["NamaMustahik"]))
            self.formMustahik.tblMustahik.setItem(i,2,QTableWidgetItem(r["NIK"]))
            self.formMustahik.tblMustahik.setItem(i,3,QTableWidgetItem(r["Tempat"]))
            self.formMustahik.tblMustahik.setItem(i,4,QTableWidgetItem(r["tglLahir"]))
            self.formMustahik.tblMustahik.setItem(i,5,QTableWidgetItem(r["Alamat"]))
            self.formMustahik.tblMustahik.setItem(i,6,QTableWidgetItem(r["Jk"]))
            self.formMustahik.tblMustahik.setItem(i,7,QTableWidgetItem(r["golongan"]))

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = Mustahik()
    #window.show()
    #sys.exit(app.exec())
