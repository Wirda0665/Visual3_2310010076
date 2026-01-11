# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'visual3_2310010076'
        )


    def simpanAdmin(self, id, nama, jk, username, password, status):
        cursor = self.conn.cursor()
        cursor.execute("insert into admin (idAdmin, NamaAdmin, Jk, Username, Password, Status) value(%s,%s,%s,%s,%s,%s)",(id, nama, jk, username, password, status))
        self.conn.commit()
        cursor.close()

    def ubahAdmin(self, id, nama, jk, username, password, status):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE admin SET NamaAdmin=%s, Jk=%s, Username=%s, Password=%s, Status=%s WHERE idAdmin=%s",(nama, jk, username, password, status, id))
        self.conn.commit()
        cursor.close()

    def hapusAdmin(self, id):
        cursor = self.conn.cursor()
        cursor.execute("delete from admin where idAdmin=%s",(id,))
        self.conn.commit()
        cursor.close()

    def dataAdmin(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from admin order by idAdmin asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariAdmin(self,param):
        sql = "select * from admin where idAdmin like %s or NamaAdmin like %s or Jk like %s or Username like %s or Password like %s or Status like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record


    def simpanMustahik(self, kd, nama, nik, tempat, tgllahir, alamat, jk, golongan):
        cursor = self.conn.cursor()
        cursor.execute("insert into mustahik (kdMustahik, NamaMustahik, NIK, Tempat, tglLahir, Alamat, Jk, golongan) value(%s,%s,%s,%s,%s,%s,%s,%s)",(kd, nama, nik, tempat, tgllahir, alamat, jk, golongan))
        self.conn.commit()
        cursor.close()

    def ubahMustahik(self, kd, nama, nik, tempat, tgllahir, alamat, jk, golongan):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE mustahik SET NamaMustahik=%s, NIK=%s, Tempat=%s, tglLahir=%s, Alamat=%s, Jk=%s, golongan=%s WHERE kdMustahik=%s",(nama, nik, tempat, tgllahir, alamat, jk, golongan, kd))
        self.conn.commit()
        cursor.close()

    def hapusMustahik(self, kd):
        cursor = self.conn.cursor()
        cursor.execute("delete from mustahik where kdMustahik=%s",(kd,))
        self.conn.commit()
        cursor.close()

    def dataMustahik(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from mustahik order by kdMustahik asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariMustahik(self,param):
        sql = "select * from mustahik where kdMustahik like %s or NamaMustahik like %s or NIK like %s or Tempat like %s or tglLahir like %s or Alamat like %s or Jk like %s or golongan like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record



    def simpanMuzaki(self, kd, nama, tempat, tgllahir, alamat, jk, nik, pekerjaan, status, penghasilan, notel, email, username, password):
        cursor = self.conn.cursor()
        cursor.execute("insert into muzaki (kdMuzaki, namaMuzaki, tempat, tglLahir, alamat, Jk, NIK, Pekerjaan, StatusPerkawinan, Penghasilan, Notel, Email, Username, Password) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(kd, nama, tempat, tgllahir, alamat, jk, nik, pekerjaan, status, penghasilan, notel, email, username, password))
        self.conn.commit()
        cursor.close()

    def ubahMuzaki(self, kd, nama, tempat, tgllahir, alamat, jk, nik, pekerjaan, status, penghasilan, notel, email, username, password):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE muzaki SET namaMuzaki=%s, tempat=%s, tglLahir=%s, alamat=%s, Jk=%s, NIK=%s, Pekerjaan=%s, StatusPerkawinan=%s, Penghasilan=%s, Notel=%s, Email=%s, Username=%s, Password=%s WHERE kdMuzaki=%s",(nama, tempat, tgllahir, alamat, jk, nik, pekerjaan, status, penghasilan, notel, email, username, password, kd))
        self.conn.commit()
        cursor.close()

    def hapusMuzaki(self, kd):
        cursor = self.conn.cursor()
        cursor.execute("delete from muzaki where kdMuzaki=%s",(kd,))
        self.conn.commit()
        cursor.close()

    def dataMuzaki(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from muzaki order by kdMuzaki asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariMuzaki(self,param):
        sql = "select * from muzaki where kdMuzaki like %s or namaMuzaki like %s or Tempat like %s or tglLahir like %s or Alamat like %s or Jk like %s or NIK like %s or Pekerjaan like %s or StatusPerkawinan like %s or Penghasilan like %s or Notel like %s or Email like %s or Username like %s or Password like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record




    def simpanZakat(self, kd, nama, bentuk, saldo, ket):
        cursor = self.conn.cursor()
        cursor.execute("insert into zakat (kdZakat, NamaZakat, bentuk, saldo, ket) value(%s,%s,%s,%s,%s)",(kd, nama, bentuk, saldo, ket))
        self.conn.commit()
        cursor.close()

    def ubahZakat(self, kd, nama, bentuk, saldo, ket):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE zakat SET NamaZakat=%s, bentuk=%s, saldo=%s, ket=%s WHERE kdZakat=%s",(nama, bentuk, saldo, ket, kd))
        self.conn.commit()
        cursor.close()

    def hapusZakat(self, kd):
        cursor = self.conn.cursor()
        cursor.execute("delete from zakat where kdZakat=%s",(kd,))
        self.conn.commit()
        cursor.close()

    def dataZakat(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from zakat order by kdZakat asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariZakat(self,param):
        sql = "select * from zakat where kdZakat like %s or NamaZakat like %s or bentuk like %s or saldo like %s or ket like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record




    def simpanZakatKeluar(self, no, kdzakat, kdmustahik, jumlah, bentuk, tglmasuk, idadmin, ket):
        cursor = self.conn.cursor()
        cursor.execute("insert into zakatkeluar (NoTransKeluar, kdZakat, kdMustahik, JumlahKeluar, bentuk, tglMasuk, idAdmin, ket) value(%s,%s,%s,%s,%s,%s,%s,%s)",(no, kdzakat, kdmustahik, jumlah, bentuk, tglmasuk, idadmin, ket))
        self.conn.commit()
        cursor.close()

    def ubahZakatKeluar(self, no, kdzakat, kdmustahik, jumlah, bentuk, tglmasuk, idadmin, ket):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE zakatkeluar SET kdZakat=%s, kdMustahik=%s, JumlahKeluar=%s, bentuk=%s, tglMasuk=%s, idAdmin=%s, ket=%s WHERE NoTransKeluar=%s",(kdzakat, kdmustahik, jumlah, bentuk, tglmasuk, idadmin, ket, no))
        self.conn.commit()
        cursor.close()

    def hapusZakatKeluar(self, no):
        cursor = self.conn.cursor()
        cursor.execute("delete from zakatkeluar where NoTransKeluar=%s",(no,))
        self.conn.commit()
        cursor.close()

    def dataZakatKeluar(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from zakatkeluar order by NoTransKeluar asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariZakatKeluar(self,param):
        sql = "select * from zakatkeluar where NoTransKeluar like %s or kdZakat like %s or kdMustahik like %s or JumlahKeluar like %s or Bentuk like %s or tglMasuk like %s or idAdmin like %s or ket like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record




    def simpanZakatMasuk(self, no, kdzakat, kdmuzaki, jumlah, bentuk, tglmasuk, norek, bukti, ket, status, idadmin):
        cursor = self.conn.cursor()
        cursor.execute("insert into zakatmasuk (NoTransMasuk, kdZakat, kdMuzaki, JumlahMasuk, bentuk, tglMasuk, norek, bukti, ket, status, idAdmin) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(no, kdzakat, kdmuzaki, jumlah, bentuk, tglmasuk, norek, bukti, ket, status, idadmin))
        self.conn.commit()
        cursor.close()

    def ubahZakatMasuk(self, no, kdzakat, kdmuzaki, jumlah, bentuk, tglmasuk, norek, bukti, ket, status, idadmin):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE zakatmasuk SET kdZakat=%s, kdMuzaki=%s, JumlahMasuk=%s, bentuk=%s, tglMasuk=%s, norek=%s, bukti=%s, ket=%s, status=%s, idAdmin=%s WHERE NoTransMasuk=%s",(kdzakat, kdmuzaki, jumlah, bentuk, tglmasuk, norek, bukti, ket, status, idadmin, no))
        self.conn.commit()
        cursor.close()

    def hapusZakatMasuk(self, no):
        cursor = self.conn.cursor()
        cursor.execute("delete from zakatmasuk where NoTransMasuk=%s",(no,))
        self.conn.commit()
        cursor.close()

    def dataZakatMasuk(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from zakatmasuk order by NoTransMasuk asc")
        record = cursor.fetchall()
        cursor.close()
        return record

    def CariZakatMasuk(self,param):
        sql = "select * from zakatmasuk where NoTransMasuk like %s or kdZakat like %s or kdMuzaki like %s or JumlahMasuk like %s or Bentuk like %s or tglMasuk like %s or norek like %s or bukti like %s or ket like %s or status like %s or idAdmin like %s"
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute(sql,[f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = cursor.fetchall()
        cursor.close()
        return record


    def simpanBayar(self, kode, namaBarang, harga, jumlah, total):
        cursor = self.conn.cursor()
        cursor.execute("insert into bayar (kode, namaBarang, harga, jumlah, total) value(%s,%s,%s,%s,%s)",(kode, namaBarang, harga, jumlah, total))
        self.conn.commit()
        cursor.close()

    def hapusBayar(self, kode):
        cursor = self.conn.cursor()
        cursor.execute("delete from bayar where kode=%s",(kode,))
        self.conn.commit()
        cursor.close()

    def dataBayar(self):
        cursor = self.conn.cursor(dictionary = True)
        cursor.execute("select * from bayar order by kode asc")
        record = cursor.fetchall()
        cursor.close()
        return record
