# 100명 추첨
# 1등 자동차
# 2~6등 냉장고
# 나머지 꽝

from random import randint

a = 1
b = [2,3,4,5,6]

rr = randint(1, 100)

for i in range(1):
    print(rr)
    if rr == a:
        print("축하합니다 자동차에 당첨 되셨습니다 !!!")
    elif rr in b:
        print("축하합니다 냉장고에 당첨 되셨습니다 !!!")
    else:
        print("다음 기회에...")

