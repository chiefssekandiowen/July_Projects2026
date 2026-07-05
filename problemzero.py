num = 1
squared_list = []
odd_list = []

while num <= 789000:
    sqd = num * num
    squared_list.append(sqd)
    num += 1

for odd in squared_list:
    if odd % 2 != 0:
        odd_list.append(odd)

print("Sum of Odd List:", sum(odd_list))

