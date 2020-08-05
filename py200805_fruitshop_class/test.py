class A:
    def prn(self):
        print("a")

my_a = A()
my_a.prn()

my_list = []

my_list[0].append(my_a)
my_list[0].prn()

my_list[1].append(my_a)
my_list[1].prn()
my_list[2].append(my_a)
my_list[2].prn()

for i in range(3):
    my_list[i].append(my_a)
