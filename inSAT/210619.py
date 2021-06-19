####4주차(6/19)

#list는 CRUD 가능(데이터 전달 및 연산용)
a = [1,2,3,4] #C
b = ['a','bc',30] #C
c = a+b #U
print(c) #R
print()

#tuple은 CRD 가능(데이터전달용)
z = (1,2,3) #c
y = 4,5,6 #c
print(z[2]) #R
print()

#set은 중복X,순서X => index가 없음 CUD가능
z = set([1,2,3]) #집합형 변수(set) #C
y = set([1,2,3,0,2,3]) #C 중복값 못 씀.
print(y) #R 불가능. index로 결과가 나오지 않음.
z.add(5) #U
print(z)
y.remove(2) #D
print(y)
#합집합(|) 교집합(&) 차집합(-)
a=set([1,2,3,4])
b=set([3,4,5,6])
c=a|b
print(c)
c=a&b
print(c)
c=a-b
print(c)
print()

#dictionary는 key:value로 이루어짐. (자바스크립트의 객체(Object)와 비슷)
#파이썬에선 key값을 무조건 문자열로, '' 혹은 ""로 감싸줘야한다.
a = {'name':'Hyowon','age':25, 'live in':'Cheonan'}
print(a)
b = {'name':'Hyowon','name':'Python'} #key 중복 안됨. 마지막 키만 인식.
print(b)
print()

class1 = [{'name':'John','math':90,'science':85,'eng':60},{'name':'James','math':70,'science':90,'eng':85}]
print(class1[0]['name']) #class1의 인덱스 0번의 'name'의 밸류값
class1[1]['math'] = 80 #U class1의 인덱스 1번의 수학값을 바꿀 수 있다.
print(class1)
print()

class2 = []
class2.append({'name':'Joshua'}) #.append로 추가 가능. .add는 안된다.
print(class2)
class2.insert(0,{'name':'Max'}) #.insert로 순서를 정해서 추가 할 수 있다.
print(class2)