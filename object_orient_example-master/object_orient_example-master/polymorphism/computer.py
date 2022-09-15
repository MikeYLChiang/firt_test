from abc import  abstractmethod

class Computer:
    def __init__(self):
        self.value = 0
    def enter(self, input):
        self.value = input
        print("input value is " + str(input))
    def add(self, input):
        self.addValue = self.value + input
        print("add value is " + str(self.addValue))
    @abstractmethod
    def show(self):
        pass

class ComputerX(Computer):
    def show(self):
        print("value is " + str(self.value))
 
class SuperComputer(Computer):
    def show(self):
        print("addValue is " + str(self.addValue))
    def minuse(self, input):
        ans = self.value - input
        print("minuse value is " + str(ans))
        
        
def main():
    print("0 is computer x, 1 is super computer")
    inputValue = input()
    if(inputValue == '0'):
        print("use computer x")
        computer = ComputerX()
    else:
        print("use super computer")
        computer = SuperComputer()
    computer.enter(7)
    computer.add(8)
    computer.show()
    
if __name__ == '__main__':
    main()
