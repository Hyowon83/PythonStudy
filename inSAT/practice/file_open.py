# file = open("D:/menu.txt","w")
# file.write("모카 3500\n라떼 3000\n카푸치노 3700")
# file.close

#같은 방법으로 파일 write 하는 법.
# with open("D:/menu.txt","w") as file:
#     file.write("모카 3500\n라떼 3000\n카푸치노 3700")
#close()를 쓸 필요가 없다.

# file = open("D:/menu.txt","r")
# line = file.read()
# print(line)
# file.close

#같은 방법으로 파일 read 하는 법.
with open("D:/menu.txt","r") as file:
    line = file.read()
    print(line)