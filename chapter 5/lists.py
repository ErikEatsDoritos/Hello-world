import random
prices = []

for i in range(30):
    prices.append(random.randrange(-10,100))

print(prices)
total = 0 
for j in range(len(prices)):
    number = prices[j] 
    if number > 5: 
        total += number
    if number < 0: 
        print(f'Error index {prices[j]} number {j}')
        print(total)
        break

