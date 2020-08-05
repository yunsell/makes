data = "a,1,b,2,c,3,a,4,b,3,a,2"
data_list = data.split(",")
# 최종 결과는 sum_list = ["a=5","b=5","c=3"]으로 만든다.
sum_list = []

# 아이템이 중복되었는지 확인
# 중복되면 인덱스 값을 전달, 중복되지 않으면 -1
def chk_dup_item(list, item):
    length = len(list)
    for i in range(length):
        # a=5에서 a를 추출하여 name에 담고 item과 비교
        name = list[i][:list[i].find("=")]
        if item == name:
            return i
    return -1

# 아이템과 수량을 순서대로 가져와 수량을 계산한다.
data_list_length = len(data_list)

for i in range(data_list_length):
    # 홀수 인 경우에만 상품과 수량을 계산하여 추가한다.
    if i%2 == 1:
        n = data_list[i-1]
        c = data_list[i]
        # 이미 등록된 상품이 있는 경우
        idx = chk_dup_item(sum_list, n)
        if idx > -1:
            str = sum_list[idx]
            sum = int(str[str.find("=")+1:]) + int(c)
            sum_list[idx] = "%s=%d" % (n,sum)
        # 처음 등록된 상품인 경우
        else:
            sum_list.append("%s=%s" % (n, c))

print(sum_list)