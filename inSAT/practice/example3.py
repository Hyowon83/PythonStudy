
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(list))

dict = {"영어 점수":100,"수학 점수":100,"과학 점수":100}
print(sum(dict.values()))

dict2 = [{"영어 점수":100,"사회점수":80},{"수학 점수":100},{"과학 점수":100}]
print(sum(dict2[0].values()))