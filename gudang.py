import sys
import pyinputplus as pyip

def Main_Menu():
    global ListBarang
    global Stock_Card
    print(f'''
-------- Welcome to The Purwadhika Jogja Warehouse --------
    ''')
    # menginput fitur yang ingin ditampilkan 
    prompt = "Main Menu Options :\n"
    choice = ['Show menu', 'Update Transaction Data and Stock Card','Add Data Stock Card', 'Delete Data Stock Card', 'Exit']
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
    if len(Dict) == 0 or 'column' not in Dict.keys():
        print('\n---------- Data is Empty ------------')
    else:
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
    if len(Dict) == 0 or 'column' not in Dict.keys():
        print('\n---------- Data is Empty ------------')
    else:
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
        print('\n----------------------------------------------------------\nShow Menu Options :\n')
        prompt = "Input the number of the menu you want to run : "
        ListMenu = [
            "1. Status and Current Stock Items",
            "2. Stock Card (All Product)",
            "3. Back\n"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
            while True:
                print('\n----------------------------------------------------------\nCurrent Item Status and Stock Menu Options :\n')
                prompt = "Enter the number of the menu you want to run : "
                List_MenuSC = [
                    "1. Summary of stock items ",
                    "2. Stock by Barcode Product",
                    "3. Back"
                ]
                Tampilan_SubMenu_Utama(List_MenuSC)
                response = input(prompt)
                # Menampilkan All Stock Card
                if response == '1':
                    show_List_Barang(ListBarang, FuncFormat)
                # Mengecek Stock Card Berdasarkan Kode Barang
                elif response == '2':
                    print('----- Product Item Code Description -----\n \n101 = Instant Noodles\n102 = Cereal\n201 = Milk\n202 = Coffee\n')
                    while True:    
                    # meminta user input primary key
                        primary_key = pyip.inputInt(prompt='\nInput Product Item Code : ', blockRegexes=[r'[a-zA-Z]'], greaterThan=100)
                        if primary_key in ListBarang.keys():
                            print(FuncFormat.format("", *ListBarang['column']))
                            print(FuncFormat.format("", *ListBarang[primary_key]))
                            break
                        else:
                            print('Barcode does not exist. Please Try Again!')
                elif response == '3':
                    break
                else:
                    print('Data does not exist.')
        elif response == '2':
            show_Tabel_SC(Stock_Card,Format_SC,titleSC)
        elif response == '3':
            Main_Menu()
        else:
            print('Data does not exist.')

def Add_SC(): 
    while True:
        print('\n----------------------------------------------------------\nAdd Menu Options :\n')
        prompt = "Enter the number of the menu you want to run: \n"
        ListMenu = [
            "1. Add Stock Card Data",
            "2. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
        # update data stock card
            show_Tabel_SC(Stock_Card,Format_SC,titleSC)
            print('\nPlease complete the data below:')
            jenis_transaksi = pyip.inputStr(prompt='Enter Transaction Type (Sales or Purchase only): ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
        # Loop item di dalam Stock_Card
            transaksi_exist = False
            for key, value in Stock_Card.copy().items():
            # Apabila transaksi sudah ada di dalam daftar
                if key == 'column':
                    continue
                elif jenis_transaksi in value:
                    print('\n---------- TRANSACTION ALREADY EXISTS ----------')
                    transaksi_exist = True
                    break
            # Apabila transaksi tidak ada di dalam daftar
                if not transaksi_exist: 
                    tanggal = pyip.inputStr(prompt='Enter Transaction Date (YYYY/MM/DD): ', blockRegexes=[r'[a-zA-Z]'])
                    kode_barang = pyip.inputInt(prompt='Enter Item Code: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]']) 
                    harga = pyip.inputInt(prompt='Enter Item Price:', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=000)
                    qty = pyip.inputInt(prompt='Enter Item Qty:', blockRegexes=[r'[a-zA-Z]'], greaterThan=0, lessThan=value[-1])
                    print('\n----- How to calculate Stock Balance -----\n \nSales = Stock Balance - Qty(Sales)\nPurchase = Stock Balance + Qty(Purchase)\n')
                    stock_balance = pyip.inputInt(prompt='Stock Balance input:', blockRegexes= float and [r'[a-zA-Z]'], greaterThan=0)
                    add = pyip.inputYesNo(prompt="\nWant to add data? (yes/no): ")
                    if add == 'yes' or add == 'y':
                        index = len(Stock_Card)
                        Stock_Card.update({
                            f'transaksi{index}': [
                                index -1, 
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
            break
        elif response == '2':
            Main_Menu()

def Delete_SC(): 
    while True:
        print('\n----------------------------------------------------------\nDelete Menu Options :\n')
        prompt = "\nEnter the number of the menu you want to run: "
        ListMenu = [
            "1. Delete Transaction on Stock Card",
            "2. Delete All Transaction of Stock Card",
            "2. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenu)
        response = input(prompt)

        if response == '1':
            show_Tabel_SC(Stock_Card, Format_SC, titleSC)
            while True:
                index = int(input("\nEnter the transaction index that you want to delete: ")) 
                if index >= 0 and index < len(Stock_Card):
                    deleted_key = list(Stock_Card.keys())[index+1]
                    show_Tabel_SC(Stock_Card, Format_SC, titleSC, index)
                    confirm = pyip.inputYesNo(f"\nAre you sure you want to clear the transaction with the index {index}? (yes/no): ")
                    if confirm == 'yes':
                        del Stock_Card[deleted_key]
                        print('\n-------- DATA SUCCESSFULLY DELETED --------')
                        show_Tabel_SC(Stock_Card,Format_SC,titleSC)  # Show updated table after deletion
                    else:
                        print('Transaction deletion is canceled.')
                    break
                else:
                    print('Invalid transaction index. Please try again!')

        elif response == '2':
            show_Tabel_SC(Stock_Card,Format_SC,titleSC)
            delete = pyip.inputYesNo(prompt='Do you want to delete all? (yes/no)')
            if delete == 'yes':
                for key in Stock_Card.copy().keys():
                    if key == 'column':
                        continue
                    del Stock_Card[key]
                print('\n-------- ALL DATA SUCCESSFULLY DELETED --------')
                show_Tabel_SC(Stock_Card,Format_SC,titleSC)
                Main_Menu()
                break
        elif response == '3':
            break
        else:
            print('The number entered is not in the List Menu. Please try again!')
            continue

def Update_Data_SC():
    while True:
        print('\n------------- Menu Data Update  -----------')
        prompt = "Enter the number of the menu you want to run : "
        print('\nWhich data do you want to change? ')
        ListMenuUtama_Update = [
            "1. Update Current Stock",
            "2. Update Stock card",
            "3. Back"
        ]
        Tampilan_SubMenu_Utama(ListMenuUtama_Update)
        response = input(prompt)

        if response == '1':
            # menampilkan data terkini
            show_List_Barang(ListBarang, FuncFormat)                  
            while True:    
            # meminta user input primary key
                primary_key = pyip.inputInt(prompt='\nEnter Item Code : ', blockRegexes=[r'[a-zA-Z]'], greaterThan=100)
                if primary_key in ListBarang.keys():
                    print(FuncFormat.format("", *ListBarang['column']))
                    print(FuncFormat.format("", *ListBarang[primary_key]))
                    break
                else:
                    print('Barcode does not exist. Please Try Again!')
                # konfirmasi apakah yakin data ini yang akan di update
            while True:
                update = pyip.inputYesNo(prompt="\nWant to change the data on this item code? (yes/no): ")
                if update == 'yes':
                # meminta inputan kolom mana yang akan di update
                    while True:
                        prompt = "\nEnter the number of the column menu you want to run: "
                        print('\nList of data fields that you can modify: ')
                        ListMenu1 = [
                                "1. Current Stock",
                                "2. Level of Stock",
                                "3. Back"
                            ]
                        Tampilan_SubMenu_Utama(ListMenu1)
                        response = input(prompt)
                # meminta value terbaru yang akan diubah
                        if response == '1':
                            while True:
                                live_stock = pyip.inputInt(prompt='Enter the latest stock quantity: ', blockRegexes=[r'[a-zA-Z]'], greaterThan=0)
                                make_sure = pyip.inputYesNo(prompt='Want to Change this Current Stock? (yes/no): ')
                                if make_sure == 'yes':
                                    for key, value in ListBarang.items():
                                        if key == 'column':
                                            continue
                                        elif primary_key in value:
                                            value[4] = live_stock
                                            break
                                        else: 
                                            continue
                                    show_List_Barang(ListBarang,FuncFormat)                             
                                    print('\n-------- DATA SUCCESSFULLY UPDATED --------')
                                    break
                                else:
                                    break 
                        elif response == '2':
                            while True:
                                print('\n----- Stock Level Description -----\n \n     Low Stock = Current Stock <= 150\n     Availabel = Current Stock >150\n')
                                level_stock = pyip.inputStr(prompt='Enter Current Stock Level:', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
                                make_sure = pyip.inputYesNo(prompt='Want to Change this Stock Level?(yes/no): ')
                                if make_sure == 'yes':
                                    for key, value in ListBarang.items():
                                        if key == 'column':
                                            continue
                                        elif primary_key in value:
                                            value[5] = level_stock
                                            break
                                    print('\n-------- DATA SUCCESSFULLY UPDATED --------')
                                    show_List_Barang(ListBarang, FuncFormat)
                                    break
                                else:
                                    break
                        elif response == '3':
                            continue
                        else:
                            print('Menu options not available')
                else:
                    Main_Menu()
        elif response == '2':  
            show_Tabel_SC(Stock_Card, Format_SC,titleSC)
            # meminta user input index
            index_update = pyip.inputInt(prompt='\nEnter the Stock Card Index that you want to change:', blockRegexes=[r'[a-zA-Z]'])
            key_update = check(Stock_Card,index_update)
            print(key_update)
            if key_update != "":
                show_Tabel_SC(Stock_Card, Format_SC, titleSC, index_update)
                update = pyip.inputYesNo(prompt="\nWant to change the data on this item code? (yes/no): ")
                if update == 'yes':
                    tanggal = pyip.inputStr(prompt='Enter the Transaction Date (YYYY/MM/DD):', blockRegexes=[r'[a-zA-Z]'])
                    kode_barang = pyip.inputInt(prompt='Enter Item Code : ',greaterThan=100, blockRegexes=[r'[a-zA-Z]'])
                    for j, val in enumerate(Stock_Card.values()):
                        if kode_barang in val:
                            print('\n----- Transaction Type -----\n \nBeginning balance\nSales \nPurchase \n')
                            jenis_transaksi = pyip.inputStr(prompt='Enter Transaction Type : ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
                            harga = pyip.inputInt(prompt='Enter Item Price: ', greaterThan=0)
                            qty = pyip.inputInt(prompt='Enter Item Qty: ', greaterThan=0)
                            stock_balance = pyip.inputInt(prompt='Enter Stock Balance: ', greaterThan=0)
                            Stock_Card[key_update][1] = tanggal
                            Stock_Card[key_update][2] = kode_barang
                            Stock_Card[key_update][3] = jenis_transaksi
                            Stock_Card[key_update][4] = qty
                            Stock_Card[key_update][5] = harga
                            Stock_Card[key_update][6] = stock_balance
                            print('\n-------- DATA UPDATED SUCCESSFULLY --------')
                            show_Tabel_SC(Stock_Card, Format_SC,titleSC)
                            break
                        elif j == len(Stock_Card) - 1:
                            print('Kode barang tidak tersedia')
                            continue
                else:
                    break
        elif response == '3':
            Main_Menu() 
        else:
            print('Menu options not available')   

def check(database,val):
    key_update = ""
    for key, value in database.items():
        if key == 'column':
            continue
        elif val in value:
            key_update = key
            break
    return key_update

if __name__ == '__main__':
    # Path CSV
    
    # check database, if empty display a message
    
    Stock_Card = {
        'column': ["Index", "Date", "Item Code", "Type of Transaction", "Qty", "Price", "Stock Balance"],
        'transaksi1': [0, '2023/01/01', 101, "Beginning Balance", 150, 2000, 150],
        'transaksi2': [1, '2023/01/01', 102, "Beginning balance", 150, 20000, 150],
        'transaksi3': [2, '2023/01/01', 201, "Beginning balance", 150, 5000, 150],
        'transaksi4': [3, '2023/01/01', 202, "Beginning balance", 150, 8000, 150],
        'transaksi5': [4, '2023/01/05', 101, "Sales", 50, 2000, 100]
    }
    
    titleSC = '\n--------------- Stock Card ---------------'
    Format_SC = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<25}"+ "{:<8}"+ "{:<10}" + "{:<15}"
    
    ListBarang = {
        'column': ["Index", "Item Code", "Name of Item", "Type of Item", "Current Stock", "Level of Stock"],
        101: [0, 101, "Mie Instan", "Makanan", 100, "Low Stock"],
        102: [1, 102, "Sereal", "Makanan", 150, "Available"],
        201: [2, 201, "Susu", "Minuman", 150, "Available"],
        202: [3, 202, "Kopi", "Minuman", 150, "Available"],
    } 

    FuncFormat = "{:<4}" + "{:<8}" + "{:<15}" + "{:<15}" + "{:<15}"+ "{:<15}"+ "{:<15}"
    Main_Menu()




