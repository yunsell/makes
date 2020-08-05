# input
s = "1,2,3,4"
i = "22"

def findItem(pl, pi):
    temp = False
    for i in pl:
        if i == pi:
            temp = True
    return temp

# def return True/False
def chk_dupl(ps, pi):
    temp = False
    list_s = ps.split(",")
    # list_s = ["1","2","3","4"]
    # list_s.count(pi) 찾은 갯수를 반환하지만 오류가 발생할 수 있음.
    # if ps.find(pi) > -1:
    if findItem(list_s, pi):
        temp = True
    # else:
    #     temp = False
    return temp

# output
r = chk_dupl(s,i)
print(r)