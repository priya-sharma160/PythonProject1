import random

num = input("How many dice do you want to roll? ")

if num.isdigit():
    num = int(num)
    total = 0
    count = 1

    print("You rolled:")

    while count <= num:
        roll = random.randint(1, 6)
        print("Die", count, ":", roll)
        total += roll
        count += 1

    print("Total sum:", total)
else:
    print("Please enter a valid number.")
