print ("Welcome to my simple Calculator")
while True:
    try:
        operation = int(input("""What operation do you want to use:
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    Please input the number you want to use:"""))
        if operation > 4 or operation < 1:
            print("Please input number 1-4 only")
            continue
        if operation > 0 and operation < 5:
            print("Successfully selected an operation")
    except ValueError:
        print("Please input number 1-4 only")