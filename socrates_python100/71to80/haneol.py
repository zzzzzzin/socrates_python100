def pro71():
    n=1
    while n!=0:
        n=int(input())
        if(n==0): break
        else: print(n)

def pro72():
    n=int(input())
    while n>0:
        print(n)
        n = n-1

def pro73():
    n=int(input())
    while n>0:
        n = n-1
        print(n)

def pro74():
    t=ord(input())
    c=ord('a')
    while(c<=t):
        print(chr(c), end=' ')
        c += 1

def pro75():
    cnt=0
    num=int(input())
    while(cnt<=num):
        print(cnt)
        cnt+=1

def pro76():
    num=int(input())
    for i in range(num+1):
        print(i)

def pro77():
    num=int(input())
    sum=0
    for i in range(num+1):
        if(i%2==0):
            sum=sum+i
    print(sum)

def pro78():
    while True:
        t=ord(input())
        if(t==ord('q')):
            print(chr(t))
            break
        else: print(chr(t))

def pro79():
    num=int(input())
    cnt=1
    sum=0
    while True:
        if(sum>=num):
            print(cnt-1)
            break
        else:
            sum+=cnt
            cnt+=1

def pro80():
    d1,d2 = map(int, input().split())
    for i in range(d1):
        for j in range(d2):
            print(str(i+1)+' '+str(j+1))

