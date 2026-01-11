# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb

class ZakatKeluar(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("zakatkeluar.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formZakatKeluar = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formZakatKeluar.size())
        self.crud = my_cruddb()
        self.formZakatKeluar.btnSimpan.clicked.connect(self.doSimpanZakatKeluar)
        self.formZakatKeluar.btnUbah.clicked.connect(self.doUbahZakatKeluar)
        self.formZakatKeluar.btnHapus.clicked.connect(self.doHapusZakatKeluar)
        self.formZakatKeluar.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.isiComboBox()
        self.formZakatKeluar.editCari.textChanged.connect(self.doCariZakatKeluar)


    def isiComboBox(self):
        try:
            # ambil data zakat
            data_zakat = self.crud.dataZakat()
            self.formZakatKeluar.cmbKdZakat.clear()
            for z in data_zakat:
                self.formZakatKeluar.cmbKdZakat.addItem(z["kdZakat"])

            # ambil data mustahik
            data_mustahik = self.crud.dataMustahik()
            self.formZakatKeluar.cmbKdMustahik.clear()
            for m in data_mustahik:
                self.formZakatKeluar.cmbKdMustahik.addItem(m["kdMustahik"])

            # ambil id admin
            data_admin = self.crud.dataAdmin()
            self.formZakatKeluar.cmbIdAdmin.clear()
            for m in data_admin:
                self.formZakatKeluar.cmbIdAdmin.addItem(str(m["idAdmin"]))

        except Exception as e:
            print("Gagal Isi Combobox :", e)


    def doSimpanZakatKeluar(self):
        if not self.formZakatKeluar.editTrans.text().strip():
            QMessageBox.information(None,"Informasi","Transaksi belum di isi")
            self.formZakatKeluar.editTrans.setFocus()
        elif not self.formZakatKeluar.cmbKdZakat.currentText().strip():
            QMessageBox.information(None,"Informasi","Kode Zakat belum di isi")
            self.formZakatKeluar.cmbKdZakat.setFocus()
        elif not self.formZakatKeluar.cmbKdMustahik.currentText().strip():
            QMessageBox.information(None,"Informasi","Kode Mustahik belum di isi")
            self.formZakatKeluar.cmbKdMustahik.setFocus()
        elif not self.formZakatKeluar.editJumlah.text().strip():
            QMessageBox.information(None,"Informasi","Jumlah belum di isi")
            self.formZakatKeluar.editJumlah.setFocus()
        elif not self.formZakatKeluar.cmbBentuk.currentText().strip():
            QMessageBox.information(None,"Informasi","Bentuk Zakat Keluar belum di isi")
            self.formZakatKeluar.cmbBentuk.setFocus()
        elif not self.formZakatKeluar.editTglKel.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None,"Informasi","Tanggal Keluar belum di isi")
            self.formZakatKeluar.editTglKel.setFocus()
        elif not self.formZakatKeluar.cmbIdAdmin.currentText().strip():
            QMessageBox.information(None,"Informasi","ID Admin belum di isi")
            self.formZakatKeluar.cmbIdAdmin.setFocus()
        elif not self.formZakatKeluar.txtKet.toPlainText().strip():
            QMessageBox.information(None,"Informasi","Keterangan belum di isi")
            self.formZakatKeluar.txtKet.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempTrans = self.formZakatKeluar.editTrans.text()
                tempKdZakat = self.formZakatKeluar.cmbKdZakat.currentText()
                tempKdMustahik = self.formZakatKeluar.cmbKdMustahik.currentText()
                tempJumlah = self.formZakatKeluar.editJumlah.text()
                tempBentuk = self.formZakatKeluar.cmbBentuk.currentText()
                tempTgl = self.formZakatKeluar.editTglKel.date().toString("yyyy-MM-dd")
                tempIdAdmin = self.formZakatKeluar.cmbIdAdmin.currentText()
                tempKet = self.formZakatKeluar.txtKet.toPlainText()
                self.crud.simpanZakatKeluar(tempTrans, tempKdZakat, tempKdMustahik, tempJumlah, tempBentuk, tempTgl, tempIdAdmin, tempKet)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass

    def doUbahZakatKeluar(self):
        tempTrans = self.formZakatKeluar.editTrans.text()
        tempKdZakat = self.formZakatKeluar.cmbKdZakat.currentText()
        tempKdMustahik = self.formZakatKeluar.cmbKdMustahik.currentText()
        tempJumlah = self.formZakatKeluar.editJumlah.text()
        tempBentuk = self.formZakatKeluar.cmbBentuk.currentText()
        tempTgl = self.formZakatKeluar.editTglKel.date().toString("yyyy-MM-dd")
        tempIdAdmin = self.formZakatKeluar.cmbIdAdmin.currentText()
        tempKet = self.formZakatKeluar.txtKet.toPlainText()
        self.crud.ubahZakatKeluar(tempTrans, tempKdZakat, tempKdMustahik, tempJumlah, tempBentuk, tempTgl, tempIdAdmin, tempKet)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusZakatKeluar(self):
        tempTrans = self.formZakatKeluar.editTrans.text()
        self.crud.hapusZakatKeluar(tempTrans)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formZakatKeluar.editTrans.clear()
        self.formZakatKeluar.cmbKdZakat.setFocus()
        self.formZakatKeluar.cmbKdMustahik.setFocus()
        self.formZakatKeluar.editJumlah.clear()
        self.formZakatKeluar.cmbBentuk.setFocus()
        self.formZakatKeluar.editTglKel.setFocus()
        self.formZakatKeluar.cmbIdAdmin.setFocus()
        self.formZakatKeluar.txtKet.clear()

    def tampilData(self):
        baris = self.crud.dataZakatKeluar()
        print(baris)
        self.formZakatKeluar.tblZakatKeluar.setRowCount(0)
        for r in baris:
            i = self.formZakatKeluar.tblZakatKeluar.rowCount()
            self.formZakatKeluar.tblZakatKeluar.insertRow(i)
            self.formZakatKeluar.tblZakatKeluar.setItem(i,0,QTableWidgetItem(r["NoTransKeluar"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,1,QTableWidgetItem(r["kdZakat"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,2,QTableWidgetItem(r["kdMustahik"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,3,QTableWidgetItem(str(r["JumlahKeluar"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,4,QTableWidgetItem(r["bentuk"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,5,QTableWidgetItem(str(r["tglMasuk"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,6,QTableWidgetItem(str(r["idAdmin"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,7,QTableWidgetItem(r["ket"]))

    def doCariZakatKeluar(self):
        cari = self.formZakatKeluar.editCari.text()
        baris = self.crud.CariZakatKeluar(cari)
        self.formZakatKeluar.tblZakatKeluar.setRowCount(0)
        for r in baris:
            i = self.formZakatKeluar.tblZakatKeluar.rowCount()
            self.formZakatKeluar.tblZakatKeluar.insertRow(i)
            self.formZakatKeluar.tblZakatKeluar.setItem(i,0,QTableWidgetItem(r["NoTransKeluar"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,1,QTableWidgetItem(r["kdZakat"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,2,QTableWidgetItem(r["kdMustahik"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,3,QTableWidgetItem(str(r["JumlahKeluar"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,4,QTableWidgetItem(r["bentuk"]))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,5,QTableWidgetItem(str(r["tglMasuk"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,6,QTableWidgetItem(str(r["idAdmin"])))
            self.formZakatKeluar.tblZakatKeluar.setItem(i,7,QTableWidgetItem(r["ket"]))


#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = ZakatKeluar()
    #window.show()
    #sys.exit(app.exec())
