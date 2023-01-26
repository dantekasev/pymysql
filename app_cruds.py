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

def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("pilih id cusstomer > ")
  sql = "delete from customers where customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))

def search_data(db):
  cursor = db.cursor()
  keyword = input("kata kunci: ")
  sql = "select * from customers where name like %s or address like %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword),)
  cursor.execute(sql, val)
  results = cursor.fetchall()

  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_menu(db):
 print("==APLIKASI CRUD DATABASE PYTHON==")
 print("1. Insert Data")
 print("2. Tampilkan Data")
 print("3. Update Data")
 print("4. Delete Data")
 print("5. Search Data")
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
  delete_data(db)
 elif menu == "5":
  search_data(db)
 elif menu == "0":
  exit()
 else:
  print("menu salah!")

if __name__ == "__main__":
 while(True):
  show_menu(db)