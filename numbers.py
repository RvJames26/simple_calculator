class Numbers:

    def get_numbers(self):
        while True:
            try:
                self.first_num = int(input("Please input your First Number: "))
                self.second_num = int(input("Please input your Second Number: "))
                break
            except ValueError:
                print(f"{self.error_color}Input numbers only{self.reset_color}")