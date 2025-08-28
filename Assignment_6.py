import random

code1 = str(random.choice([0,1,2,3,4,5,6,7,8,9])) + \
        str(random.choice([0,1,2,3,4,5,6,7,8,9])) + \
        str(random.choice([0,1,2,3,4,5,6,7,8,9]))

code2 = str(random.choice([1,2,3,4,5,6])) + \
        str(random.choice([1,2,3,4,5,6])) + \
        str(random.choice([1,2,3,4,5,6])) + \
        str(random.choice([1,2,3,4,5,6]))

print("3-digit code:", code1)
print("4-digit code:", code2)
