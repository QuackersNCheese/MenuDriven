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
# \u03c0 is pi
# \u221A is the root symbol
# \u00b0 is the degree symbol
def generate_circle_test(quantity, difficulty, function_select, rad_deg):
    sin = { '-2\u03c0': '0', '-11\u03c0/6': '1/2', '-7\u03c0/4': '1/\u221A2', '-5\u03c0/3': '\u221A3/2', '-3\u03c0/2': '1', '-4\u03c0/3': '\u221A3/2', '-5\u03c0/4': '1/\u221A2', '-7\u03c0/6': '1/2', '-\u03c0': '0', '-5\u03c0/6': '-1/2', '-3\u03c0/4': '-1/\u221A2', '-2\u03c0/3': '-\u221A3/2', '-\u03c0/2': '-1', '-\u03c0/3': '-\u221A3/2', '-\u03c0/4': '-1/\u221A2', '-\u03c0/6': '-1/2', '0': '0', '\u03c0/6': '1/2', '\u03c0/4': '1/\u221A2', '\u03c0/3': '\u221A3/2', '\u03c0/2': '1', '2\u03c0/3': '\u221A3/2', '3\u03c0/4': '1/\u221A2', '5\u03c0/6': '1/2', '\u03c0': '0', '7\u03c0/6': '-1/2', '5\u03c0/4': '-1/\u221A2', '4\u03c0/3': '-\u221A3/2', '3\u03c0/2': '-1', '5\u03c0/3': '-\u221A3/2', '7\u03c0/4': '-1/\u221A2', '11\u03c0/6': '-1/2', '2\u03c0': '0' }
    cos = { '-2\u03c0': '1', '-11\u03c0/6': '\u221A3/2', '-7\u03c0/4': '1/\u221A2', '-5\u03c0/3': '1/2', '-3\u03c0/2': '0', '-4\u03c0/3': '-1/2', '-5\u03c0/4': '-1/\u221A2', '-7\u03c0/6': '-\u221A3/2', '-\u03c0': '-1', '-5\u03c0/6': '-\u221A3/2', '-3\u03c0/4': '-1/\u221A2', '-2\u03c0/3': '-1/2', '-\u03c0/2': '0', '-\u03c0/3': '1/2', '-\u03c0/4': '1/\u221A2', '-\u03c0/6': '\u221A3/2', '0': '1', '\u03c0/6': '\u221A3/2', '\u03c0/4': '1/\u221A2', '\u03c0/3': '1/2', '\u03c0/2': '0', '2\u03c0/3': '-1/2', '3\u03c0/4': '-1/\u221A2', '5\u03c0/6': '-\u221A3/2', '\u03c0': '-1', '7\u03c0/6': '-\u221A3/2', '5\u03c0/4': '-1/\u221A2', '4\u03c0/3': '-1/2', '3\u03c0/2': '0', '5\u03c0/3': '1/2', '7\u03c0/4': '1/\u221A2', '11\u03c0/6': '\u221A3/2', '2\u03c0': '1' }
    tan = { '-2\u03c0': '0', '-11\u03c0/6': '1/\u221A3', '-7\u03c0/4': '1', '-5\u03c0/3': '\u221A3', '-3\u03c0/2': 'dne', '-4\u03c0/3': '-\u221A3', '-5\u03c0/4': '-1', '-7\u03c0/6': '-1/\u221A3', '-\u03c0': '0', '-5\u03c0/6': '1/\u221A3', '-3\u03c0/4': '1', '-2\u03c0/3': '\u221A3', '-\u03c0/2': 'dne', '-\u03c0/3': '-\u221A3', '-\u03c0/4': '-1', '-\u03c0/6': '-1/\u221A3', '0': '0', '\u03c0/6': '1/\u221A3', '\u03c0/4': '1', '\u03c0/3': '\u221A3', '\u03c0/2': 'dne', '2\u03c0/3': '-\u221A3', '3\u03c0/4': '-1', '5\u03c0/6': '-1/\u221A3', '\u03c0': '0', '7\u03c0/6': '1/\u221A3', '5\u03c0/4': '1', '4\u03c0/3': '\u221A3', '3\u03c0/2': 'dne', '5\u03c0/3': '-\u221A3', '7\u03c0/4': '-1', '11\u03c0/6': '-1/\u221A3', '2\u03c0': '0' }
    csc = { '-2\u03c0': 'dne', '-11\u03c0/6': '2', '-7\u03c0/4': '\u221A2', '-5\u03c0/3': '2/\u221A3', '-3\u03c0/2': '1', '-4\u03c0/3': '2/\u221A3', '-5\u03c0/4': '\u221A2', '-7\u03c0/6': '2', '-\u03c0': 'dne', '-5\u03c0/6': '-2', '-3\u03c0/4': '-\u221A2', '-2\u03c0/3': '-2/\u221A3', '-\u03c0/2': '-1', '-\u03c0/3': '-2/\u221A3', '-\u03c0/4': '-\u221A2', '-\u03c0/6': '-2', '0': 'dne', '\u03c0/6': '2', '\u03c0/4': '\u221A2', '\u03c0/3': '2/\u221A3', '\u03c0/2': '1', '2\u03c0/3': '2/\u221A3', '3\u03c0/4': '\u221A2', '5\u03c0/6': '2', '\u03c0': 'dne', '7\u03c0/6': '-2', '5\u03c0/4': '-\u221A2', '4\u03c0/3': '-2/\u221A3', '3\u03c0/2': '-1', '5\u03c0/3': '-2/\u221A3', '7\u03c0/4': '-\u221A2', '11\u03c0/6': '-2', '2\u03c0': 'dne' }
    sec = { '-2\u03c0': '1', '-11\u03c0/6': '2/\u221A3', '-7\u03c0/4': '\u221A2', '-5\u03c0/3': '2', '-3\u03c0/2': 'dne', '-4\u03c0/3': '-2', '-5\u03c0/4': '-\u221A2', '-7\u03c0/6': '-2/\u221A3', '-\u03c0': '-1', '-5\u03c0/6': '-2/\u221A3', '-3\u03c0/4': '-\u221A2', '-2\u03c0/3': '-2', '-\u03c0/2': 'dne', '-\u03c0/3': '2', '-\u03c0/4': '\u221A2', '-\u03c0/6': '2/\u221A3', '0': '1', '\u03c0/6': '2/\u221A3', '\u03c0/4': '\u221A2', '\u03c0/3': '2', '\u03c0/2': 'dne', '2\u03c0/3': '-2', '3\u03c0/4': '-\u221A2', '5\u03c0/6': '-2/\u221A3', '\u03c0': '-1', '7\u03c0/6': '-2/\u221A3', '5\u03c0/4': '-\u221A2', '4\u03c0/3': '-2', '3\u03c0/2': 'dne', '5\u03c0/3': '2', '7\u03c0/4': '\u221A2', '11\u03c0/6': '2/\u221A3', '2\u03c0': '1' }
    cot = { '-2\u03c0': 'dne', '-11\u03c0/6': '\u221A3', '-7\u03c0/4': '1', '-5\u03c0/3': '1/\u221A3', '-3\u03c0/2': '0', '-4\u03c0/3': '-1/\u221A3', '-5\u03c0/4': '-1', '-7\u03c0/6': '-\u221A3', '-\u03c0': 'dne', '-5\u03c0/6': '\u221A3', '-3\u03c0/4': '1', '-2\u03c0/3': '1/\u221A3', '-\u03c0/2': '0', '-\u03c0/3': '-1/\u221A3', '-\u03c0/4': '-1', '-\u03c0/6': '-\u221A3', '0': 'dne', '\u03c0/6': '\u221A3', '\u03c0/4': '1', '\u03c0/3': '1/\u221A3', '\u03c0/2': '0', '2\u03c0/3': '-1/\u221A3', '3\u03c0/4': '-1', '5\u03c0/6': '-\u221A3', '\u03c0': 'dne', '7\u03c0/6': '\u221A3', '5\u03c0/4': '1', '4\u03c0/3': '1/\u221A3', '3\u03c0/2': '0', '5\u03c0/3': '-1/\u221A3', '7\u03c0/4': '-1', '11\u03c0/6': '-\u221A3', '2\u03c0': 'dne' }
    test_bank = []
    for i in range(quantity):
        op_num = random.randint(1, function_select)
        match(difficulty):
            case 1:
                angle = random.choice(['0', '\u03c0/6', '\u03c0/4', '\u03c0/3', '\u03c0/2'])
            case 2:
                angle = random.choice(['0', '\u03c0/6', '\u03c0/4', '\u03c0/3', '\u03c0/2', '2\u03c0/3', '3\u03c0/4', '5\u03c0/6', '\u03c0', '7\u03c0/6', '5\u03c0/4', '4\u03c0/3', '3\u03c0/2', '5\u03c0/3', '7\u03c0/4', '11\u03c0/6', '2\u03c0'])
            case 3:
                angle = random.choice(['-2\u03c0', '-11\u03c0/6', '-7\u03c0/4', '-5\u03c0/3', '-3\u03c0/2', '-4\u03c0/3', '-5\u03c0/4', '-7\u03c0/6', '-\u03c0', '-5\u03c0/6', '-3\u03c0/4', '-2\u03c0/3', '-\u03c0/2', '-\u03c0/3', '-\u03c0/4', '-\u03c0/6', '0', '\u03c0/6', '\u03c0/4', '\u03c0/3', '\u03c0/2', '2\u03c0/3', '3\u03c0/4', '5\u03c0/6', '\u03c0', '7\u03c0/6', '5\u03c0/4', '4\u03c0/3', '3\u03c0/2', '5\u03c0/3', '7\u03c0/4', '11\u03c0/6', '2\u03c0'])
        rad_to_degree = { '-2\u03c0': '-360\u00b0', '-11\u03c0/6': '-330\u00b0', '-7\u03c0/4': '-315\u00b0', '-5\u03c0/3': '-300\u00b0', '-3\u03c0/2': '-270\u00b0', '-4\u03c0/3': '-240\u00b0', '-5\u03c0/4': '-225\u00b0', '-7\u03c0/6': '-210\u00b0', '-\u03c0': '-180\u00b0', '-5\u03c0/6': '-150\u00b0', '-3\u03c0/4': '-135\u00b0', '-2\u03c0/3': '-120\u00b0', '-\u03c0/2': '-90\u00b0', '-\u03c0/3': '-60\u00b0', '-\u03c0/4': '-45\u00b0', '-\u03c0/6': '-30\u00b0', '0': '0\u00b0', '\u03c0/6': '30\u00b0', '\u03c0/4': '45\u00b0', '\u03c0/3': '60\u00b0', '\u03c0/2': '90\u00b0', '2\u03c0/3': '120\u00b0', '3\u03c0/4': '135\u00b0', '5\u03c0/6': '150\u00b0', '\u03c0': '180\u00b0', '7\u03c0/6': '210\u00b0', '5\u03c0/4': '225\u00b0', '4\u03c0/3': '240\u00b0', '3\u03c0/2': '270\u00b0', '5\u03c0/3': '300\u00b0', '7\u03c0/4': '315\u00b0', '11\u03c0/6': '330\u00b0', '2\u03c0': '360\u00b0'}
        degree = rad_to_degree[angle]
        ang = angle if rad_deg == 1 else degree
        match(op_num):
            case 1:
                test_bank.append((ang, sin[angle], 'sin'))
            case 2:
                test_bank.append((ang, cos[angle], 'cos'))
            case 3:
                test_bank.append((ang, tan[angle], 'tan'))
            case 4:
                test_bank.append((ang, csc[angle], 'csc'))
            case 5:
                test_bank.append((ang, sec[angle], 'sec'))
            case 6:
                test_bank.append((ang, cot[angle], 'cot'))

    return test_bank

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
    print(generate_circle_test(20, 1, 2, 2))


if __name__ == "__main__":
    main()

