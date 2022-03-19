
def y():

    number_1 = int(input("Enter 1st number : "))
    number_2 = int(input("Enter 2nd number : "))

    operator = int(input(("Please select the operation you want to perform:\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n: ")))

    if operator == 1:
        result = (number_1 + number_2)
        print(result)
    elif operator == 2:
        result = (number_1 - number_2)
        print(result)
    elif operator == 3:
        result = (number_1 * number_2)
        print(result)
    elif operator == 4:
        try:
            result = (number_1 / number_2)
            print(result)
        except ZeroDivisionError:
            print("Not possible")
    else:
        print("operator not found")

    to_continue=input("Do you want to continue , press y to continue n to exit : ").lower()

    if to_continue == 'y':
        y()
    elif to_continue == 'n':
        print("Thankyou")
    else:
        print("I didn't understand")

y()