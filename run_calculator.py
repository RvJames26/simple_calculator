class Run:

    def run(self):
        while True:
            self.picking_operator()
            self.get_numbers()
            self.doing_math()
            
            loop = self.again()

            if loop == False:
                break