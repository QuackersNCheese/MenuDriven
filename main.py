from menu import Menu, clear, buff
from login import Account
from drill import starting_interview, generate_test, drill, bin_terview, bin_gen_test, bin_drill

def main():
    # Default user account
    this_account = Account()
    clear()
    print("*** You're doing drills! ***")
    this_account.set_user()

    # Create menu lists
    MAIN = ["Change Login", "Practice Mode", "Perfomance Analysis", "Quit"]
    LOGIN = ("Sign In", "New Account", "back to Main Menu")
    PRACTICE = ("Arithmetic", "Binary", "Unit Circle", "back to Main Menu")
    PERFORMANCE = ("Tables", "Graphs", "back to Main Menu")

    # Create menus
    main_menu = Menu("Main Menu", MAIN)
    login_menu = Menu("Login Menu", LOGIN)
    practice_menu = Menu("Practice Menu", PRACTICE)
    performance_menu = Menu("Performance Menu", PERFORMANCE)

    # Menu logic - program flow control
    while True:
        match(main_menu.select(this_account.get_username())):
            case 1:
                this_account.set_user()
            case 2:
                while True:
                    match(practice_menu.select(this_account.get_username())):
                        case 1:
                            buf = buff("Arithmetic")
                            print('-' * buf + ' ' + "Arithmetic" + ' ' + '-' * buf)
                            quant, rmin, rmax, operator = starting_interview()
                            test_bank = generate_test(quant, rmin, rmax, operator)
                            test_results = drill(test_bank)
                            this_account.save_test_results(test_results)
                            input("Press Enter to continue\n")
                        case 2:
                            buf = buff("Binary")
                            print('-' * buf + ' ' + "Binary" + ' ' + '-' * buf)
                            quantity, bits = bin_terview()
                            bin_test_bank = bin_gen_test(quantity, bits)
                            test_results = bin_drill(bin_test_bank, bits)
                            this_account.save_test_results(test_results)
                            input("Press Enter to continue\n")
                        case 3:  
                            buf = buff("Unit Circle")
                            print('-' * buf + ' ' + "Unit Circle" + ' ' + '-' * buf)
                            input("Press Enter to continue\n")
                        case 4:
                            break
                
            case 3: 
                while True:
                    match(performance_menu.select(this_account.get_username())):
                        case 1:
                            buf = buff("Tables")
                            print('-' * buf + ' ' + "Tables" + ' ' + '-' * buf)
                            all_test_results = this_account.load_user_history()
                            print("All Test Results")
                            print("op1 op2 operator is_correct dt time")
                            for record in all_test_results:
                                print(record)
                            input("Press Enter to continue\n")
                        case 2:
                            buf = buff("Graphs")
                            print('-' * buf + ' ' + "Graphs" + ' ' + '-' * buf)
                            input("Press Enter to continue\n")
                        case 3:
                            break
            case 4:
                clear()
                print("Come back soon, Goodbye!\n")
                break
    print('-' * 50)
            
        
if __name__ == "__main__":
    main()