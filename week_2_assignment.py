my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
del my_list[-1]
my_list = sorted(my_list)
print("Index of 30 is:", my_list.index(30))
