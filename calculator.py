print("Welcome")
    x = input("What operation do you want? +, -, *, / \n")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    if x == "+":
        print(num1, "+", num2, "=", num1+num2)
    elif x == "-":
        print(num1, "-", num2, "=", num1-num2)
    elif x == "*":
       print(num1, "*", num2, "=", num1*num2)
    elif x == "/":
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("***Invalid operator***")


