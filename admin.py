# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb


class Admin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("admin.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formAdmin = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formAdmin.size())
        self.crud = my_cruddb()
        self.formAdmin.btnSimpan.clicked.connect(self.doSimpanAdmin)
        self.formAdmin.btnUbah.clicked.connect(self.doUbahAdmin)
        self.formAdmin.btnHapus.clicked.connect(self.doHapusAdmin)
        self.formAdmin.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.formAdmin.editCari.textChanged.connect(self.doCariAdmin)


    def doSimpanAdmin(self):
        if not self.formAdmin.editIdAdmin.text().strip():
            QMessageBox.information(None,"Informasi","ID Admin belum di isi")
            self.formAdmin.editIdAdmin.setFocus()
        elif not self.formAdmin.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Admin belum di isi")
            self.formAdmin.editNama.setFocus()
        elif not self.formAdmin.cmbJK.currentText().strip():
            QMessageBox.information(None,"Informasi","Jenis Kelamin belum di isi")
            self.formAdmin.cmbJK.setFocus()
        elif not self.formAdmin.editUser.text().strip():
            QMessageBox.information(None,"Informasi","Username belum di isi")
            self.formAdmin.editUser.setFocus()
        elif not self.formAdmin.editPass.text().strip():
            QMessageBox.information(None,"Informasi","Password belum di isi")
            self.formAdmin.editPass.setFocus()
        elif not self.formAdmin.cmbStatus.currentText().strip():
            QMessageBox.information(None,"Informasi","Status belum di isi")
            self.formAdmin.cmbStatus.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempID = self.formAdmin.editIdAdmin.text()
                tempNama = self.formAdmin.editNama.text()
                tempJK = self.formAdmin.cmbJK.currentText()
                tempUser = self.formAdmin.editUser.text()
                tempPass = self.formAdmin.editPass.text()
                tempStatus = self.formAdmin.cmbStatus.currentText()
                self.crud.simpanAdmin(tempID, tempNama, tempJK, tempUser, tempPass, tempStatus)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass

    def doUbahAdmin(self):
        tempID = self.formAdmin.editIdAdmin.text()
        tempNama = self.formAdmin.editNama.text()
        tempJK = self.formAdmin.cmbJK.currentText()
        tempUser = self.formAdmin.editUser.text()
        tempPass = self.formAdmin.editPass.text()
        tempStatus = self.formAdmin.cmbStatus.currentText()
        self.crud.ubahAdmin(tempID, tempNama, tempJK, tempUser, tempPass, tempStatus)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusAdmin(self):
        tempID = self.formAdmin.editIdAdmin.text()
        self.crud.hapusAdmin(tempID)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formAdmin.editIdAdmin.clear()
        self.formAdmin.editNama.clear()
        self.formAdmin.cmbJK.setFocus()
        self.formAdmin.editUser.clear()
        self.formAdmin.editPass.clear()
        self.formAdmin.cmbStatus.setFocus()

    def tampilData(self):
        baris = self.crud.dataAdmin()
        print(baris)
        self.formAdmin.tblAdmin.setRowCount(0)
        for r in baris:
            i = self.formAdmin.tblAdmin.rowCount()
            self.formAdmin.tblAdmin.insertRow(i)
            self.formAdmin.tblAdmin.setItem(i,0,QTableWidgetItem(str(r["idAdmin"])))
            self.formAdmin.tblAdmin.setItem(i,1,QTableWidgetItem(r["NamaAdmin"]))
            self.formAdmin.tblAdmin.setItem(i,2,QTableWidgetItem(r["Jk"]))
            self.formAdmin.tblAdmin.setItem(i,3,QTableWidgetItem(r["Username"]))
            self.formAdmin.tblAdmin.setItem(i,4,QTableWidgetItem(r["Password"]))
            self.formAdmin.tblAdmin.setItem(i,5,QTableWidgetItem(r["Status"]))


    def doCariAdmin(self):
        cari = self.formAdmin.editCari.text()
        baris = self.crud.CariAdmin(cari)
        self.formAdmin.tblAdmin.setRowCount(0)
        for r in baris:
            i = self.formAdmin.tblAdmin.rowCount()
            self.formAdmin.tblAdmin.insertRow(i)
            self.formAdmin.tblAdmin.setItem(i,0,QTableWidgetItem(str(r["idAdmin"])))
            self.formAdmin.tblAdmin.setItem(i,1,QTableWidgetItem(r["NamaAdmin"]))
            self.formAdmin.tblAdmin.setItem(i,2,QTableWidgetItem(r["Jk"]))
            self.formAdmin.tblAdmin.setItem(i,3,QTableWidgetItem(r["Username"]))
            self.formAdmin.tblAdmin.setItem(i,4,QTableWidgetItem(r["Password"]))
            self.formAdmin.tblAdmin.setItem(i,5,QTableWidgetItem(r["Status"]))

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = Mustahik()
    #window.show()
    #sys.exit(app.exec())
