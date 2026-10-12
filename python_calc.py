def calculator():
    while True:
        print("---Menu---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. check even/odd")
        print("6. calculate percentage")
        print("7. Exit")
        
        choice = int(input("Enter the option(1-7): "))
        if choice == 1:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
            print( a + b)
        elif choice == 2:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
            print( a - b)
        elif choice == 3:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
            print(a*b)
        elif choice == 4:
            a = float(input("Enter your first number: "))
            b = float(input("Enter your second number: "))
            print(a/b)
        elif choice == 5:
            num = float(input("Enter your integar: "))
            if num % 2 == 0:
                print("Number is even")
            else:
                print("Number is odd")
        elif choice == 6:
            part = float(input("Enter the part value: "))
            total = float(input("Enter total value: "))
            if total == 0:
                print("Error: Total cannot be zero")
            else:
                percentage = (part/total) * 100
                print(percentage)
        elif choice == 7:
            print("Exit")
            break
        else:
            print("Invalid option please select an option between 1 and 7: ")

calculator()