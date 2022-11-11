number = "65, 75, 32, 22"

num = []

for i in number.split(", "):
    num.append(int(i))
    
print(num)