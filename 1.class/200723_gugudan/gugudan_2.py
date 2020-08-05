# 파일을 생성
f = open("gugudan.txt", 'w', encoding='utf8')
f.write("2단\n")
f.write("=" * 5)
f.write("\n")
# f.write("2 x 1 = 2\n")
# f.write("2 x 2 = 4\n")
# 1-9까지 반복
for a in [1,2,3,4,5,6,7,8,9]:
    print(2, "x", a, "=", a * 2)
    f.write("2 x %d = %d\n" % (a, 2*a))
f.close()

