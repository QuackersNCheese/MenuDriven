from menu import main_menu
from time import sleep

def main():
    while True:
        response = main_menu()
        match(response):
            case 1:
                print("Why, hello there!")
                break
            case _:
                print("\nThat is not an option.")
                sleep(3)
            
        
if __name__ == "__main__":
    main()