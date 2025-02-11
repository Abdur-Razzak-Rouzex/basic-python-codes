import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':
        number = random.randint(1,6)
        print(f"The dice value is: {number}")
    elif choice == 'n' :
        print("Thank you for playing")
        break
    else:
        print("Invalid input")