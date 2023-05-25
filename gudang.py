import sys
import pyinputplus as pyip

def Main_Menu():
    print(f'''
Selamat Datang di Gudang Minimarket JCDS
    ''')
    # menginput fitur yang ingin ditampilkan 
    prompt = "Masukan angka menu yang ingin dijalankan\n"
    choice = ['Menampilkan list menu', 'Update Stock terkini','Add Stock Card', 'Delete Data Stock Card', 'Exit']
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

def show_List_Barang(Dict, FuncFormat, title="\nDaftar Barang yang Tersedia\n"):
    # Function to show the list of available items
    print(title)
    for value in Dict.values():
        print(FuncFormat.format("", *value))

def show_Tabel_SC(Dict, Format_SC, titleSC):
    # Function to display the stock card table
    print(titleSC)
    for value in Dict.values():
        print(Format_SC.format("", *value))

def Sub_Menu():
    while True:
        prompt = "Masukkan angka menu yang ingin dijalankan:\n"
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

def Add_SC():
    # update data stock card
    tanggal = pyip.inputStr(prompt='Masukan Tanggal Transaksi (YYYY/MM/DD) : ', blockRegexes=[r'[a-zA-Z]'])
    jenis_transaksi = pyip.inputStr(prompt='Masukkan Jenis Transaksi : ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
    qty = pyip.inputInt(prompt='Masukan Qty Barang :', blockRegexes=[r'[a-zA-Z]'], greaterThan=0)

    # Loop item di dalam Stock_Card
    for key, value in Stock_Card.items():
        # Apabila transaksi sudah ada di dalam daftar
        if key == 'column':
            continue
        elif tanggal and jenis_transaksi in value:
            print('Transaksi sudah ada')
            break
    # Apabila transaksi tidak ada di dalam daftar
        else:    
            kode_barang = pyip.inputInt(prompt='Masukkan Kode Barang : ', greaterThan=0,blockRegexes=[r'[a-zA-Z]']) 
            harga = pyip.inputInt(prompt='Masukan Harga Barang :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=000)
            stock_balance = pyip.inputInt(prompt='Masukan Stock Balance :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=0)
            add = pyip.inputYesNo(prompt="\nIngin menambahkan data?(yes/no): ")
            if add == 'yes':
                index = len(Stock_Card) - 1
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

def Delete_SC():
    # Input indeks SC yang akan dihapus
    index = pyip.inputInt(prompt='Masukkan indeks Stock Card yang ingin dihapus: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
    # Menghapus buah berdasarkan indeks
    del Stock_Card[f'transaksi{index}']
    # Update indeks buah yang tersisa
    for key, value in Stock_Card.copy().items():
        if key != 'column' and value[0] > index:
            del Stock_Card[key]
            Stock_Card.update({
                f'transaksi{value[0] - 1}': [
                    value[0]-1, 
                    value[1], 
                    value[2], 
                    value[3],
                    value[4],
                    value[5],
                    value[6]
                    # value[7]
                    ]
                }
            )
    # Menampilkan daftar buah terbaru
    show_Tabel_SC(Stock_Card, Format_SC,titleSC)

def Update_Data_SC():
    tanggal = pyip.inputStr(prompt='Masukan Tanggal Transaksi (YYYY/MM/DD) : ', blockRegexes=[r'[a-zA-Z]'])
    jenis_transaksi = pyip.inputStr(prompt='Masukkan Jenis Transaksi : ', applyFunc=lambda x: x.capitalize(), blockRegexes=[r'[0-9]'])
    qty = pyip.inputInt(prompt='Masukan Qty Barang :', blockRegexes=[r'[a-zA-Z]'], greaterThan=0),
    kode_barang = pyip.inputInt(prompt='Masukkan Kode Barang : ', greaterThan=0,blockRegexes=[r'[a-zA-Z]']) 
    harga = pyip.inputInt(prompt='Masukan Harga Barang :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=000)
    stock_balance = pyip.inputInt(prompt='Masukan Stock Barang :', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=0)
    
    while True:
        prompt = "Masukkan angka menu yang ingin dijalankan:\n"
        ListMenu = [
            "1. Update Stock Terkini",
            "2. Update Stock card",
            "3. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
                    show_List_Barang(ListBarang, FuncFormat)
        elif response == '2':
            for key, value in Stock_Card.copy.items():
                if key == 'column':
                    continue
                elif jenis_transaksi in value:
                    Stock_Card[key][1] = tanggal
                    Stock_Card[key][2] = kode_barang
                    Stock_Card[key][3] = jenis_transaksi
                    Stock_Card[key][4] = qty
                    Stock_Card[key][5] = harga
                    Stock_Card[key][6] = stock_balance
                    break
                else:
                    continue
                    show_Tabel_SC(Stock_Card, Format_SC, titleSC)
        elif response == '3':
                    Main_Menu()    
    
    # for key, value in Stock_Card.copy.items():
    #     if key == 'column':
    #         continue
    #     elif jenis_transaksi in value:
    #         Stock_Card[key][1] = tanggal
    #         Stock_Card[key][2] = kode_barang
    #         Stock_Card[key][3] = jenis_transaksi
    #         Stock_Card[key][4] = qty
    #         Stock_Card[key][5] = harga
    #         Stock_Card[key][6] = stock_balance
    #         break
    #     else:
    #         continue
    # show_Tabel_SC(Stock_Card,Format_SC,titleSC)


if __name__ == '__main__':
    Stock_Card = {
        'column': ["Index", "Tanggal", "Kode Barang", "Jenis Transaksi", "Qty", "Harga", "Stock Balance"],
        'transaksi1': [0, '2023/01/01', 101, "Saldo Awal", 150, 2000, 150],
        'transaksi2': [1, '2023/01/01', 102, "Saldo Awal", 150, 20000, 150],
        'transaksi3': [2, '2023/01/01', 201, "Saldo Awal", 150, 5000, 150],
        'transaksi4': [3, '2023/01/01', 202, "Saldo Awal", 150, 8000, 150],
        'transaksi5': [4, '2023/01/05', 101, "Penjualan", 50, 2000, 100]        
    }
    
    titleSC = '\n Stock Card \n'
    Format_SC = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<20}"+ "{:<8}"+ "{:<10}" + "{:<15}"
    
    ListBarang = {
        'column': ["Index", "Kode Barang", "Nama Barang", "Jenis Barang", "Stock Terkini", "Level Stock"],
        'barang1': [0, 101, "Mie Instan", "Makanan", 100, "low stock"],
        'barang2': [1, 102, "Sereal", "Makanan", 150, "available"],
        'barang3': [2, 201, "Susu", "Minuman", 150, "available"],
        'barang4': [3, 202, "Kopi", "Minuman", 150, "available"],
    } # yang dibuat fungsi input hanya stock terkini trs level stock dibuat if

    FuncFormat = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<15}"+ "{:<15}"+ "{:<15}"
    Main_Menu()
