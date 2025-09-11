numbers = []

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break
    try:
        numbers.append(float(num))
    except:
        print("Please enter a valid number.")

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
