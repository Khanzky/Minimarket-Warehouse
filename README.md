# Purwadhika Jogja Minimarket Warehouse

A simple application with the python programming language used by Purwadhika Jogja Minimarket Warehouse
to check, change, add, and delete stock data and stock card reports.


## Installastion

To clone from github, run:
    mkdir folder
    cd folder
    git clone git@github.com:Khanzky/capstone_project.git
To install requitment with pip, run:
    pip install -r requitment.txt

## Quickstart Guide

1. Show Menu
    To run the "Show Menu" option in the main menu, you need to follow these steps:
        1. Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        2. The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. It takes the prompt message and a list of choices as parameters.
        3. Once the user selects an option, the chosen option is stored in the `response` variable.
        4. The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        5. If the `response` matches the first choice, which is "Show menu," the `Sub_Menu()` function is called.
        6. The `Sub_Menu()` function displays the sub-menu options to the user and prompts for a choice.
        7. Similar to the main menu, the user's choice is stored in the `response` variable.
        8. The `response` is again compared with each available choice using an if-else ladder to determine the corresponding action.
        9. If the `response` matches the first choice, which is "Summary of stock items," the `show_List_Barang()` function is called to display the list of available items.
        10. If the `response` matches the second choice, which is "Stock by Barcode Product," the user is prompted to enter the product item code. The code is then validated, and if it exists in the `ListBarang` dictionary, the corresponding item's details are displayed using the `FuncFormat` format string.
        11. If the `response` matches the third choice, which is "Back," the function breaks the loop and returns to the main menu.
        12. If the `response` doesn't match any of the available choices, an appropriate message is displayed to the user.
        13. After executing the corresponding action, the control returns to the sub-menu, and the user is again prompted for a choice.
        14. The process continues until the user selects the "Back" option in the sub-menu, which returns control to the main menu.
        15. In the main menu, if the user selects any option other than "Show menu," such as "Update Transaction Data and Stock Card," "Add Data Stock Card," or "Exit," the corresponding functions (`Update_Data_SC()`, `Add_SC()`, `Delete_SC()`, or `sys.exit()`) are called to perform the desired action.
        16. This process continues until the user selects the "Exit" option in the main menu, which terminates the program.

2. Update Transaction Data and Stock Card
        To run the "Update Transaction Data and Stock Card" option in the main menu, you need to follow these steps:
        1. Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        2. The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. It takes the prompt message and a list of choices as parameters.
        3. Once the user selects an option, the chosen option is stored in the `response` variable.
        4. The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        5. If the `response` matches the second choice, which is "Update Transaction Data and Stock Card," the `Update_Data_SC()` function is called.
        6. The `Update_Data_SC()` function prompts the user to enter the transaction details, such as the transaction ID, date, item code, quantity, and type of transaction (e.g., "In" for incoming, "Out" for outgoing).
        7. The function validates the input and checks if the item code exists in the `ListBarang` dictionary. If the code is valid and the item exists, the transaction details are added to the corresponding item's transaction list.
        8. Additionally, the stock card record is updated with the transaction details, including the transaction ID, date, quantity, and transaction type.
        9. After updating the transaction data and stock card, the control returns to the main menu, and the user is again prompted for a choice.
        10. If the user selects any option other than "Update Transaction Data and Stock Card," such as "Show Menu," "Add Data Stock Card," or "Exit," the corresponding functions (`Sub_Menu()`, `Add_SC()`, `Delete_SC()`, or `sys.exit()`) are called to perform the desired action.
        11. This process continues until the user selects the "Exit" option in the main menu, which terminates the program.

3. Add Data Stock Card 
        To run the "Add Data Stock Card" option in the main menu, you can follow these steps:
        1. Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        2. The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. It takes the prompt message and a list of choices as parameters.
        3. Once the user selects an option, the chosen option is stored in the `response` variable.
        4. The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        5. If the `response` matches the third choice, which is "Add Data Stock Card," the `Add_SC()` function is called.
        6. The `Add_SC()` function prompts the user to enter the item code, item name, and initial stock quantity.
        7. The function then checks if the item code already exists in the `ListBarang` dictionary. If the code exists, it displays an error message and prompts the user to enter a unique item code.
        8. If the item code is unique, the function adds a new entry to the `ListBarang` dictionary with the item code as the key and a list containing the item name, initial stock quantity, and an empty transaction list as the value.
        9. After successfully adding the data to the stock card, the control returns to the main menu, and the user is again prompted for a choice.
        10. If the user selects any option other than "Add Data Stock Card," such as "Show Menu," "Update Transaction Data and Stock Card," or "Exit," the corresponding functions (`Sub_Menu()`, `Update_Data_SC()`, or `sys.exit()`) are called to perform the desired action.
        11. This process continues until the user selects the "Exit" option in the main menu, which terminates the program.

4. Delete Data Stock Card
        To run the "Delete Data Stock Card" option in the main menu, you can follow these steps:
        1. Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        2. The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. It takes the prompt message and a list of choices as parameters.
        3. Once the user selects an option, the chosen option is stored in the `response` variable.
        4. The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        5. If the `response` matches the fourth choice, which is "Delete Data Stock Card," the `Delete_SC()` function is called.
        6. The `Delete_SC()` function prompts the user to enter the item code of the stock card they want to delete.
        7. The function then checks if the item code exists in the `ListBarang` dictionary. If the code does not exist, it displays an error message and prompts the user to enter a valid item code.
        8. If the item code is valid and exists in the dictionary, the function removes the corresponding entry from the `ListBarang` dictionary.
        9. After successfully deleting the data from the stock card, the control returns to the main menu, and the user is again prompted for a choice.
        10. If the user selects any option other than "Delete Data Stock Card," such as "Show Menu," "Update Transaction Data and Stock Card," or "Exit," the corresponding functions (`Sub_Menu()`, `Update_Data_SC()`, or `sys.exit()`) are called to perform the desired action.
        11. This process continues until the user selects the "Exit" option in the main menu, which terminates the program. 

5. Exit
        To run the "Exit" option in the main menu, you can follow these steps:
        1. Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        2. The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. It takes the prompt message and a list of choices as parameters.
        3. Once the user selects an option, the chosen option is stored in the `response` variable.
        4. The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        5. If the `response` matches the last choice, which is "Exit," the program execution is terminated using the `sys.exit()` function. This function stops the program and exits to the operating system.
        6. If the user selects any other option, such as "Show Menu," "Update Transaction Data and Stock Card," or "Add Data Stock Card," the corresponding functions (`Sub_Menu()`, `Update_Data_SC()`, or `Add_Data_SC()`) are called to perform the desired action.
        7. This process continues until the user selects the "Exit" option in the main menu, at which point the program will terminate and exit.

        Note: Make sure to import the `sys` module at the beginning of your code to use the `sys.exit()` function.


## Contribute

If you would like to contribute to warehouse, check out https://github.com/Khanzky/capstone_project.git 

