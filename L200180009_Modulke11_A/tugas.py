##NO 1a
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
tambah_transaksi=("INSERT INTO transaksi(id_nasabahFK,no_rekeningFK,jenis_transaksi,tanggal,jumlah) VALUES(%s,%s,%s,%s,%s)")
data_transaksi = ('11','105','debit',tanggal,'125000')
cursor.execute(tambah_transaksi,data_transaksi)

cnx.commit()
cursor.close()
cnx.close()

##NO1b
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
update_transaksi=("UPDATE transaksi SET jumlah=147000 WHERE no_transaksi=44")
cursor.execute(update_transaksi)

cnx.commit()
print(cursor.rowcount,'record(s) affected')
cursor.close()
cnx.close()

##NO 1a
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
tanggal = datetime.now().date()
tambah_transaksi=("INSERT INTO transaksi(id_nasabahFK,no_rekeningFK,jenis_transaksi,tanggal,jumlah) VALUES(%s,%s,%s,%s,%s)")
data_transaksi = ('11','105','debit',tanggal,'125000')
cursor.execute(tambah_transaksi,data_transaksi)

cnx.commit()
cursor.close()
cnx.close()

##NO1b
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
update_transaksi=("UPDATE transaksi SET jumlah=147000 WHERE no_transaksi=44")
cursor.execute(update_transaksi)

cnx.commit()
print(cursor.rowcount,'record(s) affected')
cursor.close()
cnx.close()

##NO 1c
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
delete_transaksi=("DELETE FROM transaksi WHERE no_transaksi=42")
cursor.execute(delete_transaksi)

cnx.commit()
print(cursor.rowcount, "record(s) deleted")
cursor.close()
cnx.close()

##NO2a
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM nasabah")

myresult = cursor.fetchall()
for x in myresult:
    print(x)
cursor.close()
cnx.close()

##NO2b
import mysql.connector

cnx = mysql.connector.connect(user='root', database='perbankan')
cursor = cnx.cursor()
cursor.execute("""SELECT * FROM nasabah
               WHERE nasabah.id_nasabah IN (SELECT transaksi.id_nasabahFK
               FROM transaksi WHERE tanggal BETWEEN '2009-11-10' AND '2009-12-6')""")

myresult = cursor.fetchall()
for x in myresult:
    print(x)
cursor.close()
cnx.close()
