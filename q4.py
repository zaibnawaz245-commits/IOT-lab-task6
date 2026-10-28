# Question 4 - Even / Odd count
numbers = (10, 15, 20, 25, 30, 35, 40)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")