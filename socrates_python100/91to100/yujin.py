6091.
a, b, c = map(int, input().split())

d = 1

while d%a or d%b or d%c:
    d += 1
    
print(d)


6092.
n = int(input())
ranN = list(map(int, input().split()))

answer = [0 for _ in range(23)]

for k in ranN:
    answer[k-1] += 1

print(" ".join(list(map(str, answer))))


6093. 


6094.
n = int(input())
ranN = list(map(int, input().split()))

print(min(ranN))


6095.
n = int(input())

answer = [["0" for _ in range(19)] for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    answer[x-1][y-1] = "1"
    
for k in answer:
    print(" ".join(k))


6096. 


6097. 


6098.
