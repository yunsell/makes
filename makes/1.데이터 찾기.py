data = [1,2,3,4,5]

a = 3
def myfn(list, num):
    result = None

    for i in list:
        if i == num:
            result = True
            print("찾았다")

    if not result:
        result = False
        print("못찾음")
    return result

print(myfn(data, a))
