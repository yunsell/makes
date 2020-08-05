# 짝수 "5,7,4,9,6,3,15" 7개
# 홀수 "5,7,4,9,6,3,15,21" 8개

data = "5,7,4,9,6,3,15"
length = None
data_list = data.split(",")
# 정렬
new_list =[]
for i in data_list:
    new_list.append(int(i))
new_list.sort()
# 홀수와 짝수를 구분
length = len(new_list)

temp = False # 홀수
if length % 2 == 0:
    temp = True

print(temp)

# 중위값을 출력
m_idx = int(length/2)
if temp:
    add = new_list[m_idx-1] + new_list[m_idx]
    median = add / 2
    print(median)
else:
    median = new_list[m_idx]
    print(median)