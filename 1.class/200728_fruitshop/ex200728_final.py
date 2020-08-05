data2 = []

def translate_data(sales_data):
    data = []
    temp_list = sales_data.split(",")
    for i in range(int(len(temp_list)/2)):
        data.append([temp_list[i*2],int(temp_list[i*2+1])])
    return data

def chk_item_dupl(list, item):
    for i in range(len(list)):
        if list[i][0] == item[0]:
            return True, i
    return False, None

f = open("..\\hello.txt", "r")
f2 = open("..\\testtext.txt", "r")
a = f.readline()

sales3 = f.readline()
sales2 = f2.readline()


if __name__ == "__main__":
    sales = "a,1,b,2,a,3"



    list = translate_data(sales)

    for i in range(len(list)):
        item = list[i]
        is_dupl, no_dupl = chk_item_dupl(data2, item)
        # is_dupl = True, no_dupl = 2
        if is_dupl:
            data2[no_dupl][1] = item[1] + data2[no_dupl][1]
        else:
            data2.append(item)
    print(data2)
