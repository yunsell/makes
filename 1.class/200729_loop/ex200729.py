gas = int(input("얼마나 넣을까요?... 알아 맞춰보세요.^^"))
while True:
    print("엔진 작동!!!")
    gas = gas - 1
    if gas < 1:
        # break
        gas = int(input("더 넣어요?"))
