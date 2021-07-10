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



#### saveList 추가(파일 저장)
class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []
    def addMenu(self,menuName,menuPrice):
        self.menuList.append(menuName)
        self.priceList.append(menuPrice)
    def printList(self):
        for i in range(len(self.menuList)):
            print(self.menuList[i],self.priceList[i])
    def saveList(self):
        self.file = open("D:/menu.txt","w")
        for i in range(len(self.menuList)):
            self.file.write("{}: {}\n".format(self.menuList[i],self.priceList[i]))
        self.file.close