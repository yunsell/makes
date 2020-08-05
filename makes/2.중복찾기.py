s = "1,2,3,4"
i = "2"

def find(ps, pi):          #find 함수를 만듬 (s=ps , i=pi)
    temp = False           #temp = False 칸을 만듬
    list = ps.split(",")   #list 칸을 만든후 ps를 split해서 ,를 없앰
    for a in list:         #list를 한번씩 돌림 그걸 a라고함
        if a == pi:        #만약 a(list)가 pi와 같을경우 True
            temp = True
    return temp

r = find(s, i)
print(r)