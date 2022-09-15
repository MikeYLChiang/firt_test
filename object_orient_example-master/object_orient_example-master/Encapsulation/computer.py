class Computer:
    def __init__(self):
        self.value = 0
        self.self = 0
    def enter(self, input):
        self.value = input
        print("input value is " + str(input))
    def add(self, input):
        self.addValue = self.value + input
        print("add value is " + str(self.addValue))
    def get_answer(self):
        return self.addValue
        
        
def main():
    computer = Computer()
    computer.enter(7)
    computer.add(8)
    ans = computer.get_answer()
    print("ans is " + str(ans))
    
if __name__ == '__main__':
    main()
