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
`To run the "Show Menu" option in the main menu, you need to follow these steps:
    - Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
            In the main menu: 
            1. "Show menu," 
            2. "Update Transaction Data and Stock Card," 
            3. "Add Data Stock Card,"
            4. "Delete Data Stock Card",
            5. "Exit".
        - The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice.
        - If the `response` == "1"
            Will be show:
                1. Status and Current Stock Items
                2. Stock Card (All Product)
                3. Back
        - If the `response` doesn't match any of the available choices, an appropriate message is displayed to the user.
        - After executing the corresponding action, the control returns to the sub-menu, and the user is again prompted for a choice.
        - The process continues until the user selects the "Back" option in the sub-menu, which returns control to the main menu.
        - This process continues until the user selects the "Exit" option in the main menu, which terminates the program.

2. Update Transaction Data and Stock Card
`To run the "Update Transaction Data and Stock Card" option in the main menu, you need to follow these steps:
    - Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
    - The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. 
    - Once the user selects an option, the chosen option is stored in the `response` variable.
    - If the `response` matches the second choice, which is "Update Transaction Data and Stock Card," the `Update_Data_SC()` function is called.
    - The `Update_Data_SC()` function prompts the user to enter the transaction details.
    - The function validates the input and checks if the item code exists in the `ListBarang` dictionary. 
       If the code is valid and the item exists, the transaction details are added to the corresponding item's transaction list.
    - Additionally, the stock card record is updated with the transaction details, including the transaction ID, date, quantity, and transaction type.
    - After updating the transaction data and stock card, the control returns to the main menu, and the user is again prompted for a choice.
  
3. Add Data Stock Card 
To run the "Add Data Stock Card" option in the main menu, you can follow these steps:
        - Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        - The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. 
        - Once the user selects an option, the chosen option is stored in the `response` variable.
        - If the `response` matches the third choice, which is "Add Data Stock Card," the `Add_SC()` function is called.
        - The `Add_SC()` function prompts the user to enter the item code, item name, and initial stock quantity.
        - The function then checks if the item code already exists in the `ListBarang` dictionary. 
           If the code exists, it displays an error message and prompts the user to enter a unique item code.
        - If the item code is unique, 
           The function adds a new entry to the `ListBarang` dictionary:
           the item code as the key and a list containing the item name, initial stock quantity, and an empty transaction list as the value.
        - After successfully adding the data to the stock card, the control returns to the main menu, and the user is again prompted for a choice.

4. Delete Data Stock Card
To run the "Delete Data Stock Card" option in the main menu, you can follow these steps:`
        - Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        - The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice. 
        - Once the user selects an option, the chosen option is stored in the `response` variable.
        - If the `response` matches the fourth choice, which is "Delete Data Stock Card," the `Delete_SC()` function is called.
        - The `Delete_SC()` function prompts the user to enter the item code of the stock card they want to delete.
        - The function then checks if the item code exists in the `ListBarang` dictionary. 
            If the code does not exist, it displays an error message and prompts the user to enter a valid item code.
        - If the item code is valid and exists in the dictionary, the function removes the corresponding entry from the `ListBarang` dictionary.
        - After successfully deleting the data from the stock card, the control returns to the main menu, and the user is again prompted for a choice.

5. Exit

    `To run the "Exit" option in the main menu, you can follow these steps:
        - Execute the `Main_Menu()` function. This function displays the main menu options to the user and prompts for a choice.
        - The `pyip.inputMenu()` function is used to present the menu options to the user and receive their choice.
        - Once the user selects an option, the chosen option is stored in the `response` variable.
        - The `response` is then compared with each available choice using an if-else ladder to determine which action to perform.
        - If the `response` matches the last choice, which is "Exit," the program execution is terminated using the `sys.exit()` function. 
            This function stops the program and exits to the operating system.


## Contribute

If you would like to contribute to warehouse, check out https://github.com/Khanzky/capstone_project.git 

