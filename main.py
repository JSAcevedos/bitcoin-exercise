prices = input().split()
days = []
index = 0

for i in prices:
    index += 1
    price = int(i)
    day = 0
    for j in range(len(prices) - index):
        if price >= int(prices[index + j]):
            day += 1
        else:
            day += 1
            break
        if j == (len(prices) - index - 1):
            day = 0
    days.append(day)

print(days)
