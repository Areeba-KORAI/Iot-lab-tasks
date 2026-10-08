my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]

total_sum = 0
count = 0

for num in my_list:
    total_sum += num
    count += 1

average = total_sum / count
print(f"The average is: {average}")