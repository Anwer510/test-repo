from calculator import Calculator
from utils import format_result


def main():
    calc = Calculator()
    
    x, y = 10, 3
    
    print(f"Addition: {format_result(calc.add(x, y))}")
    print(f"Subtraction: {format_result(calc.subtract(x, y))}")
    print(f"Multiplication: {format_result(calc.multiply(x, y))}")
    print(f"Division: {format_result(calc.divide(x, y))}")
    print(f"Power: {format_result(calc.power(x, y))}")
    
    numbers = [4, 7, 2, 9, 1, 5]
    print(f"
Stats for {numbers}:")
    print(f"  Mean: {format_result(calc.mean(numbers))}")
    print(f"  Median: {calc.median(numbers)}")
    print(f"  Min: {min(numbers)}, Max: {max(numbers)}")


if __name__ == "__main__":
    main()
