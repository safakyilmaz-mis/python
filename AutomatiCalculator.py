class calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def add(self):
        return self.number1+self.number2
    def subtract(self):
        return self.number1-self.number2
    def multiply(self):    
        return self.number1*self.number2
    def divide(self):
        return self.number1/self.number2

Calculator = calculator(int(input()),int(input()))
print("sum of two numbers: " + str(Calculator.add()))
print("subtract of two numbers: " + str(Calculator.subtract()))
print("multiplication of two numbers: " + str(Calculator.multiply()))
print("divide operation of two numbers: " + str(Calculator.divide()))
