class Calculator:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def add(self) -> float:
        c = self.a + self.b
        return c
    
    def sub(self) -> float:
        c = self.a - self.b
        return c
    
    def mul(self) -> float:
        c = self.a * self.b
        return c
    
    def div(self) -> float:
        c = self.a / self.b
        return c
    
a_add_b = Calculator(1,2).add()
a_sub_b = Calculator(1,2).sub()
a_mul_b = Calculator(1,2).mul()
a_div_b = Calculator(1,2).div()

print(f'Add 1 and 2: {a_add_b}')
print(f'Subtract 1 and 2: {a_sub_b}')
print(f'Multiply 1 and 2: {a_mul_b}')
print(f'Divide 1 and 2: {a_div_b}')