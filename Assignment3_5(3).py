num = input("Enter an integer: ")

if num.isdigit():
    num = int(num)
    if num < 2:
        print(num, "is not a prime number.")
    else:
        is_prime = True
        i = 2
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
else:
    print("Please enter a valid integer.")
