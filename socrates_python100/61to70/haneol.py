def pro61():
    a,b = map(int, input().split())
    c = a|b
    print(c)


def pro62():
    a,b = map(int, input().split())
    c = a^b
    print(c)


def pro63():
    a,b = map(int, input().split())
    c = a-b
    if c>0:
        print(a)
    else :
        print(b)

def pro64():
    a,b,c = map(int, input().split())
    min = a
    if min>b:
        min=b
    if min>c:
        min=c
    print(min)

def pro65():
    inputStr = input()
    number = map(int, inputStr.split())
    for num in number:
        if num%2==0:
            print (str(num))

def pro66():
    inputStr = input()
    number = map(int, inputStr.split())
    for num in number:
        if num%2==0:
            print ("even")
        else:
            print("odd")

def pro67():
    number = int(input())
    if(number<0):
        if(number%2==0):
            print("A")
        else:
            print("B")
    else:
        if(number%2==0):
            print("C")
        else:
            print("D")

def pro68():
    number = int(input())
    if(number>=90): print("A")
    elif(number>=70): print("B")
    elif(number>=40): print("C")
    else: print("D")

def pro69():
    grade = str(input())
    if  grade == 'A':
        print("best!!!")
    elif    grade == 'B':
        print("good!!")
    elif    grade == 'C':
        print("run!")
    elif    grade == 'D':
        print("slowly~")
    else:
        print("what?")

def pro70():
    num = int(input())
    if num // 3 == 0 or num // 3 == 4:
        print("winter")
    if num // 3 == 1:
        print("spring")
    if num // 3 == 2:
        print("summer")
    if num // 3 == 3:
        print("fall")

