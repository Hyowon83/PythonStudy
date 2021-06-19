# x=input('x값을 입력하세요. : ')
# x=int(x)
# y=input('y값을 입력하세요. : ')
# y=int(y)
# if x<y:
#     print(x)
# else:
#     print(y)
# print()


# a=input('a=')
# a=int(a)
# b=input('b=')
# b=int(b)
# if a==b*4:
#     print(a)
# else:
#     print(b)
# print()


# val=input('값을 입력하세요. : ')
# val=int(val)
# if val%3==0:
#     print(val,"입력한 값은 3의 배수입니다.")
# else:
#     print(val,"입력한 값은 3의 배수가 아닙니다.")


# z=input('값을 입력하세요. : ')
# z=int(z)
# if z%3==0 and z%2==0:
#     print(z,"입력한 값은 3과 2의 공배수입니다.")
# else:
#     print(z)


# for i in range(0,13,2):  //0부터 12까지 2씩 증가
# 	print(i)

# for i in range(13,0,-2):  //13부터 1까지 2씩 감소
# 	print(i)

# for i in range(3,101,3):  //3부터 100까지 3의배수
# 	print(i)

# n = int(input()) + 1
# sum = 0
# for i in range(1, n):  //1부터 입력받은 값까지의 전체 합
#     sum += i

# print(sum)

# sum = 0
# for i in range(1,101): //1부터 100까지의 전체 합
#     sum = sum + i

# print(sum)


# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i + 1

# print(sum)


# i=-1
# while i < 30:
#     print(i)
#     i = i + 3


# #구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         #print(i,' * ',j,' = ',i*j)
#         print("{} * {} = {}".format(i, j, i * j))
#     print()


# #구구단2
# i = 2
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print("{} * {} = {}".format(i, j, i * j))
#         j = j + 1
#     i = i + 1
#     print()


#### 6/19
# student = []
# n = input('이름 : ') # 홍길동
# while n != '':
#     student.append({'name':n})
#     n = input('이름 : ')

# print(student)


# student = []
# while True:
#     # 학생의 이름을 입력받는다.
#     name = input()
#     if name == "": # 학생의 이름이 빈 문자열이라면 종료
#         break
#     else: # 빈 문자열이 아니라면 딕셔너리에 추가한다.
#         student.append({"name": name})

# print(student)


# 각 학생의 이름, 영어점수, 수학점수를 입력받고
# 각 학생정보는 딕셔너리에 모든 학생은 리스트에 저장하세요 
# students = []
# studentsList = []
# name = input('이름 : ')
# eng = input('영어점수 : ')
# math = input('수학점수 : ')
# allStudent = 0
# engTotal = 0
# mathTotal = 0
# while name != '':
#     students.append({'name':name,'영어점수':eng,'수학점수':math})
#     studentsList.append(name)
#     name = input('이름 : ')
#     eng = float(eng)
#     math = float(math)
#     allStudent += 1
#     engTotal += eng
#     mathTotal += math
#     if name == '':
#         break
#     else:
#         eng = input('영어점수 : ')
#         math = input('수학점수 : ')
    
# print(students)
# print(studentsList)
# print("영어점수와 수학점수의 총 합: ",engTotal+mathTotal)
# print("영어 평균: ",engTotal/allStudent)
# print("수학 평균: ",mathTotal/allStudent)

#2
students = []
scores = [0.0, 0.0, 0.0, 0.0]
ENG_TOTAL = 0
MATH_TOTAL = 1
ENG_AVG = 2
MATH_AVG = 3


while True:
    name = input("이름: ")
    if name == "":
        break
    mat = float(input("수학 점수: "))
    eng = float(input("영어 점수: "))
    students.append({"이름": name, "수학 점수": mat, "영어 점수": eng})

for student in students:
    scores[MATH_TOTAL] += student["수학 점수"]
    scores[ENG_TOTAL] += student["영어 점수"]

scores[MATH_AVG] = scores[MATH_TOTAL] / len(students)
scores[ENG_AVG] = scores[ENG_TOTAL] / len(students)

print("수학 점수의 총합: {}".format(scores[MATH_TOTAL]))
print("영어 점수의 총합: {}".format(scores[ENG_TOTAL]))
print("수학 점수의 평균: {}".format(scores[MATH_AVG]))
print("영어 점수의 평균: {}".format(scores[ENG_AVG]))

#3 함수로 표현하는 방법
student = []
def getPoint(x):
    eng = input('영어점수: ')
    mat = input('수학점수: ')
    d = {'name':x,'영어점수: ':eng,'수학점수: ':mat}
    return d #실행된 함수의 결과를 반환해서 사라지지 않게한다.

while True:
    name = input('이름: ')
    if name == '':
        break
    student.append(getPoint(name)) #위에 정의된 함수 x자리에 name값을 넣는다. #return된 d값이 getPoint(name)에 들어간다.

print(student)