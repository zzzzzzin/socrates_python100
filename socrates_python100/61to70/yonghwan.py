# 문제61번
a, b = map(int, input().split())
result = a | b
print(result)

# 문제62번
a, b = map(int, input().split())
result = a ^ b
print(result)

# 문제63번
a, b = input().split()
a = int(a) 
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 문제64번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
result = a if a <b and a< c else (b if b < c else c)
print(result)

# 문제65번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
  print(a)
if b%2==0 :
  print(b) 
if c%2==0 :
  print(c)
