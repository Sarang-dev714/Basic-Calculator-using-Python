
# This is developed by Sarang Dev A
# calc.py
# Basic Calculator CLI
# Supports: add, subtract, multiply, divide, power, modulo, clear, exit


def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return None
    return a / b
def mod(a, b):
    if b == 0:
        return None
    return a % b
def power(a, b): return a ** b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def main():
    print("=== Basic Calculator ===")
    print("Operations: +  -  *  /  %  ^  (type 'help' for commands, 'exit' to quit)\n")

    while True:
        cmd = input("Enter operation (+, -, *, /, %, ^) or command: ").strip().lower()
        if cmd in ("exit", "quit"):
            print("Goodbye!")
            break
        if cmd == "help":
            print("Commands:")
            print("  +  : addition")
            print("  -  : subtraction")
            print("  *  : multiplication")
            print("  /  : division")
            print("  %  : modulo")
            print("  ^  : power (a^b)")
            print("  clear : clears (no-op in CLI)")
            print("  exit  : quit program")
            continue
        if cmd == "clear":
            print("\n" * 2)
            continue

        if cmd not in {"+", "-", "*", "/", "%", "^"}:
            print("Unknown operation. Type 'help' for commands.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if cmd == "+":
            res = add(a, b)
        elif cmd == "-":
            res = sub(a, b)
        elif cmd == "*":
            res = mul(a, b)
        elif cmd == "/":
            res = div(a, b)
            if res is None:
                print("Error: Division by zero.")
                continue
        elif cmd == "%":
            res = mod(a, b)
            if res is None:
                print("Error: Modulo by zero.")
                continue
        elif cmd == "^":
            res = power(a, b)

        print(f"Result: {res}\n")

if __name__ == "__main__":
    main()
