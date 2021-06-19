list = [10, 20, 30, 30]

# for i in range(len(list)):
#     if list[i] == 30:
#         del list[i]

# print(list)

# for item in list:
#     print(item)
#     if item == 30:
#         list.remove(item)

# print(list)

distinct = []
for item in list:
    if item != 30:
        distinct.append(item)

list = distinct
distinct = None
print(list)
