## - Check if a user-entered number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Exit the loop as we found a divisor
        else:
            continue  # Continue to the next iteration if not divisible
        pass  # This pass is optional and does nothing

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")