length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print(f"The zander is {difference:.1f} cm below the size limit. Please release it back into the lake.")
else:
    print("The zander meets the size limit. You may keep it.")
