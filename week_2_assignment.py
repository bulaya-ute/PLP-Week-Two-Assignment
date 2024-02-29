my_list = []
for number in (10, 20, 30, 40):
    my_list.append(number)
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
del my_list[-1]
my_list = sorted(my_list)
print("Index of 30 is:", my_list.index(30))
