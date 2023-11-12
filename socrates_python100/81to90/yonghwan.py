# 문제81번
def print_hex_gugudan(n):
    for i in range(1, 16):
        print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

input_value = input()

if input_value == 'A':
    print_hex_gugudan(10)
elif input_value == 'B':
    print_hex_gugudan(11)
elif input_value == 'C':
    print_hex_gugudan(12)
elif input_value == 'D':
    print_hex_gugudan(13)
elif input_value == 'E':
    print_hex_gugudan(14)
elif input_value == 'F':
    print_hex_gugudan(15)

# 문제82번
def replace_369(number):
    replaced = ""
    for digit in str(number):
        if digit == '3' or digit == '6' or digit =='9':
            replaced = 'X'
        else:
            replaced += digit
    return replaced

def print_numbers(n):
    for i in range(1, n+1):
        replaced_number = replace_369(i)
        print(replaced_number, end=" ")
input_number = int(input())
print_numbers(input_number)

# 문제83번
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)

print(r*g*b)

# 문제84번
input_numbers=input()
numbers = input_numbers.split()
numbers = [float(num) for num in numbers]
volume = numbers[0]*numbers[1]*numbers[2]*numbers[3]/8/1024/1024
rounded_number = round(volume, 1)
result = str(rounded_number) + " MB"
print(result)

# 문제85번
input_numbers=input()
numbers = input_numbers.split()
numbers = [float(num) for num in numbers]
volume = numbers[0]*numbers[1]*numbers[2]/8/1024/1024
rounded_number = round(volume, 2)
result = str(rounded_number) + " MB"
print(result)

# 문제 86번
n = int(input())
s=0
c=1
while s < n :
    s= s+c
    c= c+1
    if s>=n :
        break
print(s)

# 문제 87번
n = int(input())
c = 1

while c <= n:
    if c % 3 != 0:
        print(c)
    c = c + 1

# 문제 88번
x, y, z = input().split()
a = int(x)
d = int(y)
n = int(z)
print(a+(n-1)*d)

# 문제 89번
x, y, z = input().split()
a = int(x)
r = int(y)
n = int(z)
print(a*r**(n-1))

# 문제 90번
x, y, z, n = input().split()
a = int(x)
m = int(y)
d = int(z)
n = int(n)

i = 0
while i < n - 1:
    a = a * m + d
    i = i+1

print(a)
