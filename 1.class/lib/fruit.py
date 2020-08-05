# 상품명,수량으로 이루어진 문자열을 받아 2차원 리스트를 만들어 반환
# data = [['a',1],['b',1],['c',1],['a',1],['d',1],['f',1],['c',1]]
def feat1(param):
    data = []
    # 인덱스 번호를 i에 담는다
    temp = param.split(',')
    for i in range(len(temp)):
        if i % 2 == 1:
            print(i, [temp[i - 1], int(temp[i])])
            data.append([temp[i - 1], int(temp[i])])

    print(data)
    print("=" * 30)

    return data
