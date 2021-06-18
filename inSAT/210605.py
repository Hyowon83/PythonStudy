####2주차(6/5)
# IDE(Integrated Development Environment): 통합개발환경

# .upper .lower 함수(메소드)
x="Hello"
print(x)
print(x.upper()) # x를 전부 대문자로 출력
print(x.lower()) # x를 전부 소문자로 출력
x=x.upper()      # x를 전부 대문자로 저장
print(x)
print()


# .strip 공백 없애기
x="     Hello World     "
print('['+x+']')
print('['+x.strip()+']')  # 앞 뒤 공백 없애기
print('['+x.lstrip()+']') # 왼쪽 공백 없애기
print('['+x.rstrip()+']') # 오른쪽 공백 없애기
print()


# 모든 문자열은 배열이다.(인덱스 번호를 갖는다.)
# .find
x="Hello World"
y="안녕안녕안녕하세요"
print(x[0])
print(x[5])
print(y[6])
print(x.find('ll')) # ll의 시작 위치를 인덱스 번호로 출력. = 2
print(y.find('안녕')) # = 0
print(y.rfind('안녕')) # 문자가 중복일 때 마지막 위치를 출력
print()


# .in (contain 포함)
# 문자열 자르기
str="10 20 30 40 50"
ar=str.split() # 결과물이 리스트 형태로 나옴.
print(str)
print(ar)
str="10,20,30,40,50"
ar=str.split() # 아무것도 설정하지 않으면 공백을 기준으로 나눔.
print(ar)
str="10,20,30,40,50"
ar=str.split(',') # ,를 기준으로 나누라고 설정.
print(ar) # ,를 포함하지는 않음.
print()


# 부울대수(Boolean)
# 문자열 비교는 사전에 나오는 순서에 따른다. 사전에 먼저 나오는 글자가 더 작음.( "a" < "z"/"a" < "aa" )
# 문바열 비교: " " < "1234..." < "ABC..." < "abc..."
# 논리비교
# == != > < >= <=
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print()
a=5
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print()
a=5
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print()

# 논리연산
# AND OR NOT


# if문(alternate 선택적)
####과제
# 1) 두 값을 읽어들임(x,y) 2)x가 y보다 작으면 x출력 3)그렇지 않으면 y출력
# input('값을 입력하세요. : ')
# x=input('x값을 입력하세요. : ')
# x=int(x)
# y=input('y값을 입력하세요. : ')
# y=int(y)
# if x<y:
#     print(x)
# else:
#     print(y)


# 조건이 더 많다면, elif를 사용한다.
# x=input('x=')
# x=int(x)
# if x%3==0:
#     print(x,"는 3의 배수")
# elif x%5==0:
#     print(x,"는 5의 배수")
# elif x%2==0:
#     print(x,"는 2의 배수")
# else:
#     print(x,"해당하는 조건이 없음.")
# print() 