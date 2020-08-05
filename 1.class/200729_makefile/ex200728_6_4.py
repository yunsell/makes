def transform_data(sales_data):
    data = []
    temp_list = sales_data.split(",")
    for i in range(int(len(temp_list) / 2)):
        data.append([temp_list[i * 2], int(temp_list[i * 2 + 1])])
    return data


def chk_item_dupl(list, item):
    for i in range(len(list)):
        if list[i][0] == item[0]:
            return True, i
    return False, None


def calc_total(main_list, sub_list):
    for i in range(len(sub_list)):
        item = sub_list[i]
        is_dupl, no_dupl = chk_item_dupl(main_list, item)
        # is_dupl = True, no_dupl = 2
        if is_dupl:
            main_list[no_dupl][1] = item[1] + main_list[no_dupl][1]
        else:
            main_list.append(item)


if __name__ == "__main__":
    data2 = []

    s1 = "a,1,b,2,a,3"
    s2 = "s,2,d,5,f,3,s,1"
    s3 = "a,2,f,5,s,4,d,2"
    sales = [s1, s2, s3]

    for sale in sales:
        list = transform_data(sale)
        calc_total(data2, list)

    print(data2)
