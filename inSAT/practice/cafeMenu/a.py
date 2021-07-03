import menu as m

# menu = m.Menu()
# menu.getMenu()
# menu.addMenu(menu.name, menu.price)
# menu.printList()


cafe = m.Menu()

while True:
    cafe.name = input("메뉴 이름:")
    if cafe.name == "":
        break
    cafe.price = int(input("가격: "))
    cafe.addMenu(cafe.name,cafe.price)

cafe.printList()