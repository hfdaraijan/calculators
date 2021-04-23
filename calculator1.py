print("Welcome")
while True:
    x = input("What operation do you want? +, -, *, / \n")


    if x == "+":
        while True:
            try:
                num1 = float(input("Enter your 1st number: "))
                num2 = float(input("Enter your 2nd number: "))
                print(num1, "+", num2, "=", num1+num2)
                break
            except ValueError:
                print("Please input number only...")  
                continue 
    elif x == "-":
        while True:
            try:
                num1 = float(input("Enter your 1st number: "))
                num2 = float(input("Enter your 2nd number: "))
                print(num1, "-", num2, "=", num1-num2)
                break
            except ValueError:
                print("Please input number only...")  
                continue 
    elif x == "*":
        while True:
            try:
                num1 = float(input("Enter your 1st number: "))
                num2 = float(input("Enter your 2nd number: "))
                print(num1, "*", num2, "=", num1*num2)
                break
            except ValueError:
                print("Please input number only...")  
                continue 
    elif x == "/":
        while True:
            try:
                num1 = float(input("Enter your 1st number: "))
                num2 = float(input("Enter your 2nd number: "))
                print(num1, "/", num2, "=", num1/num2)
                break
            except ValueError:
                print("Please input number only...")  
                continue 
    else:
        print("***Invalid operator***")

 