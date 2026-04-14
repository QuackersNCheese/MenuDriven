import os   # clear screen
from time import sleep

# *** clear the screen
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Menu:
    def __init__(self, title, option_list):
        self.title = title
        self.option_list = option_list

    # make a title header and display menu
    def banner(self): 
        print ('*' * 50)
        buff = (50 - (len(self.title) + 2)) // 2
        print('-' * buff + ' ' + self.title + ' ' + '-' * buff)
        print("-" * 50)
        margin = 16
        for index in range(len(self.option_list)):
            print(margin * ' ' + str(index + 1) + ') ' + self.option_list[index])
        print('-' * 24) 

    # *** Display Menu and return user selected menu number
    def select(self):      
        while True:
            clear()
            self.banner()
            try:
                answer = int(input("Please select a number: "))
                if answer < 1 or answer > len(self.option_list):
                    raise ValueError
                break
            except ValueError:
                print("\nOops!  That was not a valid number.")
                sleep(1)
            except Exception as e:
                print(e)
        return answer