string = "1 2 3 4 5 9472 4274298347234872  98472 834239872 29847 298273 492837487234"


total = 0

number = []
for n in string.split(): 
    print(n)
    number.append(int(n))

print(number)


for g in range (len(number)): 
    total += int(number[g])

print(total)