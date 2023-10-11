71
n = 1    
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)

72
n = int(input())
while n!=0 :
  print(n)
  n = n-1

73
n = int(input())
while n!=0 :
  n = n-1
  print(n)

74
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

75
n = int(input())
i = 0
while n>=i :
  print(i)
  i=i+1

76
n = int(input())
for i in range(n+1) :
  print(i)

77
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i

print(s)
