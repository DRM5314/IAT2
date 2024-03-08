class Machine:
    sodas = []
    name = " Default 1"

    def __init__(self, name):
        self.name = name


    def giveSodad(self,soda):
        print("I am giving a soda!! is:"+soda)

    def askCode(self):
        print("Enter a code please!!")

    def askForMoney(self):
        print("Please insert coin!!")

    def getName(self):
        return self.name