class Operator:

    def picking_operator(self):
                print ("Welcome to my simple Calculator")

                while True:
                    try:
                        self.operation = int(input("""What operation do you want to use:
                                    1. Addition
                                    2. Subtraction
                                    3. Multiplication
                                    4. Division
                                    Please input the number you want to use:"""))
                        if self.operation > 4 or self.operation < 1:
                            print(f"{self.error_color}Please input number 1-4 only{self.reset_color}")
                            continue
                        if self.operation > 0 and self.operation < 5:
                            print("Successfully selected an operation")
                            break
                    except ValueError:
                        print(f"{self.error_color}Please input number 1-4 only{self.reset_color}")