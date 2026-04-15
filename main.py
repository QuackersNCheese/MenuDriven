from menu import Menu, clear, buff

def main():
    # Create menu lists
    MAIN = ("Login", "Practice Mode", "Perfomance Analysis", "Quit")
    LOGIN = ("Sign In", "New Account", "back to Main Menu")
    PRACTICE = ("Addition", "Subtraction", "Multiplication", "Integer Division", "back to Main Menu")
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
                while True:
                    match(login_menu.select()):
                        case 1:
                            buf = buff("Sign-in")
                            print('-' * buf + ' ' + "Sign-in" + ' ' + '-' * buf) #-----------------
                            input("Press any key\n")
                        case 2:
                            buf = buff("Create new login")
                            print('-' * buf + ' ' + "Create new login" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 3:
                            break

            case 2:
                while True:
                    match(practice_menu.select()):
                        case 1:
                            buf = buff("Addition")
                            print('-' * buf + ' ' + "Addition" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 2:
                            buf = buff("Subtraction")
                            print('-' * buf + ' ' + "Subtraction" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 3:
                            buf = buff("Multiplication")
                            print('-' * buf + ' ' + "Multiplication" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 4:  
                            buf = buff("Integer Division")
                            print('-' * buf + ' ' + "Integer Division" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 5:
                            break
                
            case 3: 
                while True:
                    match(performance_menu.select()):
                        case 1:
                            buf = buff("Tables")
                            print('-' * buf + ' ' + "Tables" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 2:
                            buf = buff("Graphs")
                            print('-' * buf + ' ' + "Graphs" + ' ' + '-' * buf)
                            input("Press any key\n")
                        case 3:
                            break
            case 4:
                clear()
                print("Come back soon, Goodbye!\n")
                break
    print('-' * 50)
            
        
if __name__ == "__main__":
    main()