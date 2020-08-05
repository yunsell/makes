# input "a,1,b,2,a,3"
sales = "a,1,b,2,a,3"
list = sales.split(",")         #문자열 파일을 리스트로 변환
data = []
data2 = []
#print(list)
# list = ['a',1,'b',2,'a',3]

length = len(list) # 6회
for i in range(length):
    # [[]]
    if i % 2 == 1:
        # print(i)
        data.append([list[i-1],int(list[i])])
print(data)


# data = [['a',1],['b',2],['a',3]]
# data2 = [['a',1],['b',2]]
for j in data:        #j에다 data['a',1],['b',2],['a',3]를 넣음
    is_dupl = False
    no_dupl = None
    for k in range(len(data2)):     #k에다가 data2의 인덱스 값을 순서대로
        if data2[k][0] == j[0]:     #만약 data2 [k][0] 번째랑 j[0]째랑 같으면
            is_dupl = True          #이건 참이고
            no_dupl = k             #중복이 아닌건 k 이다
    if is_dupl:
        data2[no_dupl][1] = j[1] + data2[no_dupl][1]
    else:
        data2.append(j)
print("="*30)
print(data2)
