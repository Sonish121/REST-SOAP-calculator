class Calculator:
    @staticmethod
    def add(num1, num2):
        return float(num1 + num2)
    
    @staticmethod
    def subtract(num1, num2):
        return float(num1 - num2)
    
    @staticmethod
    def multiply(num1, num2):
        return float(num1 * num2)
    
    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero")
        return float(num1 / num2)