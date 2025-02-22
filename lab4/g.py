#1
def square_generator():
    N = int(input("Enter N: "))
    def generate_squares(N):
        for i in range(1, N + 1):
            yield i ** 2

    for square in generate_squares(N):
        print(square)

square_generator()


#2
def even_numbers():
    n = int(input("Enter n: "))

    def generate_even(n):
        for i in range(0, n + 1, 2):
            yield i

    print(",".join(str(num) for num in generate_even(n)))

even_numbers()


#3
def divisible_by_3_and_4():
    s = int(input("Enter s: "))
    
    def generate_divisible(s):
        for i in range(s + 1):
            if i % 3 == 0 and i % 4 == 0:
                yield i

    for num in generate_divisible(s):
        print(num)

divisible_by_3_and_4()


#4
def squares():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    def generate_squares(a, b):
        for i in range(a, b + 1):
            yield i ** 2

    for sq in generate_squares(a, b):
        print(sq)

squares()


#5
def countdown():
    c = int(input("Enter c: "))

    def generate_countdown(c):
        for i in range(c, -1, -1):
            yield i

    for num in generate_countdown(c):
        print(num)

countdown()

