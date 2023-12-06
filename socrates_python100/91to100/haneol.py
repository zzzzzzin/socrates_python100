def pro91():
    abc = input()
    a,b,c = map(int, abc.split(' '))
    d = 1
    while d%a!=0 or d%b!=0 or d%c!=0 :
        d += 1
    print(d)

def pro92():
    n = int(input())      
    a = input().split(' ') 

    for i in range(n) : 
        a[i] = int(a[i]) 
    
    d = []                    
    for i in range(24) :  
        d.append(0)       

    for i in range(n) :    
        d[a[i]] += 1

    for i in range(1, 24) :  
        print(d[i], end=' ')

def pro93():
    n = int(input())      
    a = input().split()  

    reversed_list = a[::-1]

    for i in range(n) :  
        print(reversed_list[i], end=' ')

def pro94():
    n = int(input())      
    a = input().split(' ')
    min = int(a[0]) # int로 변환하는게 중요
    for i in range(1,n):
        if int(a[i]) < min:
            min = int(a[i])
    print(min)

def pro95():
    #바둑판 만들기
    d = [[0 for j in range(20)] for i in range(20)]

    #바둑돌 놓기
    n = int(input())
    for i in range(n) :
        x, y = input().split()
        d[int(x)][int(y)] = 1
    
    for i in range(1, 20) :
        for j in range(1, 20) : 
            print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
        print()

def pro96():
    # 바둑판 만들기
    d = [[0 for j in range(20)] for i in range(20)]

    # 입력값 적용
    for i in range(19):
        row_input = input().split()
        for j in range(19):
            d[i + 1][j + 1] = int(row_input[j])

    #십자뒤집기
    n = int(input())
    for i in range(n) :
        x, y = input().split()
        for j in range(1,20):
            if(d[int(j)][int(y)] == 0):
                d[int(j)][int(y)] = 1
            else: d[int(j)][int(y)] = 0

            if(d[int(x)][int(j)] == 0):
                d[int(x)][int(j)] = 1
            else: d[int(x)][int(j)] = 0 
    #출력
    for i in range(1, 20) :
        for j in range(1, 20) : 
            print(d[i][j], end=' ')   
        print()

def pro97():
    #뽑기판 만들기
    a, b = map(int, input().split())
    board = [[0 for j in range(b)] for i in range(a)]
    #뽑기 놓기
    n = int(input())
    for i in range(n) :
        l, d, x, y = map(int, input().split())
        if d == 0: #가로
            for j in range(0,l):
                board[int(j+x)][int(y)] = 1
        else: #세로
            for k in range(0,l):
                board[int(x)][int(y-k)] = 1
    #출력하기
    for i in range(a) :
        for j in range(b) : 
            print(board[i][j], end=' ') 
        print()