# [['a', 3], ['b', 6], ['c', 2], ['r', 1]]

source = [['a', 3], ['b', 6], ['c', 2], ['r', 1]]
with open('202007.csv', 'w', encoding='utf8') as f:
    for i in source:
        f.write("{0},{1}\n".format(i[0],i[1]))