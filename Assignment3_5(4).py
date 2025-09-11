cities = []

for i in range(5):
    name = input("Enter the name of city " + str(i + 1) + ": ")
    cities.append(name)

print("\nYou entered:")
for city in cities:
    print(city)
