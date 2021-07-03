####5주차(6/26)
# 재귀함수로 100까지 더하기
def plus(n):
    if n == 1:
        return 1
    else:
        return n + plus(n-1)

x = plus(100)
print(x)