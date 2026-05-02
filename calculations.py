class Calculations:

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