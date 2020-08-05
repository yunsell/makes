myfriends = {'a':'가,나','b':'다,라,마','c':'가,다,바'}

text = ""
my_friend_set = set()

for i in myfriends.values():
    # [1,2] => {1,2} => 합집합
    my_list = i.split(",")
    my_set = set(my_list)
    my_friend_set = my_friend_set | my_set


# 친구들의 수
text = "총 %s명\n" % len(list(my_friend_set))


for k in my_friend_set:
    print(k)
    temp = ""
    # "가,나,다"
    for j in myfriends.keys():
        if k in myfriends[j]:
            temp = temp+','+j
        print(j)
    text = text + "{} = {}\n".format(k,temp)


print(text)