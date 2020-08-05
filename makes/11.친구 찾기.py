myfrinds = {'a':'가,나', 'b':'다,라,마', 'c':'가,다,바'}

#output
#총 6명
#가 = a,c
#나 = a
#다 = b,c
#...
text = ""
my_friend_set = set()

for i in myfrinds.values():      # '가','나' '다,라,마' '가,다,바'
    my_list = i.split(",")       #     0        1          2
    my_set = set(my_list)
    my_friend_set = my_friend_set | my_set



# 친구들의 수
text = "총 %s명\n" % len(my_friend_set)     #list는 빼도됨

for k in my_friend_set:        #가 나 다 라 마 바
    temp = ""                  #0  1  2  3 4  5
    # "가,나,다"
    for j in myfrinds.keys():
        if k in myfrinds[j]:
            temp = temp + ' ' + j
    text = text + "{} = {}\n".format(k,temp)

print(text)
