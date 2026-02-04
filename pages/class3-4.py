import random 

target = random.randint(0, 100)

min_val = 0
max_val = 100

while True:
    num = int(input(f"Enter a number between {min_val} and {max_val}: "))
    if num < min_val or num > max_val:
        print("Invalid input. Please try again.")
    elif num < target:
        print("Too low. Try again.")
        min_val = num + 1

    elif num > target:
        print("Too high. Try again.")
        max_val = num - 1

    else:
        print("Congratulations! You guessed the number.")
        break