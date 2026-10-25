# Unit 2 - Loops + Break/Continue

for num in range(2, 101):

    is_prime = True

    # Nested loop to check factors
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Skip non-prime numbers
    if not is_prime:
        continue

    print(num, end=" ")