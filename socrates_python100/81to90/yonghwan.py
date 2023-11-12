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
