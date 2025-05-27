print("\033[92mA PROGRAM THAT HANDLES ERRORS!\n\033[0m")
inf_bool = True
while inf_bool == True:
    try: 
        num1 = int(input("Enter the first number: "))
        inf_bool = False
    except:
        print("\033[91mPlease enter a digit!\033[0m")
inf_bool2 = True 
while inf_bool2 == True:
    try:
        num2 = int(input("Enter the second number: "))
        if num2 == 0:
            raise ZeroDivisionError("Zero would produce an error in division!")
        inf_bool2 = False
    except ValueError:
        print("\033[91mPlease enter a digit!\033[0m")
    except ZeroDivisionError:
        print("\033[91mSecond number should not be 0!\033[0m")
quotient = num1 // num2
remainder = num1 % num2
print(f"The quotient of {num1}/{num2} is {quotient} and their remainder is {remainder}")
