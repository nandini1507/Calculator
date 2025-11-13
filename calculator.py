def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            return "Error: Division by zero"
        result /= n
    return result

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    nums = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in nums.split()]

    if choice == '1':
        print("Result:", add(numbers))
    elif choice == '2':
        print("Result:", subtract(numbers))
    elif choice == '3':
        print("Result:", multiply(numbers))
    elif choice == '4':
        print("Result:", divide(numbers))
    else:
        print("Invalid choice. Try again.")
