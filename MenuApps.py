from os import system
from json import dump, load
from datetime import datetime
 
def print_menu():
    system("cls")
    print("""
    Aplikasi Pendataan Menu Restoran Sederhana
    [1]. Lihat Semua Menu
    [2]. Tambah Menu Baru
    [3]. Cari Menu
    [4]. Hapus Menu
    [5]. Update Menu
    [6]. Tentang Aplikasi
    [Q]. Keluar
        """)
 
def print_header(msg):
    system("cls")
    print(msg)
 
def not_empty(container):
    if len(container) != 0:
        return True
    else:
        return False
 
def verify_ans(char):
    if char.upper() == "Y":
        return True
    else:
        return False
 
def print_data(id_menu=None, nama=True, harga=True, stok=True, all_data=False):
    if id_menu != None and all_data == False:
        print(f"ID : {id_menu}")
        print(f"NAMA : {menus[id_menu]['nama']}")
        print(f"HARGA : {menus[id_menu]['harga']}")
        print(f"STOK : {menus[id_menu]['stok']}")
    elif stok == False and all_data == False:
        print(f"ID : {id_menu}")
        print(f"NAMA : {menus[id_menu]['nama']}")
        print(f"HARGA : {menus[id_menu]['harga']}")
 
    elif all_data == True:
        for id_menu in menus: # lists, string, dict
            nama = menus[id_menu]["nama"]
            harga = menus[id_menu]["harga"]
            stok = menus[id_menu]["stok"]
            print(f"ID : {id_menu} - NAMA : {nama} - HARGA : {harga} - STOK : {stok}")
 
def view_menus():
    print_header("DAFTAR MENU TERSIMPAN")
    if not_empty(menus):
        print_data(all_data=True)
    else:
        print("MAAF BELUM ADA MENU TERSIMPAN")
    input("Tekan ENTER untuk kembali ke MENU")
 
def create_id_menu(name, price):
    hari_ini = datetime.now()
    tahun = hari_ini.year
    bulan = hari_ini.month
    hari = hari_ini.day
 
    counter = len(menus) + 1
    first = name[0].upper()
    last_3 = price[-3:]
    
    id_menu = ("%04d%02d%02d-R%03d%s%s" % (tahun, bulan, hari, counter, first, last_3))
    return id_menu
 
 
 
def add_menu():
    print_header("MENAMBAHKAN MENU BARU")
    nama = input("NAMA \t: ")
    harga = input("HARGA \t: ")
    stok = input("STOK \t: ")
    respon = input(f"Apakah yakin ingin menyimpan menu : {nama} ? (Y/N) ")
    if verify_ans(respon):
        id_menu = create_id_menu(name=nama, price=harga)
        menus[id_menu] = {
            "nama" : nama,
            "harga" : harga,
            "stok" : stok
        }
        saved = save_data_menus()
        if saved:
            print("Data Menu Tersimpan.")
        else:
            print("Kesalahan saat menyimpan")
    else:
        print("Data Batal Disimpan")
    input("Tekan ENTER untuk kembali ke MENU")
 
def searching_by_name(menu):
    for id_menu in menus:
        if menus[id_menu]['nama'] == menu:
            return id_menu
    else:
        return False
 
def find_menu():
    print_header("MENCARI MENU")
    nama = input("Nama Menu yang Dicari : ")
    exists = searching_by_name(nama)
    if exists:
        print("Data Ditemukan")
        print_data(id_menu=exists)
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
def delete_menu():
    print_header("MENGHAPUS MENU")
    nama = input("Nama Menu yang akan Dihapus : ")
    exists = searching_by_name(nama)
    if exists:
        print_data(id_menu=exists)
        respon = input(f"Yakin ingin menghapus {nama} ? (Y/N) ")
        if verify_ans(respon):
            del menus[exists]
            saved = save_data_menus()
            if saved:
                print("Data Menu Telah Dihapus")
            else:
                print("Kesalahan saat menyimpan")
        else:
            print("Data Menu Batal Dihapus")
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
def update_nama_menu(id_menu):
    print(f"Nama Lama : {menus[id_menu]['nama']}")
    new_name = input("Masukkan Nama Menu Yang baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        menus[id_menu]['nama'] = new_name
        print("Data Telah di simpan")
        print_data(id_menu)
    else:
        print("Data Batal diubah")
 
def update_harga_menu(id_menu):
    print(f"Harga Menu Lama : {menus[id_menu]['harga']}")
    new_price = input("Masukkan Harga Menu Yang Baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        menus[id_menu]['harga'] = new_price
        print("Data Telah di simpan")
        print_data(id_menu)
    else:
        print("Data Batal diubah")
 
def update_stok_menu(id_menu):
    print(f"Stok Menu Lama : {menus[id_menu]['stok']}")
    new_stock = input("Masukkan Stok Menu Yang Baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        menus[id_menu]['stok'] = new_stock
        print("Data Telah di simpan")
        print_data(id_menu)
    else:
        print("Data Batal diubah")
 
def update_menu():
    print_header("MENGUPDATE INFO MENU")
    nama = input("Nama Menu yang akan di-update : ")
    exists = searching_by_name(nama)
    if exists:
        print_data(exists)
        print("EDIT FIELD [1] NAMA - [2] HARGA - [3] STOK")
        respon = input("MASUKAN PILIHAN (1/2/3) : ")
        if respon == "1":
            update_nama_menu(exists)
        elif respon == "2":
            update_harga_menu(exists)
        elif respon == "3":
            update_stok_menu(exists)
        saved = save_data_menus()
        if saved:
            print("Data Menu Telah di-update.")
        else:
            print("Kesalahan saat menyimpan")
 
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
def about_application():
    print_header("TENTANG APLIKASI")
    print("APLIKASI INI DI BUAT OLEH : Riccardo Rehyan S"
        "DI BUAT PADA TANGGAL : 21/11/2020")

def check_user_input(char):
    char = char.upper()
    if char == "Q":
        print("BYE!!!")
        return True
    elif char == "1":
        view_menus()
    elif char == "2":
        add_menu()
    elif char == "3":
        find_menu()
    elif char == "4":
        delete_menu()
    elif char == "5":
        update_menu()
    elif char == "6":
        about_application()
        return True
def load_data_menus():
    with open(file_path, 'r') as file:
        data = load(file)
    return data
 
def save_data_menus():
    with open(file_path, 'w') as file:
        dump(menus, file)
    return True
 
 
#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "mytxt/menu.json"
menus = load_data_menus()
while not stop:
    print_menu()
    user_input = input("Pilihan : ")
    stop = check_user_input(user_input)