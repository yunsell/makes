from py200805_fruitshop_class.mydir import MyDir
from py200805_fruitshop_class.mysale import MySale

my_dir_0701 = MyDir("200701")
my_dir_0701_list = []
for i in my_dir_0701.files:
    my_dir_0701_list.append(MySale("{}/{}".format(my_dir_0701.dir,i)))

print(my_dir_0701_list)






#my_dir_0702 = MyDir("200702")
#print(my_dir_0702.files)
#my_dir_0703 = MyDir("200703")
#print(my_dir_0703.files)
