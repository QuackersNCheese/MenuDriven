from menu import Menu, clear

def main():
    # Create menu lists
    MAIN = ("Login", "Practice Mode", "Perfomance Analysis", "Quit")
    LOGIN = ("Sign In", "New Account", "back to Main Menu")
    PRACTICE = ("Multiplication", "back to Main Menu")
    PERFORMANCE = ("Tables", "Graphs", "back to Main Menu")

    # Create menus
    main_menu = Menu("Main Menu", MAIN)
    login_menu = Menu("Login Menu", LOGIN)
    practice_menu = Menu("Practice Menu", PRACTICE)
    performance_menu = Menu("Performance Menu", PERFORMANCE)

    # Menu logic - program flow control
    while True:
        match(main_menu.select()):
            case 1:
                login_menu.select()
            case 2:
                practice_menu.select()
            case 3: 
                performance_menu.select()
            case 4:
                clear()
                print("Come back soon, Goodbye!\n")
                break
    print('-' * 50)
            
        
if __name__ == "__main__":
    main()