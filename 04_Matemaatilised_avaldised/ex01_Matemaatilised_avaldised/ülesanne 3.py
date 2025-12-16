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