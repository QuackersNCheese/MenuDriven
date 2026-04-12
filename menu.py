import os   # clear screen
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_display():
    print("1) Hello!")
    print()

def main_menu():
    clear()
    while True:
        menu_display()
        try:
            answer = int(input("Please select a number: "))
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(3)
            clear()
        except Exception as e:
            print(e)
    return answer