number_of_order = int(input())
total = 0
total_sum = 0

for i in range (number_of_order):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())

    total = price_per_capsule * days * capsules
    if total <= 0:
        continue
    print(f"The price for the coffee is: ${total:.2f}")
    total_sum += total

    total = 0

print(f"Total: ${total_sum:.2f}")