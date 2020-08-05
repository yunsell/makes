for i in ["200R0131Rainy", "179RaiRR354ny", "21R354yn76"]:
    count = 0
    for j in i:
        # count = count + 1
        if j == "R":
            print(i[:count])
            print(i[count:])
        count = count + 1