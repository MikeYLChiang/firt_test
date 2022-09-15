class Computer:
    def __init__(self):
        self.value = 0
    def enter(self, input):
        self.value = input
        print("input value is " + str(input))
    def add(self, input):
        addValue = self.value + input
        print("add value is " + str(addValue))
        
        
def main():
    computer = Computer()
    computer.enter(7)
    computer.add(8)
    
if __name__ == '__main__':
    main()
