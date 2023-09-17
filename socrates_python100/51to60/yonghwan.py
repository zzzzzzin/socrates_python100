#문제51번
def compare_integers(a, b):
    return a != b
a, b = map(int, input().split())
result = compare_integers(a, b)
print(result)

#문제52번
n = int(input())
print(bool(n))

#문제53번
a = bool(int(input()))
print(not a)

#문제54번
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#문제55번
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#문제56번
a, b = map(int, input().split())
def compare_integers(a,b):
    return bool(a) != bool(b)
    
result = compare_integers(a,b)
print(result)

#문제57번
a, b = map(int, input().split())
def compare_integers(a,b):
    return bool(a) == bool(b)

result = compare_integers(a,b)
print(result)

#문제58번
def both_false(a, b):
    return not bool(a) and not bool(b)

a, b = map(int, input().split())

result = both_false(a, b)
print(result)

#문제59번
num = int(input())
result = ~num
print(result)

#문제60번
a, b = map(int, input().split())
result = a & b
print(result)
