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

96
answer = []
for _ in range(19):
    arr = input().split()
    answer.append(arr)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for k in range(19):
        answer[k][y-1] = str(int(not int(answer[k][y-1])))
        answer[x-1][k] = str(int(not int(answer[x-1][k])))
        
for k in answer:
    print(" ".join(k))

97
a, b = map(int, input().split())
matrix = [["0" for _ in range(b)] for _ in range(a)]

for _ in range(int(input())):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(y-1, y+l-1):
            matrix[x-1][i] = "1"
    else:
        for i in range(x-1, x+l-1):
            matrix[i][y-1] = "1"
for k in matrix:
    print(" ".join(k))

98
matrix = []
for _ in range(10):
    matrix.append(input().split())
    
x, y = 1, 1
while x <= 8 and y <= 8:
    if matrix[x][y] == "2":
        matrix[x][y] = "9"
        break
    matrix[x][y] = "9"
    if matrix[x][y+1] == "1" and matrix[x+1][y] == "1":
        break
    elif matrix[x][y+1] == "1":
        x += 1
    else:
        y += 1

for k in matrix:
    print(" ".join(k))
