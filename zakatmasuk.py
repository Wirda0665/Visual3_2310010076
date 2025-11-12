# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from CrudDB import my_cruddb

class ZakatMasuk(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_ui = QFile("zakatmasuk.ui")
        file_ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formZakatMasuk = loader.load(file_ui, self)
        file_ui.close()
        self.resize(self.formZakatMasuk.size())
        self.crud = my_cruddb()
        self.formZakatMasuk.btnSimpan.clicked.connect(self.doSimpanZakatMasuk)
        self.formZakatMasuk.btnUbah.clicked.connect(self.doUbahZakatMasuk)
        self.formZakatMasuk.btnHapus.clicked.connect(self.doHapusZakatMasuk)
        self.formZakatMasuk.btnClear.clicked.connect(self.doBersih)
        self.tampilData()
        self.isiComboBox()
        self.formZakatMasuk.editCari.textChanged.connect(self.doCariZakatMasuk)

    def isiComboBox(self):
        try:
            # ambil semua data zakat
            data_zakat = self.crud.dataZakat()
            self.formZakatMasuk.cmbKdZakat.clear()
            for z in data_zakat:
                self.formZakatMasuk.cmbKdZakat.addItem(z["kdZakat"])

            # ambil semua data muzaki
            data_muzaki = self.crud.dataMuzaki()
            self.formZakatMasuk.cmbKdMuzaki.clear()
            for m in data_muzaki:
                self.formZakatMasuk.cmbKdMuzaki.addItem(m["kdMuzaki"])

            # ambil id admin
            data_admin = self.crud.dataAdmin()
            self.formZakatMasuk.cmbIdAdmin.clear()
            for m in data_admin:
                self.formZakatMasuk.cmbIdAdmin.addItem(str(m["idAdmin"]))

        except Exception as e:
            print("Gagal Isi Combobox:", e)

    def doSimpanZakatMasuk(self):
        if not self.formZakatMasuk.editNotrans.text().strip():
            QMessageBox.information(None,"Informasi","Nomor Transaksi belum di isi")
            self.formZakatMasuk.editNotrans.setFocus()
        elif not self.formZakatMasuk.cmbKdZakat.currentText().strip():
            QMessageBox.information(None,"Informasi","Kode Zakat belum di isi")
            self.formZakatMasuk.cmbKdZakat.setFocus()
        elif not self.formZakatMasuk.cmbKdMuzaki.currentText().strip():
            QMessageBox.information(None,"Informasi","Kode Muzaki belum di isi")
            self.formZakatMasuk.cmbKdMuzaki.setFocus()
        elif not self.formZakatMasuk.editJumlah.text().strip():
            QMessageBox.information(None,"Informasi","Jumlah belum di isi")
            self.formZakatMasuk.editJumlah.setFocus()
        elif not self.formZakatMasuk.cmbBentuk.currentText().strip():
            QMessageBox.information(None,"Informasi","Bentuk Zakat Masuk belum di isi")
            self.formZakatKeluar.cmbBentuk.setFocus()
        elif not self.formZakatMasuk.editTglMsk.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None,"Informasi","Tanggal Masuk belum di isi")
            self.formZakatMasuk.editTglMsk.setFocus()
        elif not self.formZakatMasuk.editNorek.text().strip():
            QMessageBox.information(None,"Informasi","Nomor Rekening belum di isi")
            self.formZakatMasuk.editNorek.setFocus()
        elif not self.formZakatMasuk.editBukti.text().strip():
            QMessageBox.information(None,"Informasi","Bukti belum di isi")
            self.formZakatMasuk.editBukti.setFocus()
        elif not self.formZakatMasuk.txtKet.text().strip():
            QMessageBox.information(None,"Informasi","Keterangan belum di isi")
            self.formZakatMasuk.txtKet.setFocus()
        elif not self.formZakatMasuk.cmbStatus.currentText().strip():
            QMessageBox.information(None,"Informasi","Status belum di isi")
            self.formZakatMasuk.cmbStatus.setFocus()
        elif not self.formZakatMasuk.cmbIdAdmin.currentText().strip():
            QMessageBox.information(None,"Informasi","ID Admin belum di isi")
            self.formZakatMasuk.cmbIdAdmin.setFocus()
        else:
            pesan = QMessageBox.information(None, "Informasi","Apakah Anda Yakin Menyimpan Data Ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:

                tempNoTrans = self.formZakatMasuk.editNotrans.text()
                tempKdZakat = self.formZakatMasuk.cmbKdZakat.currentText()
                tempKdMuzaki = self.formZakatMasuk.cmbKdMuzaki.currentText()
                tempJumlah = self.formZakatMasuk.editJumlah.text()
                tempBentuk = self.formZakatMasuk.cmbBentuk.currentText()
                tempTgl = self.formZakatMasuk.editTglMsk.date().toString("yyyy-MM-dd")
                tempNorek = self.formZakatMasuk.editNorek.text()
                tempBukti = self.formZakatMasuk.editBukti.text()
                tempKet = self.formZakatMasuk.txtKet.text()
                tempStatus = self.formZakatMasuk.cmbStatus.currentText()
                tempIdAdmin = self.formZakatMasuk.cmbIdAdmin.currentText()
                self.crud.simpanZakatMasuk(tempNoTrans, tempKdZakat, tempKdMuzaki, tempJumlah, tempBentuk, tempTgl, tempNorek, tempBukti, tempKet, tempStatus, tempIdAdmin)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
            else:
                pass

    def doUbahZakatMasuk(self):
        tempNoTrans = self.formZakatMasuk.editNotrans.text()
        tempKdZakat = self.formZakatMasuk.cmbKdZakat.currentText()
        tempKdMuzaki = self.formZakatMasuk.cmbKdMuzaki.currentText()
        tempJumlah = self.formZakatMasuk.editJumlah.text()
        tempBentuk = self.formZakatMasuk.cmbBentuk.currentText()
        tempTgl = self.formZakatMasuk.editTglMsk.date().toString("yyyy-MM-dd")
        tempNorek = self.formZakatMasuk.editNorek.text()
        tempBukti = self.formZakatMasuk.editBukti.text()
        tempKet = self.formZakatMasuk.txtKet.text()
        tempStatus = self.formZakatMasuk.cmbStatus.currentText()
        tempIdAdmin = self.formZakatMasuk.cmbIdAdmin.currentText()
        self.crud.ubahZakatMasuk(tempNoTrans, tempKdZakat, tempKdMuzaki, tempJumlah, tempBentuk, tempTgl, tempNorek, tempBukti, tempKet, tempStatus, tempIdAdmin)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")

    def doHapusZakatMasuk(self):
        tempNoTrans = self.formZakatMasuk.editNotrans.text()
        self.crud.hapusZakatMasuk(tempNoTrans)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")

    def doBersih(self):
        self.formZakatMasuk.editNotrans.clear()
        self.formZakatMasuk.cmbKdZakat.setFocus()
        self.formZakatMasuk.cmbKdMuzaki.setFocus()
        self.formZakatMasuk.editJumlah.clear()
        self.formZakatMasuk.cmbBentuk.setFocus()
        self.formZakatMasuk.editTglMsk.setFocus()
        self.formZakatMasuk.editNorek.clear()
        self.formZakatMasuk.editBukti.clear()
        self.formZakatMasuk.txtKet.clear()
        self.formZakatMasuk.cmbStatus.setFocus()
        self.formZakatMasuk.cmbIdAdmin.setFocus()

    def tampilData(self):
        baris = self.crud.dataZakatMasuk()
        print(baris)
        self.formZakatMasuk.tblZakatMasuk.setRowCount(0)
        for r in baris:
            i = self.formZakatMasuk.tblZakatMasuk.rowCount()
            self.formZakatMasuk.tblZakatMasuk.insertRow(i)
            self.formZakatMasuk.tblZakatMasuk.setItem(i,0,QTableWidgetItem(r["NoTransMasuk"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,1,QTableWidgetItem(r["kdZakat"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,2,QTableWidgetItem(r["kdMuzaki"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,3,QTableWidgetItem(str(r["JumlahMasuk"])))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,4,QTableWidgetItem(r["bentuk"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,5,QTableWidgetItem(str(r["tglMasuk"])))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,6,QTableWidgetItem(r["norek"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,7,QTableWidgetItem(r["bukti"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,8,QTableWidgetItem(r["ket"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,9,QTableWidgetItem(r["status"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,10,QTableWidgetItem(str(r["idAdmin"])))


    def doCariZakatMasuk(self):
        cari = self.formZakatMasuk.editCari.text()
        baris = self.crud.CariZakatMasuk(cari)
        self.formZakatMasuk.tblZakatMasuk.setRowCount(0)
        for r in baris:
            i = self.formZakatMasuk.tblZakatMasuk.rowCount()
            self.formZakatMasuk.tblZakatMasuk.insertRow(i)
            self.formZakatMasuk.tblZakatMasuk.setItem(i,0,QTableWidgetItem(r["NoTransMasuk"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,1,QTableWidgetItem(r["kdZakat"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,2,QTableWidgetItem(r["kdMuzaki"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,3,QTableWidgetItem(str(r["JumlahMasuk"])))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,4,QTableWidgetItem(r["bentuk"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,5,QTableWidgetItem(str(r["tglMasuk"])))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,6,QTableWidgetItem(r["norek"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,7,QTableWidgetItem(r["bukti"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,8,QTableWidgetItem(r["ket"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,9,QTableWidgetItem(r["status"]))
            self.formZakatMasuk.tblZakatMasuk.setItem(i,10,QTableWidgetItem(str(r["idAdmin"])))

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = ZakatMasuk()
    #window.show()
    #sys.exit(app.exec())
