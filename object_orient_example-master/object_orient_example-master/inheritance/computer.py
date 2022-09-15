class Computer:
    def __init__(self):
        self.value = 0
    def enter(self, input):
        self.value = input
        print("input value is " + str(input))
    def add(self, input):
        addValue = self.value + input
        print("add value is " + str(addValue))
        
class SuperComputer(Computer):
    def minuse(self, input):
        ans = self.value - input
        print("minuse value is " + str(ans))
        
        
def main():
    computer = SuperComputer()
    computer.enter(7)
    computer.add(8)
    computer.minuse(3)
    
if __name__ == '__main__':
    main()
