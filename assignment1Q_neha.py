variable_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var_odd = 0
var_even = 0
for i in variable_num:
    if i % 2 == 0:
        var_even += 1
    else:
        var_odd += 1
print("number of given even numbers in the list:", var_even)
print("number of given odd numbers in the list:", var_odd)            