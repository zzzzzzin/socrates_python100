# 문제 91번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)

# 문제 92번
n = int(input())       # 출석 번호를 몇 번 부를지 입력 받음
a = input().split()    # 각 번호를 공백을 기준으로 나누어 리스트에 저장

for i in range(n):
    a[i] = int(a[i])    # 리스트에 저장된 값을 정수로 변환

d = [0] * 24           # 0으로 초기화된 크기가 24인 리스트 생성

for i in range(n):
    d[a[i]] += 1        # 각 번호에 해당하는 빈도를 1씩 증가

for i in range(1, 24):
    print(d[i], end=' ')  # 1부터 23까지의 빈도 출력

# 문제 93번
n = int(input())      # 출석 번호를 몇 번 부를지 입력 받음
a = input().split()   # 각 번호를 공백을 기준으로 나누어 리스트에 저장

for i in range(n):
    print(a[n - 1 - i], end=' ')

# 문제 94번
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

min_number = min(a)
print(min_number)

# 문제 95번
# 2차원 리스트 초기화
d = [[0 for j in range(20)] for i in range(20)]

n = int(input())

# 흰 돌을 놓은 위치에 1로 표시
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

# 바둑판 출력
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

# 문제 96번

# 문제 97번
# 격자판의 세로(h), 가로(w) 입력
h, w = map(int, input().split())

# 격자판 초기화
board = [[0] * w for _ in range(h)]

# 놓을 수 있는 막대의 개수(n) 입력
n = int(input())

# 각 막대의 정보 입력 및 격자판에 막대 놓기
for _ in range(n):
    l, d, x, y = map(int, input().split())

    # 가로 방향 막대 놓기
    if d == 0:
        for i in range(l):
            board[x - 1][y - 1 + i] = 1
    # 세로 방향 막대 놓기
    else:
        for i in range(l):
            board[x - 1 + i][y - 1] = 1

# 격자판 출력
for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()

# 문제 98번
