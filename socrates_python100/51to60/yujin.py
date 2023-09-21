#51
print("첫번째 값을 입력하시오: ")
a = input()

print("두번째 값을 입력하시오: ")
b = input()

print("순서대로 "+a+", "+b+" 입니다")

if a == b:
    print("TRUE")
else:
    print("FALSE")

#52
print("값을 입력하시오: ")
a = bool(int(input()))
print(not a)

#53
print("값을 입력하시오: ")
a = bool(int(input()))
print(a)

#54
print("두개의 정수를 띄어서 입력하시오: ")
a, b=input().split()

x=bool(int(a))
y=bool(int(b))

if x and y == True:
  print(True)
else: print(False)

#55
print("두개의 정수를 띄어서 입력하시오: ")
a, b=input().split()

x=bool(int(a))
y=bool(int(b))

if x or y == True:
  print(True)
else: print(False)

#56
print("두개의 정수를 띄어서 입력하시오: ")
a, b = input().split()

x = bool(int(a))
y = bool(int(b))

z = x ^ y
print(z)

#57
print("두개의 정수를 띄어서 입력하시오: ")
a, b = input().split()

x = bool(int(a))
y = bool(int(b))

z = x ^ y
print(not z)

#58
print("두개의 정수를 띄어서 입력하시오: ")
a, b = input().split()

x = bool(int(a))
y = bool(int(b))

z = not x and not y
print(z)

#59
print("하나의 정수를 입력하시오: ")
a = int(input())
x = ~a
print(x)

#60

