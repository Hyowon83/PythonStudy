####7주차 마지막 수업(7/10)
# 흐름 익히기
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 호출") # 3. 호출
    
    def test(self):
        print("Parent 클래스의 test 호출")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self) # 2. Parent 클래스의 __init__ 실행
        print("Child 클래스의 __init__ 호출") # 4. Child 클래스의 __init__ 실행


c = Child() # 1. Child 클래스가 실행 ## 5. 결과: 두 줄의 결과가 출력 됨.
c.test()
print(c.value)
