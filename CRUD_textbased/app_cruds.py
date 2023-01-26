import mysql.connector
import os

db = mysql.connector.connect (
 host = "localhost",
 user = "dante",
 password = "dante.123",
 database = "toko_mainan",
)

def insert_data(db):
 name = input("Masukan nama : ")
 address = input("Masukan alamat : ")
 val = (name, address)
 cursor = db.cursor()
 sql = "insert into customers (name, address) values (%s, %s)"
 cursor.execute(sql, val)
 db.commit()
 print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
 cursor = db.cursor()
 sql = "select * from customers"
 cursor.execute(sql)
 results = cursor.fetchall()

 if cursor.rowcount < 0:
  print("Tidak ada data")
 else:
  for data in results:
   print(data)


def update_data(db):
 cursor = db.cursor()
 show_data(db)
 customer_id = input("pilih id customer> ")
 name = input("Nama baru: ")
 address = input("Alamat baru: ")
 
 sql = "update customers set name=%s, address=%s where customer_id=%s"
 val = (name, address, customer_id)
 cursor.execute(sql, val)
 db.commit()
 print("{} data berhasil diubah".format(cursor.rowcount))

def show_menu(db):
 print("==APLIKASI CRUD DATABASE PYTHON==")
 print("1. Insert Data")
 print("2. Tampilkan Data")
 print("3. Update Data")
 print("0. Keluar")
 menu = input("Pilih menu> ")

 #clear screen
 os.system("clear")

 if menu == "1":
  insert_data(db)
 elif menu == "2":
  show_data(db)
 elif menu == "3":
  update_data(db)
 elif menu == "4":
  exit()
 else:
  print("menu salah!")

if __name__ == "__main__":
 while(True):
  show_menu(db)
