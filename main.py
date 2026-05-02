class Calculator:

    def __init__(self):
        self.error_color = "\033[41m\033[97m"
        self.reset_color = "\033[0m"
        self.answer_color = "\033[42m"

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
        if self.operation == 1:
            sum = self.first_num + self.second_num
            print(f"{self.first_num} + {self.second_num} = {self.answer_color}{sum}{self.reset_color}")
        if self.operation == 2:
            difference = self.first_num - self.second_num
            print(f"{self.first_num} - {self.second_num} = {self.answer_color}{difference}{self.reset_color}")
        if self.operation == 3:
            product = self.first_num * self.second_num
            print(f"{self.first_num} x {self.second_num} = {self.answer_color}{product}{self.reset_color}")
        if self.operation == 4:
            quotient = self.first_num / self.second_num
            print(f"{self.first_num} / {self.second_num} = {self.answer_color}{quotient}{self.reset_color}")

    def again(self):
        while True:
            try_again = input("Do you want to try again?(y/n) ")
            if try_again == "y":
                return True
            if try_again == "n":
                print("Thank you!")
                return False
            else:
                print(f"{self.error_color}Please input y or n only{self.reset_color}")

    def run(self):
        while True:
            self.picking_operator()
            self.get_numbers()
            self.doing_math()
            
            loop = self.again()

            if loop == False:
                break

calcu = Calculator()
calcu.run()