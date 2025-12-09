"""Math exercises."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    addition_result = num_a + num_b
    difference = num_a - num_b
    return addition_result, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = math.pi * radius ** 2
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    # Write your code here
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return int(round(triangle_area, 0))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    b = (c ** 2 - a ** 2) ** 0.5
    return b

if __name__ == '__main__':
    sum_and_difference(5,6)
    assert addition_result == 11
    assert not -1 != difference

    float_division_result = float_division(10,10)
    assert isinstance(float_division_result, float)
    assert 0.99 < float_division_result < 1.01
    integer_division_result = integer_division(10,2)
    assert 4.99 < float_division_result < 5.01

    multiplication, power, remainder = powerful_operations(3,4)
    assert multiplication == 12
    assert power == 81
    assert remainder == 3

    multiplication, power, remainder = powerful_operations(10,2)
    assert multiplication == 20
    assert power == 100
    assert remainder == 0
    area_of_a_circle_result = area_of_a_circle(3)
    assert 28.269 < area_of_a_circle_result < 28.271, f""

"""Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile
 ristküliku ümbermõõdu ja pindala."""

def compute_rectangle():
    lenght = float(input("sisesta ristküliku pikkus"))
    width = float(input("sisesta ristküliku laius"))
    area = width * lenght
    circumference = 2 * (lenght + width)
    print(f"Antud ristküliku pindala on {area}")
    print(f"ümbermõõt on {circumference}")

    if __name__ == "__main__":
        compute_rectangle()

"""Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise
 tervituse koos tekstiga, mis ütleb kas tegemist on 7-18-aastase inimesega."""

 def greet_by_name(name: str) -> str:
     return f"Tervist {name}!"

 def verify_age(age: int) -> str:
     if 7 <= age <= 18:
         return "Oled 7-18 aastane"
     return "Oled noorem või vanem kui 7-18 aastased"

if __name__ == "__main__":
    name = input("Sisesta oma nimi: ")
    age = int(input("Sissesta oma vanus aastates täisarvuna: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")

"Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega"

def calculate(num1: float, num2: float, operation: str) -> str:
    result = ""
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "//":
            result = num1 // num2
        elif operation == "**":
            result = num1 ** num2
        elif operation == "%":
            result = num1 % num2
        return f"{num1}+{num2}={result}"


if __name__ == "__name__":
    first = float(input("Sisesta esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op = input("Sisestage tehe: ")
    print(f"Tulemus: {calculate(first, second, op)}")

