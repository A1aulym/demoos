#ex1
import math
somelist = map(int, input().split(','))
print(math.prod(somelist))


#ex2
string = input()

cnt = 0
cnt1 = 0

for i in string:
    if i.isupper():
        cnt += 1
    if i.islower():
        cnt1 += 1

print(cnt)
print(cnt1)


#ex3
s = input()

s_reversed = s[::-1]

if s == s_reversed:
    print("True")
else:
    print('False')


# ex4
import math, time

SQ = int(input())
milisc = int(input())
time.sleep(0.001 * milisc)

print("Square root of", SQ, " after ", milisc, " miliseconds is ", math.sqrt(SQ) )


#ex5
x = tuple(map(int, input().split()))

if x and all(x):
    print("True")
else:
    print("False")