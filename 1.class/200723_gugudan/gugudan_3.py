# 반복문
for i in [1,2]:
    print(i)

print("="*50)
print("2단 출력하기")
file1 = open('2dan.txt', 'w', encoding='utf8')
for i in [1,2,3,4,5,6,7,8,9]:
    data = " 2 x %d = %2d\n" % (i, i*2)
    # 화면에 출력
    print(data)
    # 파일에 기록
    file1.write(data)
file1.close()

# 반복문(외부)에 반복문(내부)를 넣으면 외부 반복 횟수만큼 내부 반복이 된다.
# 1에 대해 a,b,c가 2에 대해 다시  a,b,c가 반복된다.
# 반복문 내에서 변수는 중복되지 않아야 한다.
# 즉 외부 반복에 i가 내부 반복문에 다시 사용되지 않아야 한다.
for i in [1,2]:
    print(i)
    for j in ["a","b","c"]:
        print(j)
    print("*" * 10)

# 구구단 만들기
print("="*50)

file2 = open('99dan.txt', 'w')
for i in [2,3,4,5,6,7,8,9]:
    for j in [1,2,3,4,5,6,7,8,9]:
        data = "%d x %d = %2d\n" % (i, j, i*j)
        # 화면에 출력
        print(data)
        # 파일에 기록
        file2.write(data)
file2.close()

# 반복문을 3번 중첩사용한다면
for i in [1]:
    for j in ["a"]:
        for k in ["가"]:
            print(i,j,k)


print("="*50)
for i in [2,3,4,5,6,7,8,9]:
    for j in [1,2,3,4,5,6,7,8,9]:
        print(i,j)

# 234, 567, 89 구구단 가로로 표현하기
file3 = open('hor99dan.txt', 'w')
for i in [2,5,8]:
    for j in [1,2,3,4,5,6,7,8,9]:
        if i == 8:
            data = "%d x %d = %2d   %d x %d = %2d\n" % (
                i, j, i*j, i+1, j, (i + 1) * j)
        else:
            data = "%d x %d = %2d   %d x %d = %2d   %d x %d = %2d\n" % (
            i, j, i * j, i + 1, j, (i + 1) * j, i + 2, j, (i + 2) * j)
        # 화면에 출력
        print(data)
        # 파일에 기록
        file3.write(data)
file3.close()