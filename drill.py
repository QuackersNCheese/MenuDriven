import os
from time import sleep, time
import random

# *** clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# *** gather desired test conditions
def starting_interview():
    quantity = 0
    range_min = 0
    range_max = 0
    
    while True:
        #clear()
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
        try:
            range_min = int(input("What is the lowest number to use in your problems? "))
            if range_min < -1_000_000 or range_min > 1_000_000:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    while True:
        try:
            range_max = int(input("What is the highest number to use in your problems? "))
            if range_max < -1_000_000 or range_max > 1_000_000:
                raise ValueError
            if range_max <= range_min:
                raise ValueError("max must be greater than min")
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    while True:
        try:
            erator = input("what is the operation that you would like to practice? (+, -, *, //, %, mixed: ~) ")
            if erator not in ['+', '-', '*', '//', '%', '~']:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid answer.")
            sleep(1)
        except Exception as e:
            print(e)           
    return quantity, range_min, range_max, erator

# *** create a list of test questions
def generate_test(quantity, range_min, range_max, iterator):
    test_bank = []
    for i in range(quantity):
        if iterator == "~":
            operator = random.choice(['+', '-', '*', '//', '%'])
        else:
            operator = iterator
        op1 = random.randint(range_min, range_max)
        op2 = random.randint(range_min, range_max)
        while operator == '//' and (op2 == 0 or op1 % op2 != 0) or '%' and (op1 < 0 or op2 <=1):
            op1 = random.randint(range_min, range_max)
            op2 = random.randint(range_min, range_max)
        test_bank.append((op1, op2, operator))
    return test_bank

# *** run thru the test questions and return test results
def drill(test_bank):
    results = []
    total = len(test_bank)
    correct = 0
    t_total = 0

    clear()
    for test in test_bank:
        op1, op2, erator = test
        while True:
            try:
                start_time = time()
                answer = int(input(f"{op1} {erator} {op2} = "))
                dt = time() - start_time
                is_correct = answer == eval(str(op1) + erator + str(op2))
                if is_correct:
                     correct += 1
                results.append((op1, op2, erator, is_correct, dt, start_time))
                t_total += dt
                break
            except ValueError:
                print("\nOops!  That was not a valid answer.")
                sleep(1)
                clear()
            except Exception as e:
                print(e)
    print(f"You got {correct} out of {total} correct in {t_total:.2f} seconds.")
    print(f"That's {correct/total*100:.2f}% at a rate of {t_total/total:.2f} seconds per question.")
    return results

def bin_terview():
    quantity = 0
    bits = 0
    
    while True:
        #clear()
        print("You're about to do drills converting unsigned binary numbers to decimal.")
        print("Example: a 4 bit binary number 0b0010 is 2 in decimal or for convenience,")
        print("0010 = 2")
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
        try:
            bits = int(input("What is the number bits you would like to convert (I like 4)? "))
            if bits < 1 or bits > 64:
                raise ValueError
            break
        except ValueError:
            print("\nOops!  That was not a valid number.")
            sleep(1)
        except Exception as e:
            print(e)
    return quantity, bits

# *** create a list of binary test questions
def bin_gen_test(quantity, bits):
    test_bank = []
    for i in range(quantity):
        operator = 'dec_bin'
        op1 = random.randint(0, 2 ** (bits) - 1)
        op2 = bin(op1)
        test_bank.append((op1, op2, operator))
    return test_bank

# *** run thru the test questions and return test results
def bin_drill(test_bank, bits):
    results = []
    total = len(test_bank)
    correct = 0
    t_total = 0

    clear()
    for test in test_bank:
        dec_num, bin_str, erator = test
        while True:
            try:
                start_time = time()
                answer = int(input(f"{bin_str[2:].zfill(bits)} = "))
                dt = time() - start_time
                is_correct = answer == dec_num
                if is_correct:
                     correct += 1
                results.append((dec_num, bin_str, erator, is_correct, dt, start_time))
                t_total += dt
                break
            except ValueError:
                print("\nOops!  That was not a valid answer.")
                sleep(1)
                clear()
            except Exception as e:
                print(e)
    print(f"You got {correct} out of {total} correct in {t_total:.2f} seconds.")
    print(f"That's {correct/total*100:.2f}% at a rate of {t_total/total:.2f} seconds per question.")
    return results

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
    clear()
    quantity, bits = bin_terview()
    bin_test_bank = bin_gen_test(quantity, bits)
    for test in bin_test_bank:
        print(test)
    print(bin_drill(bin_test_bank, bits))


if __name__ == "__main__":
    main()
