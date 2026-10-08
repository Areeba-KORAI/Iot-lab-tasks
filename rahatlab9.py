shopping = []

print("Enter 5 shopping items:")
for i in range(1, 6):
    item = input(f"Item {i}: ")
    shopping.append(item)

print("\n--- Complete Shopping List ---")
print(shopping)