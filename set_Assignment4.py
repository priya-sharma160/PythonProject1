names = set()
name = input("Enter a name (or press Enter to finish): ")
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

    name = input("Enter a name (or press Enter to finish): ")

print("\nNames entered:")
for n in names:
    print(n)

