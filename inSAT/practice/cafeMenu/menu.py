class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []
    # def getMenu(self):
    #     self.name = input("메뉴명 : ")
    #     self.price = input("가격 : ")
    def addMenu(self,menuName,menuPrice):
        self.menuList.append(menuName)
        self.priceList.append(menuPrice)
    def printList(self):
        for i in range(len(self.menuList)):
            print(self.menuList[i],self.priceList[i])