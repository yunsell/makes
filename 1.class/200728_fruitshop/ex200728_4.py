# input "1,2,3,4,5"
# 3
def my_fn(p1, p2):
    # src = "1,2,3,4,5"
    list = p1.split(",")
    # ['1','2','3','4','5']
    for i in list:
        if i == p2:
            return True
    return False

# 중복이면 True/False
print(my_fn("1,2,3,4,5", "22"))