61
print("두개의 정수를 입력하시오: ")
a, b = map(int, input().split())
x = a | b
print(x)

62
print("두개의 정수를 입력하시오: ")
a, b = map(int, input().split())
x = a ^ b
print(x)

63
print("두개의 정수를 입력하시오: ")
a, b = input().split()
a = int(a)
b = int(b)
x = (a if(a>=b) else b)
print (int(x))

64
print("세개의 정수를 입력하시오: ")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
x = (a if(a>=b) else b) if ((a if(a>=b) else b)>c) else c
print (int(x))

65
print("세개의 정수를 입력하시오: ")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
  print(a)

if b%2==0 :
  print(b)

if c%2==0 :
  print(c)

66
print("세개의 정수를 입력하시오: ")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
  print ("1: even")
else :
  print ("1: odd")
  
if b%2==0 :
  print ("2: even")
else :
  print ("2: odd")

if c%2==0 :
  print ("3: even")
else :
  print ("3: odd")

67
print("0이 아닌 하나의 정수를 입력하시오: ")
a = int(input())

if a<0 :
  if a%2==0:
    print("A")
  else :
    print("B")
else :
  if a%2==0 :
    print("C")
  else :
    print("D")

68
print("0~100 사이의 정수를 입력하시오: ")
a = int(input())

if a>=90 :
  print("A")
else :
  if a>=70:
    print("B")
  else :
    if a>=40:
      print("C")
    else :
        print("D")

69
print("A,B,C,D 중 하나를 입력하시오: ")
a = str(input())

if a=="A" :
  print("best!!!")
else :
  if a=="B":
    print("good!!")
  else :
    if a=="C":
      print("run")
    else :
      if a=="D":
        print("slowly!")
      else :
        print ("what?")

70
print("1~12중 하나를 입력하시오: ")
a = int(input())

if a//3==1:
  print("spring")
else :
  if a//3==2:
    print ("summer")
  else :
    if a//3==3:
      print ("fall")
    else :
      print("winter")
