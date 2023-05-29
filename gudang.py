import sys
import pyinputplus as pyip

def Main_Menu():
    print(f'''
-------- Selamat Datang di Gudang Minimarket JCDS --------
    ''')
    # menginput fitur yang ingin ditampilkan 
    prompt = "Pilihan Menu Yang Tersedia :\n"
    choice = ['Menampilkan List Menu', 'Update Data Transaksi dan Stock Card','Add Data Stock Card', 'Delete Data Stock Card', 'Exit']
    response = pyip.inputMenu(prompt=prompt, choices=choice, numbered=True)
    print(response)
    # Fitur menampilkan daftar sub menu
    if response == choice[0]:
        Sub_Menu()
    # Fitur merubah data
    elif response == choice[1]:
        Update_Data_SC()
    #     # Fitur menambah data
    elif response == choice[2]:
        Add_SC()
    #     # Fitur menghapus data
    elif response == choice[3]:
        Delete_SC()
    #     # Fitur exit program
    else:
         sys.exit()

def Tampilan_SubMenu_Utama(menu):
    # Function to display the menu
    for item in menu:
        print(item)

def show_List_Barang(Dict, FuncFormat, title="\n---------- Daftar Barang yang Tersedia ----------\n", val=0):
    # Function to show the list of available items
    print(title)
    for value in Dict.values():
        if val == 0:
            print(FuncFormat.format("", *value))
        else:
            if val in value:
                print(FuncFormat.format("", *value))
                break

def show_Tabel_SC(Dict, Format_SC, titleSC, val=0):
    # Function to display the stock card table
    print(titleSC)
    for value in Dict.values():
        if val == 0:
            print(Format_SC.format("", *value))
        else:
            if val in value:
                print(Format_SC.format("", *value)) 
                break
                

def Sub_Menu():
    while True:
        print('\n----------------------------------------------------------\nPilihan Menu Yang Tersedia :\n')
        prompt = "Masukkan angka menu yang ingin dijalankan: "
        ListMenu = [
            "1. Daftar Stock Barang Terkini",
            "2. Stock Card Product",
            "3. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
            show_List_Barang(ListBarang, FuncFormat)
        elif response == '2':
            show_Tabel_SC(Stock_Card, Format_SC, titleSC)
        elif response == '3':
            Main_Menu()

def Add_SC(): # pada penamabahan data di index ke 5 selalu loncat ke 6 walaupun di index = len(Stock_Card) -1
    while True:
        prompt = "Masukkan angka menu yang ingin dijalankan:\n"
        ListMenu = [
            "1. Add Data Stock Card",
            "2. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
        # update data stock card
            show_Tabel_SC(Stock_Card,Format_SC,titleSC)
            print('\nSilahkan Lengkapi Data Berikut :')
            tanggal = pyip.inputStr(prompt='Masukan Tanggal Transaksi (YYYY/MM/DD) : ', blockRegexes=[r'[a-zA-Z]'])
            jenis_transaksi = pyip.inputStr(prompt='Masukkan Jenis Transaksi : ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])

        # Loop item di dalam Stock_Card
            transaksi_exist = False
            for key, value in Stock_Card.copy().items():
            # Apabila transaksi sudah ada di dalam daftar
                if key == 'column':
                    continue
                elif tanggal and jenis_transaksi in value:
                    print('Transaksi sudah ada')
                    transaksi_exist = True
                    break
            # Apabila transaksi tidak ada di dalam daftar
                if not transaksi_exist: 
                    kode_barang = pyip.inputInt(prompt='Masukkan Kode Barang : ', greaterThan=0,blockRegexes=[r'[a-zA-Z]']) 
                    harga = pyip.inputInt(prompt='Masukan Harga Barang :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=000)
                    qty = pyip.inputInt(prompt='Masukan Qty Barang :', blockRegexes=[r'[a-zA-Z]'], greaterThan=0)
                    stock_balance = pyip.inputInt(prompt='Masukan Stock Balance :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=0)
                    add = pyip.inputYesNo(prompt="\nIngin menambahkan data?(yes/no): ")
                    if add == 'yes' or add == 'y':
                        index = len(Stock_Card)
                        Stock_Card.update({
                            f'transaksi{index}': [
                                index, 
                                tanggal,
                                kode_barang,
                                jenis_transaksi,
                                qty,
                                harga,
                                stock_balance
                            ]
                            }
                        )
                        break
                    else:
                        break
            # Menampilkan daftar stock data terbaru
            show_Tabel_SC(Stock_Card, Format_SC,titleSC)
            Main_Menu()
        elif response == 2:
            Main_Menu()


def Delete_SC(): # kenapa tabel yang dihapus tidak sesuai dengan tabel yang ditampilkan per index?
    while True:
        prompt = "Masukkan angka menu yang ingin dijalankan:\n"
        ListMenu = [
            "1. Delete Transaksi Stock Card",
            "2. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
            while True:
                index = int(input("Masukkan indeks transaksi yang ingin dihapus: ")) 

                if index == 0:
                    print('Tidak diperbolehkan menghapus judul tabel.')
                    continue

                elif index >= 1 and index < len(Stock_Card):
                    deleted_key = list(Stock_Card.keys())[index]
                    show_Tabel_SC(Stock_Card, Format_SC, titleSC, index)
                    confirm = input(f"Apakah Anda yakin ingin menghapus transaksi dengan indeks {index}? (y/n): ")
                    if confirm.lower() == 'y':
                        del Stock_Card[deleted_key]
                        print('Transaksi Stock Card berhasil dihapus.')
                        show_Tabel_SC(Stock_Card,Format_SC,titleSC)  # Show updated table after deletion
                    else:
                        print('Penghapusan transaksi dibatalkan.')
                    break

                else:
                    print('Indeks transaksi tidak valid. Silahkan coba lagi.')

        elif response == '2':
            Main_Menu()
        else:
            print('Angka yang dimasukkan tidak terdapat di List Menu. Silahkan coba lagi.')
            continue

def Update_Data_SC():
    while True:
        print('\n------------- Menu Update Data Minimarket JCDS -----------')
        prompt = "Masukkan angka menu yang ingin dijalankan: "
        print('\nData mana yang ingin anda ubah? ')
        ListMenuUtama_Update = [
            "1. Update Stock Terkini",
            "2. Update Stock card",
            "3. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenuUtama_Update)
        response = input(prompt)

        if response == '1':
            # menampilkan data terkini
            show_List_Barang(ListBarang, FuncFormat)
            key_exists = False                    
            while True:    
            # meminta user input primary key
                primary_key = pyip.inputInt(prompt='\nMasukan Kode Barang : ', blockRegexes=[r'[a-zA-Z]'], greaterThan=100)
                for key, value in ListBarang.items():
                    if key == 'column':
                        continue
                    elif primary_key in value:
                        key_exists = True
                        show_List_Barang(ListBarang,FuncFormat,primary_key)
                        break
                if key_exists:
                    break
                else:
                    print('Kode barang tidak ada. Silakan coba lagi.')
                # konfirmasi apakah yakin data ini yang akan di update
            while True:
                update = pyip.inputYesNo(prompt="\nIngin merubah data pada kode barang ini?(yes/no): ")
                if update == 'yes':
                # meminta inputan kolom mana yang akan di update
                    while True:
                        prompt = "\nMasukkan angka menu kolom yang ingin dijalankan: "
                        print('\nData Yang Bisa Anda Ubah dan jalankan:')
                        ListMenu1 = [
                                "1. Stock Terkini",
                                "2. Level Stock",
                                "3. Back"
                            ]
                        Tampilan_SubMenu_Utama(ListMenu1)
                        response = input(prompt)
                # meminta value terbaru yang akan diubah
                        if response == '1':
                            live_stock = pyip.inputInt(prompt='Masukan jumlah stock terbaru :', blockRegexes=[r'[a-zA-Z]'], greaterThan=0)
                            for key, value in ListBarang.items():
                                if key == 'column':
                                    continue
                                elif primary_key in value:
                                    value[4] = live_stock
                                    break
                                else: 
                                    continue
                            show_List_Barang(ListBarang,FuncFormat)                             
                            print('\n-------- DATA BERHASIL DIPERBARUI --------') 
                        elif response == '2':
                            level_stock = pyip.inputStr(prompt='Masukkan Level Stock Terkini: ', applyFunc=lambda x: x.title())
                            for key, value in ListBarang.items():
                                if key == 'column':
                                    continue
                                elif primary_key in value:
                                    value[5] = level_stock
                                    break
                            print('Data berhasil diperbarui.')
                            show_List_Barang(ListBarang, FuncFormat)
                            break
                        elif response == '3':
                            Tampilan_SubMenu_Utama(ListMenuUtama_Update)
                            break
                else:
                    # Main_Menu()
                    break
        elif response == '2':
            found = False
            #while True:
            show_Tabel_SC(Stock_Card, Format_SC,titleSC)
            # meminta user input index
            index_update = pyip.inputInt(prompt='\nMasukkan Indeks Stock Card yang Ingin Diubah: ', blockRegexes=[r'[a-zA-Z]'])
            for key, value in Stock_Card.items():
                if key == 'column':
                    continue
                elif index_update in value:
                    found = True
                    key_update = key
                    break
            if found == True:
                show_Tabel_SC(Stock_Card, Format_SC, titleSC, index_update)
                update = pyip.inputYesNo(prompt="\nIngin merubah data pada kode barang ini?(yes/no): ")
                #while True:
                if update == 'yes':
                    tanggal = pyip.inputStr(prompt='Masukkan Tanggal Transaksi (YYYY/MM/DD): ', blockRegexes=[r'[a-zA-Z]'])
                    kode_barang = pyip.inputInt(prompt='Masukkan Kode Barang: ',greaterThan=100, blockRegexes=[r'[a-zA-Z]'])
                    jenis_transaksi = pyip.inputStr(prompt='Masukkan Jenis Transaksi: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
                    harga = pyip.inputInt(prompt='Masukkan Harga Barang: ', greaterThan=0)
                    qty = pyip.inputInt(prompt='Masukkan Qty Barang: ', greaterThan=0)
                    stock_balance = pyip.inputInt(prompt='Masukkan Stock Balance: ', greaterThan=0)
                    Stock_Card[key_update][1] = tanggal
                    Stock_Card[key_update][2] = kode_barang
                    Stock_Card[key_update][3] = jenis_transaksi
                    Stock_Card[key_update][4] = qty
                    Stock_Card[key_update][5] = harga
                    Stock_Card[key_update][6] = stock_balance
                    print('Data berhasil diperbarui.')
                    show_Tabel_SC(Stock_Card, Format_SC,titleSC)
                else:
                    Main_Menu()
        elif response == '3':
            Main_Menu()    


if __name__ == '__main__':
    Stock_Card = {
        'column': ["Index", "Tanggal", "Kode Barang", "Jenis Transaksi", "Qty", "Harga", "Stock Balance"],
        'transaksi1': [0, '2023/01/01', 101, "Saldo Awal", 150, 2000, 150],
        'transaksi2': [1, '2023/01/01', 102, "Saldo Awal", 150, 20000, 150],
        'transaksi3': [2, '2023/01/01', 201, "Saldo Awal", 150, 5000, 150],
        'transaksi4': [3, '2023/01/01', 202, "Saldo Awal", 150, 8000, 150],
        'transaksi5': [4, '2023/01/05', 101, "Penjualan", 50, 2000, 100]        
    }
    
    titleSC = '\n----------- Stock Card ----------\n'
    Format_SC = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<20}"+ "{:<8}"+ "{:<10}" + "{:<15}"
    
    ListBarang = {
        'column': ["Index", "Kode Barang", "Nama Barang", "Jenis Barang", "Stock Terkini", "Level Stock"],
        'barang1': [0, 101, "Mie Instan", "Makanan", 100, "Low Stock"],
        'barang2': [1, 102, "Sereal", "Makanan", 150, "Available"],
        'barang3': [2, 201, "Susu", "Minuman", 150, "Available"],
        'barang4': [3, 202, "Kopi", "Minuman", 150, "Available"],
    } # yang dibuat fungsi input hanya stock terkini trs level stock dibuat if

    FuncFormat = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<15}"+ "{:<15}"+ "{:<15}"
    Main_Menu()



''' Permasalahan:
1.  pada regular func def update
    - Stock Card index 0 tdk bisa di pilih yang muncul secara keseluruhan bukan index yang dipilih
    - di Update stock terkini blm bisa menampilkan perbaris index yang dipilih
2.  Belum kesimpan di global jadi kalau mau update/save di tampilan awal tdk berubah
3.  def add
    no index 5 tdk ada jadi langsung dilanjutkan ke index 6
4. reg.func def update


1. Di def delete no index kenapa jadi acak
2. data yang diubah blm tersimpan diglobal
3. def update data blm kelar
4. blm disesuai dengan flow chart
5. blm di edit" nama dan keterangan '''