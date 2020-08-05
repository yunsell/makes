i = 0

f = open("e:\\2dan.txt", "w", encoding="utf8")

while i < 9:
    i = i + 1
    print("2 x", i, "=", 2*i)
    j = 2*i
    data = "2 x %d = %d\n" % (i,j)
    # data = "2 x %d = %d\n" % (i, 2*i)
    f.write(data)

f.close()