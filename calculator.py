class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def sum(self):
        return self.input1 + self.input2

    def sub(self):
        return self.input1 - self.input2

if __name__ == "__main__":
    ops = Calculator(10, 3)
    print(ops.sum())
    print(ops.sub())
