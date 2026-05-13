# Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# New function added in feature branch
def square(a):
    return a * a

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("2 * 3 =", multiply(2, 3))
    print("6 / 2 =", divide(6, 2))