# str = 'a,1,b,1,a,1'
# temp = ['a','1','b','1','a','1']
# list = [['a','1'],['b','1'],['a','1']]

def chk_item_dupl(list, item):
    for i in range(len(list)):
        if list[i][0] == item[0]:
            return True, i
    return False, None


if __name__ == "__main__":
    data2 = []
    # str = 'a,1,b,1,a,1'
    list = [['a', '1'], ['b', '1'], ['a', '1']]
    for i in range(len(list)):
        item = list[i]
        is_dupl, no_dupl = chk_item_dupl(data2, item)
        if is_dupl:
            data2[no_dupl][1] = item[1] + data2[no_dupl][1]
        else:
            data2.append(item)
        print(is_dupl, no_dupl)
