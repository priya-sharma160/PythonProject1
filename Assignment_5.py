talents = int(input("Enter the number of talents: "))
pounds = int(input("Enter the number of pounds: "))
lots = int(input("Enter the number of lots: "))
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
total_lots = (talents * 20 * 32) + (pounds * 32) + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("\n converted Weight")
print(f"The weight is {kilograms} kilograms and {grams:.2f} grams.")
