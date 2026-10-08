numbers = []
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
    	odd_count += 1

print("\n--- Statistics Summary ---")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")