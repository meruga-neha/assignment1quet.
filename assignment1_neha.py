value_num= 0
x, y = 0, 1
num_mult = 9
for i in range(0, num_mult):
    x = y
    y = value_num
    value_num = x + y
    print(value_num)
if value_num <= 1:
    print("nothing")



