# 파일을 만든다.
f = open('new_01.txt', 'w', encoding='utf8')
for i in range(1,11):
    txt = "점심을 많이 먹으면 졸립다ㅠㅠ\n"
    f.write(txt)
f.close()

# 파일을 다시 읽는다.
f = open('new_01.txt', 'r', encoding='utf8')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()