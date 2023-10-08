# 문제61번
a, b = map(int, input().split())
result = a | b
print(result)

# 문제62번
a, b = map(int, input().split())
result = a ^ b
print(result)

# 문제63번
a, b = input().split()
a = int(a) 
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 문제64번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
result = a if a <b and a< c else (b if b < c else c)
print(result)

# 문제65번
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

# 문제66번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0 :
    print("even")
else :
    print("odd")
if b%2==0 :
    print("even")
else :
    print("odd")
if c%2==0 :
    print("even")
else :
    print("odd")

# 문제67번
a = input()
a = int(a)
if a<0 :
  if a%2==0 :
    print('A')
  else :
    print('B')
else :
  if a%2==0 :
    print('C')
  else :
    print('D')

# 문제68번
a = input()
a = int(a)

if 90 <= a <= 100:
    print("A")
else:
    if a >= 70:
        print("B")
    else:
        if a >= 40:
            print("C")
        else:
            print("D")

# 문제69번
a = input()
a = str(a)
if a == "A":
    print("best!!!")
else:
    if a == "B":
        print("good!!")
    else:
        if a == "C":
            print("run!")
        else:
            if a == "D":
                print("slowly~")
            else:
                print("what?")

# 문제70번
a = input()
a = int(a)
if 3<=a<=5:
    print("spring")
else:
    if 6<=a<=8:
        print("summer")
    else:
        if 9<=a<=11:
            print("fall")
        else:
            print("winter")
