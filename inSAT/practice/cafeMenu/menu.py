#### 수정 및 보안(상운오빠)
# class Menu:
#     def __init__(self):
#         self.menuList = []
#         self.priceList = []
#     # def getMenu(self):
#     #     self.name = input("메뉴명 : ")
#     #     self.price = input("가격 : ")
#     def addMenu(self,menuName,menuPrice):
#         self.menuList.append(menuName)
#         self.priceList.append(menuPrice)
#     def printList(self):
#         for i in range(len(self.menuList)):
#             print(self.menuList[i],self.priceList[i])


# import os
# filePath = "c:/tmp"
#         if os.path.isfile("c:/tmp/menu.txt"):
#             mode = "a"
#         else:
#             mode = "w"

# #### saveList 추가(파일 저장)
# class Menu:
#     def __init__(self):
#         self.menuList = []
#         self.priceList = []
#     def addMenu(self, name, price):
#         self.menuList.append(name)
#         self.priceList.append(price)
#     def printList(self):
#         for i in range(len(self.menuList)):
#             print(self.menuList[i],self.priceList[i])
#     def saveList(self):
#         with open("D:/tmp/menu.txt", "w") as file:
#             for i in range(len(self.menuList)):
#                 file.write("{}, {}\n".format(self.menuList[i], self.priceList[i]))


# sentence = "카라멜마끼아또/2000원"
# # 비파괴적 함수, 파괴적 함수
# print(sentence.split("/"))
# print(sentence)

# sentence = sentence[1:]
# print(sentence[1:])
# print(sentence)

# print("Hello World", seq="")


#### 저장된 파일 읽어서 추가하기
class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []
        with open("D:/tmp/menu.txt", "r") as file:   
            for line in file:
                (name, price) = line.strip().split(", ")
                self.menuList.append(name)
                self.priceList.append(price)
                if name  == "":
                    break
        self.printList()

    def addMenu(self, name, price):
        self.menuList.append(name)
        self.priceList.append(price)
    def printList(self):
        for i in range(len(self.menuList)):
            print(self.menuList[i],self.priceList[i])
    def saveList(self):
        with open("D:/tmp/menu.txt", "w") as file:
            for i in range(len(self.menuList)):
                file.write("{}, {}\n".format(self.menuList[i], self.priceList[i]))