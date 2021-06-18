#### 1주차(5/29)
# 변수? 메모리의 특정공간 #한번에 마지막에 넣은 하나의 값만 보관
x=3 
y=5
print(x)
print(y)
print(x+y)
print(x*y)
x="Hello"
print(x)
x=3.14
print(x)
print() # 한 줄 띄우기


# 값을 출력하는 두가지 방법
x="Hello"
print(x) # 변수 지정 후 변수 불러오기
print("Hello") # 그냥 출력하기
print()


# 변수의 종류
n=3 # 정수형[Integer: int] 변수 #int n=3 #하지만 파이썬에선 정의하지 않고 그냥 n=3이라고만 써도 된다.
print(type(n))
f=3.14 # 실수[소수점 *Floating Point Number*,Real Number: float]형 변수 #int f=3.14 //error
print(type(f))
s="Hello" # 문자열(형) 변수
print(type(s))
print()


# 나누기의 몫과 나머지
print(10/3)
print(10//3) # 몫
print(10%3) # 나머지
print()


# '+' 연결연산자 혹은 더하기
x="Hello"
y="World"
print(x+y) # 문자열 연결연산자
a=3
b=5
print(a+b) # 더하기
print("a"+"b") # ""로 문자열만들기
# print(x+a) #다른 형태의 더하기는 error
print()


# 띄어쓰기
x="Hello"
y="World"
print(x+" "+y) # 공백사용
print(x, y) # , 사용
print("헬로","파이썬")
print(10,20,30,40,50)
print()


# '*' 정수와 문자열
x=3
print(x*"Hello") # 모든 연산자는 서로 다른 타입끼리 사용 못하지만, *은 예외.
print('-'*40) # 응용 #정수와 문자열의 위치는 상관없이 '문자열'의 '정수'개 반복.
print()


####1주차 첫번째 과제####
# 변수1에 13을 넣고, 변수2에 25를 넣은 다음, 두 개의 합, 곱, 나머지를 출력.
# 출력결과: (변수1) = 13 , (변수2) = 25 , sum = 48 , multi = 9999 , rem = 999
x=13
y=25
print("x =",x)
print("y =",y)
print("sum =",x+y)
print("multi =",x*y)
print("rem =",x%y)
print("한줄에 쓰기 :",'x =',x,', y =',y,", sum =",x+y,", multi =",x*y,", rem =",x%y)
print()


# 교재 p77 원의 둘레와 넓이 구하기
pi=3.14159265
r=10
print("원주율 =",pi)
print("반지름 =",r)
print("원의 둘레 =",2*pi*r)
print("원의 넓이 =",pi*r*r)
print()


# format
print("{},{}".format(10,5)) # :d(decimal 십진수,정수) :f(floating-point number 실수)