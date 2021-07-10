#### 수정 및 보안(상운오빠)
# import menu as m

# # menu = m.Menu()
# # menu.getMenu()
# # menu.addMenu(menu.name, menu.price)
# # menu.printList()


# cafe = m.Menu()

# while True:
#     cafe.name = input("메뉴 이름:")
#     if cafe.name == "":
#         break
#     cafe.price = int(input("가격: "))
#     cafe.addMenu(cafe.name,cafe.price)

# cafe.printList()



#### 박재형 선생님
import menu

cafe = menu.Menu()

name = input("메뉴명 : ")
while name != "":
    price = input("가격 : ")
    cafe.addMenu(name,price)
    name = input("메뉴명 : ")

cafe.printList()
cafe.saveList()