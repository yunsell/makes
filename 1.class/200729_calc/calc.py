sum = None


def my_four_cal(sum, param):
    result = sum
    if "+" in param:
        result = sum + int(param[1:])
    elif "-" in param:
        result = sum - int(param[1:])
    elif "*" in param:
        result = sum * int(param[1:])
    elif "/" in param:
        result = sum / int(param[1:])
    return result


while True:
    if not sum:
        sum = int(input("입력...>"))
        print("sum이 {}입니다.".format(sum))
        # break
    txt = input("입력...>")
    print("{}를 계산합니다.".format(txt))
    sum = my_four_cal(sum, txt)
    print(sum)
    if txt == 'q':
        break

