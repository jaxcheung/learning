def collatz(number):
    while number != 1:
        print(number)
        number = number // 2 if number % 2 == 0 else number * 3 + 1
    print(number)

try:
    number = int(input("Input a number: "))
    if number < 1:
        raise ValueError("Please enter a positive integer.")
    collatz(number)
except ValueError as e:
    print(f"Invalid input: {e}")