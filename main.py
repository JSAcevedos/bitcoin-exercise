# Variables declaration and created input to get the data
prices = input().split()
days = []
index = 0

# Loop that compares each item with the next items until find a bigger price

for i in prices:
# Local variables for the loop, index will allow only search after each list item, convert each item in integer to make the comparations, set the days counter to zero for each item
    index += 1
    price = int(i)
    day = 0
# Count how many days musto to wait to find a better price, if there is no a better price set day to zero
    for j in range(len(prices) - index):
        if price >= int(prices[index + j]):
            day += 1
        else:
            day += 1
            break
        if j == (len(prices) - index - 1):
            day = 0
    days.append(day)

# Print the array output without the brackets or the commas.
for i in range(len(days)):
    if i == len(days) - 1:
        print(days[i], end="")
    else:
        print(days[i], end=" ")
