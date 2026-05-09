import os
from time import sleep, time
import random

# *** clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def circle_interview():
    quantity = 10
    difficulty = 1
    function_select = 2
    
    while True:
        #clear()
        print("You're about to practice remembering trigonometric values for common angles.")
        print("Just a few questions before we start... ")
        try:
            quantity = int(input("How many problems would you like in your drill? "))
            if quantity < 1 or quantity > 100:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    while True:
        print("Difficulty 1 will cover angles in quadrant one, level 2 will cover all four quadrants as positive angles.")
        print("Difficulty 3 will include negative angles.")
        try:
            difficulty = int(input("Choose difficulty on a scale of 1 to 3. "))
            if difficulty < 1 or difficulty > 3:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    while True:
        try:
            function_select = int(input("Basic sine cosine (2), include tangent (3) or all (6) trig functions? "))
            if function_select < 2 or function_select > 6 or function_select == 4 or function_select == 5:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    while True:
        try:
            rad_deg = int(input("Radians (1) or Degrees (2)? "))
            if rad_deg < 1 or rad_deg > 2:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid answer.")
            sleep(1)
        except Exception as e:
            print(e)           
    return quantity, difficulty, function_select, rad_deg

# *** create a list of test questions
def generate_circle_test(quantity, difficulty, function_select, rad_deg):
    sin = { '0': '0', '\u03c0/6': '1/2', '\u03c0/4': '1/\u221A2', '\u03c0/3': '\u221A3/2', '\u03c0/2': '1' }
    test_bank = []
    for i in range(quantity):
        angle = random.choice(['0', '\u03c0/6', '\u03c0/4', '\u03c0/3', '\u03c0/2'])
        print(angle, sin[angle])

    return test_bank
    #     op1 = random.randint(range_min, range_max)
    #     op2 = random.randint(range_min, range_max)
    #     while operator == '//' and (op2 == 0 or op1 % op2 != 0) or '%' and (op1 < 0 or op2 <=1):
    #         op1 = random.randint(range_min, range_max)
    #         op2 = random.randint(range_min, range_max)
    #     test_bank.append((op1, op2, operator))
    # return test_bank

def main():
    ## Testing Arithmetic
    # quant, rmin, rmax, operator = starting_interview()
    # test_bank = generate_test(quant, rmin, rmax, operator)
    # test_results = drill(test_bank)
    # print("** Problem List ***")
    # print("op1, op2, operator, is_correct, dt, time")
    # for test in test_results:
    #     print(test)

    # *** Testing binary
    #clear() 
    #quantity, bits = bin_terview()
    #bin_test_bank = bin_gen_test(quantity, bits)
    #for test in bin_test_bank:
    #    print(test)
    #print(bin_drill(bin_test_bank, bits))

    # *** Testing Unit Circle
    clear()
    #quant, diff, select, rad = circle_interview()
    #print(quant, diff, select, rad)
    print(generate_circle_test(10, 1, 2, 1))


if __name__ == "__main__":
    main()

