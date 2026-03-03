class Calculator:
    """A simple calculator with basic and statistical operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exp):
        return base ** exp

    def mean(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def median(self, numbers):
        if not numbers:
            return 0
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            return sorted_nums[mid]
