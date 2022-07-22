import PySimpleGUI as sg    # to open a new window
import os.path              # python's os module
import random               # random number generator
############################### class
class Main_menu:
    def main_main_menu():
        run = 1
        while run == 1:
            Main_menu.print_menu()
            selection = Main_menu.get_menu_selection()
            Main_menu.exec_menu(selection)

    def print_menu():
        print("Yo! Welcome to Help-Me-Decide!\n" + 
            "\nYour options are: \n" + 
            " 1. Computer, decide for me please!\n" +
            " 2. Wait can I add more to the pool?\n" + 
            " 3. Let's see what do we have here...\n" + 
            " 4. Okay, I'm done. Can I leave now?\n")
    
    def get_menu_selection():
        return input("Enter your selection: ")
    
    def exit_program():
        print("\nSee you next time!\n")
        exit()

    def exec_menu(selection):
        if selection == "1":
            Main_menu.get_random_from_saved()
        elif selection == "2":
            return
        elif selection == "3":
            return
        elif selection == "4":
            Main_menu.exit_program()
        else:
            print("Invalid selection. Please try again.\n")
        
    def get_random_from_saved():
        saved = ["Thai Kitchen", "Taste Place"]
        print(random.choice(saved))


############################### main menu
Main_menu.main_main_menu()

