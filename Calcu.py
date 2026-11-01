def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if choice == '1':
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {num1 * num2}")


else:
    print("Invalid input")