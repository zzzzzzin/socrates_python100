81
a = input()
for i in range(1, 16):
    b = str(hex(int(a, 16)*i))[2:]
    b = b.upper()
    print(a+'*'+str(i)+'='+b)

82
n = list(map(str, range(1, int(input())+1)))

for i in n:
    if "3" in i or "6" in i or "9" in i:
        n[n.index(i)] = "X"
        
print(" ".join(n))

83
a, b, c = map(int, input().split())
d = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            d+=1
print(d)

84
h, b, c, s = map(int, input().split())
print('%.1f MB' % (h*b*c*s/8/1024/1024))

85
w, h, b = map(int, input().split())
print('%.2f MB' % (w*h*b/8/1024/1024))
