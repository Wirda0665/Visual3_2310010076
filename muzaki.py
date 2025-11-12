# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb

class Muzaki(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("muzaki.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formMuzaki = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formMuzaki.size())
        self.crud = my_cruddb()
        self.formMuzaki.btnSimpan.clicked.connect(self.doSimpanMuzaki)
        self.formMuzaki.btnUbah.clicked.connect(self.doUbahMuzaki)
        self.formMuzaki.btnHapus.clicked.connect(self.doHapusMuzaki)
        self.formMuzaki.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.formMuzaki.editCari.textChanged.connect(self.doCariMuzaki)


    def doSimpanMuzaki(self):
        if not self.formMuzaki.editKode.text().strip():
            QMessageBox.information(None,"Informasi","Kode Muzaki belum di isi")
            self.formMuzaki.editKode.setFocus()
        elif not self.formMuzaki.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Muzaki belum di isi")
            self.formMuzaki.editNama.setFocus()
        elif not self.formMuzaki.editTempat.text().strip():
            QMessageBox.information(None,"Informasi","Tempat belum di isi")
            self.formMuzaki.editTempat.setFocus()
        elif not self.formMuzaki.dateTgl.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None,"Informasi","Tanggal belum di isi")
            self.formMuzaki.dateTgl.setFocus()
        elif not self.formMuzaki.txtAlamat.toPlainText().strip():
            QMessageBox.information(None,"Informasi","Alamat belum di isi")
            self.formMuzaki.txtAlamat.setFocus()
        elif not self.formMuzaki.cmbJK.currentText().strip():
            QMessageBox.information(None,"Informasi","Jenis Kelamin belum di isi")
            self.formMuzaki.cmbJK.setFocus()
        elif not self.formMuzaki.editNik.text().strip():
            QMessageBox.information(None,"Informasi","NIK belum di isi")
            self.formMuzaki.editNik.setFocus()
        elif not self.formMuzaki.editPekerjaan.text().strip():
            QMessageBox.information(None,"Informasi","Pekerjaan belum di isi")
            self.formMuzaki.editPekerjaan.setFocus()
        elif not self.formMuzaki.cmbStatus.currentText().strip():
            QMessageBox.information(None,"Informasi","Status belum di isi")
            self.formMuzaki.cmbStatus.setFocus()
        elif not self.formMuzaki.editPenghasilan.text().strip():
            QMessageBox.information(None,"Informasi","Penghasilan belum di isi")
            self.formMuzaki.editPenghasilan.setFocus()
        elif not self.formMuzaki.editTelp.text().strip():
            QMessageBox.information(None,"Informasi","Nomor Telepon belum di isi")
            self.formMuzaki.editTelp.setFocus()
        elif not self.formMuzaki.editEmail.text().strip():
            QMessageBox.information(None,"Informasi","Email belum di isi")
            self.formMuzaki.editEmail.setFocus()
        elif not self.formMuzaki.editUser.text().strip():
            QMessageBox.information(None,"Informasi","Username belum di isi")
            self.formMuzaki.editUser.setFocus()
        elif not self.formMuzaki.editPass.text().strip():
            QMessageBox.information(None,"Informasi","Password belum di isi")
            self.formMuzaki.editPass.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempKD = self.formMuzaki.editKode.text()
                tempNama = self.formMuzaki.editNama.text()
                tempTempat = self.formMuzaki.editTempat.text()
                tempTglLahir = self.formMuzaki.dateTgl.date().toString("yyyy-MM-dd")
                tempAlamat = self.formMuzaki.txtAlamat.toPlainText()
                tempJK = self.formMuzaki.cmbJK.currentText()
                tempNik = self.formMuzaki.editNik.text()
                tempPekerjaan = self.formMuzaki.editPekerjaan.text()
                tempStatus = self.formMuzaki.cmbStatus.currentText()
                tempPenghasilan = self.formMuzaki.editPenghasilan.text()
                tempTelp = self.formMuzaki.editTelp.text()
                tempEmail = self.formMuzaki.editEmail.text()
                tempUsername = self.formMuzaki.editUser.text()
                tempPassword = self.formMuzaki.editPass.text()
                self.crud.simpanMuzaki(tempKD, tempNama, tempTempat, tempTglLahir, tempAlamat, tempJK, tempNik, tempPekerjaan, tempStatus, tempPenghasilan, tempTelp, tempEmail, tempUsername, tempPassword)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass

    def doUbahMuzaki(self):
        tempKD = self.formMuzaki.editKode.text()
        tempNama = self.formMuzaki.editNama.text()
        tempTempat = self.formMuzaki.editTempat.text()
        tempTglLahir = self.formMuzaki.dateTgl.date().toString("yyyy-MM-dd")
        tempAlamat = self.formMuzaki.txtAlamat.toPlainText()
        tempJK = self.formMuzaki.cmbJK.currentText()
        tempNik = self.formMuzaki.editNik.text()
        tempPekerjaan = self.formMuzaki.editPekerjaan.text()
        tempStatus = self.formMuzaki.cmbStatus.currentText()
        tempPenghasilan = self.formMuzaki.editPenghasilan.text()
        tempTelp = self.formMuzaki.editTelp.text()
        tempEmail = self.formMuzaki.editEmail.text()
        tempUsername = self.formMuzaki.editUser.text()
        tempPassword = self.formMuzaki.editPass.text()
        self.crud.ubahMuzaki(tempKD, tempNama, tempTempat, tempTglLahir, tempAlamat, tempJK, tempNik, tempPekerjaan, tempStatus, tempPenghasilan, tempTelp, tempEmail, tempUsername, tempPassword)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusMuzaki(self):
        tempKD = self.formMuzaki.editKode.text()
        self.crud.hapusMuzaki(tempKD)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formMuzaki.editKode.clear()
        self.formMuzaki.editNama.clear()
        self.formMuzaki.editTempat.clear()
        self.formMuzaki.dateTgl.setFocus()
        self.formMuzaki.txtAlamat.clear()
        self.formMuzaki.cmbJK.setFocus()
        self.formMuzaki.editNik.clear()
        self.formMuzaki.editPekerjaan.clear()
        self.formMuzaki.cmbStatus.setFocus()
        self.formMuzaki.editPenghasilan.clear()
        self.formMuzaki.editEmail.clear()
        self.formMuzaki.editEmail.clear()
        self.formMuzaki.editUser.clear()
        self.formMuzaki.editPass.clear()

    def tampilData(self):
        baris = self.crud.dataMuzaki()
        print(baris)
        self.formMuzaki.tblMuzaki.setRowCount(0)
        for r in baris:
            i = self.formMuzaki.tblMuzaki.rowCount()
            self.formMuzaki.tblMuzaki.insertRow(i)
            self.formMuzaki.tblMuzaki.setItem(i,0,QTableWidgetItem(r["kdMuzaki"]))
            self.formMuzaki.tblMuzaki.setItem(i,1,QTableWidgetItem(r["namaMuzaki"]))
            self.formMuzaki.tblMuzaki.setItem(i,2,QTableWidgetItem(r["tempat"]))
            self.formMuzaki.tblMuzaki.setItem(i,3,QTableWidgetItem(r["tglLahir"]))
            self.formMuzaki.tblMuzaki.setItem(i,4,QTableWidgetItem(r["alamat"]))
            self.formMuzaki.tblMuzaki.setItem(i,5,QTableWidgetItem(r["Jk"]))
            self.formMuzaki.tblMuzaki.setItem(i,6,QTableWidgetItem(r["NIK"]))
            self.formMuzaki.tblMuzaki.setItem(i,7,QTableWidgetItem(r["Pekerjaan"]))
            self.formMuzaki.tblMuzaki.setItem(i,8,QTableWidgetItem(r["StatusPerkawinan"]))
            self.formMuzaki.tblMuzaki.setItem(i,9,QTableWidgetItem(str(r["Penghasilan"])))
            self.formMuzaki.tblMuzaki.setItem(i,10,QTableWidgetItem(r["Notel"]))
            self.formMuzaki.tblMuzaki.setItem(i,11,QTableWidgetItem(r["Email"]))
            self.formMuzaki.tblMuzaki.setItem(i,12,QTableWidgetItem(r["Username"]))
            self.formMuzaki.tblMuzaki.setItem(i,13,QTableWidgetItem(r["Password"]))

    def doCariMuzaki(self):
        cari = self.formMuzaki.editCari.text()
        baris = self.crud.CariMuzaki(cari)
        self.formMuzaki.tblMuzaki.setRowCount(0)
        for r in baris:
            i = self.formMuzaki.tblMuzaki.rowCount()
            self.formMuzaki.tblMuzaki.insertRow(i)
            self.formMuzaki.tblMuzaki.setItem(i,0,QTableWidgetItem(r["kdMuzaki"]))
            self.formMuzaki.tblMuzaki.setItem(i,1,QTableWidgetItem(r["namaMuzaki"]))
            self.formMuzaki.tblMuzaki.setItem(i,2,QTableWidgetItem(r["tempat"]))
            self.formMuzaki.tblMuzaki.setItem(i,3,QTableWidgetItem(r["tglLahir"]))
            self.formMuzaki.tblMuzaki.setItem(i,4,QTableWidgetItem(r["alamat"]))
            self.formMuzaki.tblMuzaki.setItem(i,5,QTableWidgetItem(r["Jk"]))
            self.formMuzaki.tblMuzaki.setItem(i,6,QTableWidgetItem(r["NIK"]))
            self.formMuzaki.tblMuzaki.setItem(i,7,QTableWidgetItem(r["Pekerjaan"]))
            self.formMuzaki.tblMuzaki.setItem(i,8,QTableWidgetItem(r["StatusPerkawinan"]))
            self.formMuzaki.tblMuzaki.setItem(i,9,QTableWidgetItem(r["Penghasilan"]))
            self.formMuzaki.tblMuzaki.setItem(i,10,QTableWidgetItem(r["Notel"]))
            self.formMuzaki.tblMuzaki.setItem(i,11,QTableWidgetItem(r["Email"]))
            self.formMuzaki.tblMuzaki.setItem(i,12,QTableWidgetItem(r["Username"]))
            self.formMuzaki.tblMuzaki.setItem(i,13,QTableWidgetItem(r["Password"]))

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = Muzaki()
    #window.show()
    #sys.exit(app.exec())
