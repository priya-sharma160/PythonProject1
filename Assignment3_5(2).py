numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print("Please enter a valid number.")

# Sort in descending order
numbers.sort(reverse=True)

# Print the top 5 numbers
print("Top 5 greatest numbers:")
for num in numbers[:5]:
    print(num)
