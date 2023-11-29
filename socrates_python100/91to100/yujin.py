86
n = int(input())

sum = 0
for i in range(1, n+1):
    if sum >= n:
        break
    sum += i
    
print(sum)

87
n = int(input())

for k in range(1, n+1):
    if k % 3:
        print(k, end=" ")

88
a, d, n = map(int, input().split())

print(a + d * (n-1))

89
a, r, n = map(int, input().split())

print(a * r**(n-1))

90
a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a * m + d
print(a)

91
a, b, c = map(int, input().split())
d = 1
while d%a or d%b or d%c:
    d += 1
print(d)

92
n = int(input())
ranN = list(map(int, input().split()))
answer = [0 for _ in range(23)]
for k in ranN:
    answer[k-1] += 1
print(" ".join(list(map(str, answer))))

93
n = int(input())
ranN = input().split()

for i in range(n-1, -1, -1):
    print(ranN[i], end=" ")

94
n = int(input())
ranN = list(map(int, input().split()))

print(min(ranN))

95
n = int(input())
answer = [["0" for _ in range(19)] for _ in range(19)]
for i in range(n):
    x, y = map(int, input().split())
    answer[x-1][y-1] = "1"
    
for k in answer:
    print(" ".join(k))
