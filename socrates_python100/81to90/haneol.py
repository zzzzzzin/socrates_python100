def pro81():
    n=input()
    hex_value = int(n,16)
    for i in range(1,16):
        print('%X'%hex_value, '*%X'%i, '=%X'%(hex_value*i), sep='')
        
def pro82():
    n=int(input())
    for i in range(1,n+1):
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print("X",end=' ')
        else: 
            print(i,end=' ')

def pro83():
    rgb = input()
    r,g,b = map(int, rgb.split(' '))
    cnt = 0
    
    for i in range(0,r):
        for j in range(0,g):
            for k in range(0,b):
                print(i,j,k)
                cnt += 1
    print(cnt) 

def pro84():
    n = input()
    h,b,c,s = map(float, n.split(' '))
    result = h*b*c*s/8/1024/1024
    print(str(round(result,1))+" MB")

def pro85():
    n = input()
    w,h,b = map(float, n.split(' '))
    result = w*h*b/8/1024/1024
    result = "{:.2f}".format(result)
    print(str(result)+" MB")

def pro86():
    n = int(input())
    i = 1
    sum = 0
    while True:
        if sum >= n:
            print(sum)
            break
        else:
            sum = sum+i
            i = i+1

def pro87():
    n = int(input())
    for i in range(1, n+1) :
        if i%3==0 :
            continue           
        else: print(i, end=' ')  

def pro88():
    adn = input()
    a,d,n = map(int, adn.split(' '))
    sum = d*(n-1)+a
    print(sum)
