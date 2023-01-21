operator = input("""\nChoose one of the following operators: \n \t+ \t- \t* \t/ \t**
or type any other value to sum many numbers. \n\t\t""")

list_operators = ["+", "-", "*", "/", "**"]

if operator not in list_operators:
    print("""You chose to sum many numbers. 
    Once all are typed in, please press enter twice.""")

    number = input("Number: ")

    try:
        float(number)
    except ValueError:
        number = input("Choose a numeric value for number: \n\t\t")

    number = float(number)
    end = ""

    while end.upper() != "END":
        add = input("Add: ")

        if add.upper() != "END":
            try:
                float(add)
            except ValueError:
                add = input("Choose a numeric value to add: \n\t\t")

            add = float(add)
            number = number + add
        else:
            end = "END"
            print("The sum of your numbers is: ", number)

else:

    numberA = input("Choose number A: \n\t\t")

    try:
        float(numberA)
    except ValueError:
        numberA = input("Choose a numeric value for number A: \n\t\t")

    numberB = input("Choose number B: \n\t\t")

    try:
        float(numberB)
    except ValueError:
        numberB = input("Choose a numeric value for number B: \n\t\t")

    numberA = float(numberA)
    numberB = float(numberB)

    if operator == "+":
        print("A + B =", numberA + numberB)
    elif operator == "-":
        print("A - B =", numberA - numberB)
    elif operator == "*":
        print("A * B =", numberA * numberB)
    elif operator == "/":
        if numberB == 0:
            print("Critical error - DIVISION BY 0!!!")
        else:
            print("A / B =", numberA / numberB)
    elif operator == "**":
        print("A ** B =", numberA ** numberB)
    else:
        operator = input("Choose one of the following operators: \n \t+ \t- \t* \t/ \t**\n\t\t")
