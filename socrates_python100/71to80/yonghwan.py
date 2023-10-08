# 문제71번
n = 1    
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)

# 문제72번
n = input()
n = int(n)
while n!=0 :
  print(n)
  n = n-1

# 문제73번
n = input()
n = int(n)
while n!=0 :
  n = n-1
  print(n)

# 문제74번
value = ord(input())
t = ord('a')
while t <= value:
    print(chr(t), end=" ")
    t = t+1

# 문제75번
a = int(input())
t = 0
while t <= a:
    print(t)
    t = t+1

# 문제76번
n = int(input())
for i in range(n+1) :
  print(i)

# 문제77번
n = int(input())
a = 0
for i in range(n+1):
    if i % 2 == 0:
        a=a+i
print(a)

# 문제78번
key = str(input())
while key != "q":
    print(key)
    key = str(input())
else:
    print(key)

# 문제79번
value = int(input())
total = 0

for i in range(value+1):
    i = i+1 
    total = total + i
    if total >= value:
        print(i)
        break

# 문제80번
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    for r in range (1, m+1):
        print(i,r)
