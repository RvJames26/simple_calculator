error_color = "\033[41m\033[97m"
reset_color = "\033[0m"
answer_color = "\033[42m"

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
            print(f"{error_color}Please input number 1-4 only{reset_color}")
            continue
        if operation > 0 and operation < 5:
            print("Successfully selected an operation")
            break
    except ValueError:
        print(f"{error_color}Please input number 1-4 only{reset_color}")

while True:
    try:
        first_num = int(input("Please input your First Number: "))
        second_num = int(input("Please input your Second Number: "))
        break
    except ValueError:
        print(f"{error_color}Input numbers only{reset_color}")

if operation == 1:
    sum = first_num + second_num
    print(f"{first_num} + {second_num} = {answer_color}{sum}{reset_color}")
if operation == 2:
    difference = first_num - second_num
    print(f"{first_num} + {second_num} = {answer_color}{difference}{reset_color}")
if operation == 3:
    product = first_num * second_num
    print(f"{first_num} x {second_num} = {answer_color}{product}{reset_color}")
if 