from random import randint

n = randint(1, 100)

while True:
    ans = input("번호를 입력해주세요. (Q to exit): ")
    if ans.upper() == "Q":
        break
    ians = int(ans)
    if (n == ians):
        print("정답입니다!")
        break
    elif (n > ians):
        print("업")
    else:
        print("다운")