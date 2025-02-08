def is_prime(n):
    if n <= 1:
        return False   
    for i in range(2, n):  
        if n % i == 0:  
            return False   
    return True  
num = [10, 3, 5, 8, 11, 14, 17, 19, 21, 23, 29, 30]
prime_numbers = list(filter(lambda x: is_prime(x), num))

print("Prime numbers:", prime_numbers)