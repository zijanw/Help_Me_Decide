import PySimpleGUI as gui   # to open a new window
import os.path              # python's os module
import random               # random number generator


############################### class
class Main_menu:

    # main
    def main_main_menu():
        # run forever until user quits
        while True:
            Main_menu.print_menu()
            selection = Main_menu.get_menu_selection()
            Main_menu.exec_menu(selection)

    # print main menu
    def print_menu():
        print("Yo! Welcome to Help-Me-Decide!\n" + 
            "\nYour options are: \n" + 
            " 1. Computer, decide for me please!\n" +
            " 2. Wait can I add more to the list?\n" + 
            " 3. Help me recall what I had...\n" + 
            " 4. Okay, I'm done. Can I leave now?\n")
    
    # get input from user
    def get_menu_selection():
        return input("Enter your selection: ")
    
    # quit program
    def exit_program():
        print("\nSee you next time!\n")
        exit()

    # execute methods based on user input
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
        
    # randomize from pool
    def get_random_from_saved():
        saved = ["Thai Kitchen", "Taste Place"]
        print("\nThe decision is......\n" + 
            random.choice(saved) + "!!!\n")

############################### main menu
layout = [[gui.Text(Main_menu.print_menu())], [gui.Button("OK")]]
window = gui.Window("Help-Me-Decide!", layout, margins = (250, 100))

while True:
    event, values = window.read()
    #Main_menu.main_main_menu()

    if event == "OK" or event == gui.WIN_CLOSED:
        break

window.close()
