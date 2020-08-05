from lib.fruit import feat1

feat1("a,2,d,3,g,7,t,5")

# input 1,2,3
def increase_one(param):
    # param = "1,2,3,4,5"
    new_param = param.split(",")
    # "12345" or [1,2,3,4,5]
    # [2,3,4,5,6] -> "2,3,4,5,6"
    temp = []
    for n in new_param:
        temp.append(str(int(n)+1))
    '''
    1 + 1
    2 + 1
    3 + 1
    4 + 1
    5 + 1
    '''
    ",".join(temp)
    return temp
# output 2,3,4
myval = increase_one("7,8,9")
print(myval)