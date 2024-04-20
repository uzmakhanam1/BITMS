'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_magical_prime(n):
    if not is_prime(n):
        return False
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

# Example usage
number = int(input("Enter a number to check if it's prime and magical prime: "))
if is_prime(number):
    print(number, "is a prime number.")
    if is_magical_prime(number):
        print(number, "is also a magical prime.")
    else:
        print(number, "is not a magical prime.")
else:
    print(number, "is not a prime number.")'''


####
def is_neon_number(n):
    square = n * n
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == n

# Example usage
number = int(input("Enter a number to check if it's a neon number: "))
if is_neon_number(number):
    print(number, "is a neon number.")
else:
    print(number, "is not a neon number.")

