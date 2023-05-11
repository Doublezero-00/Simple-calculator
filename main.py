shoud_continue = True
while shoud_continue == True: 
    #Taking user inputs
    num1 = float(input('\033[32m'"Enter value 01 : "))
    num2 = float(input('\033[32m'"Enter value 02 : "))

    #Function for giving addition of two numbers
    def addition(num1: float,num2: float) -> float:
        return num1+num2

    #Function for giving substraction of two numbers
    def substraction(num1: float,num2: float) -> float:
        return num1-num2

    #Function for giving multiplication of two numbers
    def multiplication(num1: float,num2: float) -> float:
        return num1*num2

    #Function for giving division of two numbers
    def division(num1: float,num2: float) -> float:
        return num1/num2

    def clear(num1: float,num2: float):
        num1 = 0
        num2 = 0
        all_clear = 0
        return all_clear

    #User selections
    print('\033[33m'"1] +")
    print('\033[33m'"2] -")
    print('\033[33m'"3] *")
    print('\033[33m'"4] /")
    print('\033[33m'"5] clear")

    #taking input for user selection
    user_select = int(input('\033[32m'"Enter your choice : "))

    #Print outputs
    if user_select == 1:
        print(addition(num1,num2))

    elif user_select == 2:
        print(substraction(num1,num2))

    elif user_select == 3:
        print(multiplication(num1,num2))

    elif user_select == 4:
        print(division(num1,num2))

    elif user_select == 5:
        print(clear(num1,num2))

    else :
        print('\033[31m'"Invalid choice! please check again")
    
    user_input = input('\033[32m'"May I continue?(y/n) : ")

    if user_input == "n" or user_input == "N":
        break





