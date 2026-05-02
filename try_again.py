class Again:
    
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