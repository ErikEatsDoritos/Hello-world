string = ("one,two,three,four,five")

numb = string.split(",")

print(numb)
number = []
for i in range(len(numb)):
    print(i)
    number = numb.append(int(number[i]))

print(number)
