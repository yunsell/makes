data = [1,2,3,4,5]

a = 3
# a = 31
def myfn(list, num):
    result = None

    for i in list:
        if i != num:
            result = True
            print("bingo")

    if not result:
        result = False
    return result

print(myfn(data, a))