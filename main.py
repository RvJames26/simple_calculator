class Calculator:

    def __init__(self):
        error_color = "\033[41m\033[97m"
        reset_color = "\033[0m"
        answer_color = "\033[42m"

    def picking_operator(self):
        while True:
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
                        print(f"{self.error_color}Please input number 1-4 only{self.reset_color}")
                        continue
                    if operation > 0 and operation < 5:
                        print("Successfully selected an operation")
                        break
                except ValueError:
                    print(f"{self.error_color}Please input number 1-4 only{self.reset_color}")

    def get_numbers(self):
        while True:
            try:
                first_num = int(input("Please input your First Number: "))
                second_num = int(input("Please input your Second Number: "))
                break
            except ValueError:
                print(f"{self.error_color}Input numbers only{self.reset_color}")

    def doing_math(self):
        if operation == 1:
            sum = first_num + second_num
            print(f"{first_num} + {second_num} = {self.answer_color}{sum}{self.reset_color}")
        if operation == 2:
            difference = first_num - second_num
            print(f"{first_num} - {second_num} = {self.answer_color}{difference}{self.reset_color}")
        if operation == 3:
            product = first_num * second_num
            print(f"{first_num} x {second_num} = {self.answer_color}{product}{self.reset_color}")
        if operation == 4:
            quotient = first_num / second_num
            print(f"{first_num} / {second_num} = {self.answer_color}{quotient}{self.reset_color}")

    def again(self):
        while True:
            try_again = input("Do you want to try again?(y/n) ")
            if try_again == "y":
                break
            if try_again == "n":
                print("Thank you!")
                break
            else:
                print(f"{self.error_color}Please input y or n only{self.reset_color}")
                continue

        if try_again == "y":
            continue
        if try_again == "n":
            break