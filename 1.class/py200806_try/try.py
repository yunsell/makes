try:
    a = 4/0
    print(a)
except ZeroDivisionError as e:
    print(0)
print("end")