class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0

        is_negative = (a < 0 and b > 0) or (a > 0 and b < 0)

        pos_a = a if a >= 0 else 0 - a
        pos_b = b if b >= 0 else 0 - b

        for _ in range(pos_b):
            result = self.add(result, pos_a)
        
        if is_negative:
            return 0 - result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        is_negative = (a < 0 and b > 0) or (a > 0 and b < 0)
        
        pos_a = a if a >= 0 else 0 - a
        pos_b = b if b >= 0 else 0 - b
            
        result = 0
        while pos_a >= pos_b:
            pos_a = self.subtract(pos_a, pos_b)
            result = self.add(result, 1)
        
        if is_negative:
            return -result
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")

        if b < 0:
            a = self.subtract(0, a)
            b = self.subtract(0, b)
            return self.subtract(0, self.modulo(a, b))

        if a >= 0:
            while a >= b:
                a = self.subtract(a, b)
            return a
        else:
            while a < 0:
                a = self.add(a, b)
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 3))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))