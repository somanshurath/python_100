import random
import string

print("\n------------------")
print("Password Generator")
print("------------------\n")

print("Password can contain special characters, numeric characters as well as alphabetic characters.\n")

length = 0
num = 0
spec = 0
cap = 0
lower = 0

# input

checkLength = True

while checkLength:
    length = int(input("Enter the total number of characters required.\n"))
    if length < 6:
        print("Password must have at least 6 characters.\n")
        continue
    else:
        checkLength = False

checkNo = True

while checkNo:
    num = int(input("\nEnter the total number of numeric characters.\n"))
    if num > length:
        print(f"Password can only have at most {length} numeric characters.\n")
        continue
    else:
        checkNo = False
    if num == length:
        spec = 0
        cap = 0

checkSpec = True

while checkSpec and length - num != 0:
    spec = int(input("\nEnter the total number of special characters.\n"))
    if spec > length - num:
        print(f"Password can now have at most {length - num} special characters.\n")
        continue
    else:
        checkSpec = False
    if spec == length - num:
        cap = 0

checkCap = True

while checkCap and length - num - spec != 0:
    cap = int(input("\nEnter the total number of alphabetic characters that must be in capital.\n"))
    if cap > length - num - spec:
        print(f"Password can have at most {length - num - spec} capital alphabetic characters.\n")
        continue
    else:
        checkCap = False

lower = length - num - spec - cap

# processing

password = length * [0]

locList = [i for i in range(length)]

numList = list(string.digits)

# for num
for i in range(num):
    position = random.choice(locList)
    password[position] = random.choice(numList)
    locList.remove(position)

sp = ['!', '#','@','.','?','$']

# for spec
for i in range(spec):
    position = random.choice(locList)
    password[position] = random.choice(sp)
    locList.remove(position)

lowerList = list(string.ascii_lowercase)
upperList = list(string.ascii_uppercase)

# for cap
for i in range(cap):
    position = random.choice(locList)
    password[position] = random.choice(upperList)
    locList.remove(position)

# for lower
for i in range(lower):
    position = random.choice(locList)
    password[position] = random.choice(lowerList)
    locList.remove(position)

# final output
print("\nYour new password: ",end='')

for x in range(len(password)):
    print(password[x], end='')

print("\n")
