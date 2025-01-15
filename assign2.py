#create an empty list
my_list=[] 
my_list=[10,20,30,40]
print(my_list)
my_list[2]=15
print(my_list)
my_list3=[50,60,70]
print(my_list3)
my_list.extend(my_list3)
print(my_list3)
print(my_list.extend(my_list3))
del my_list[-1]
print(my_list)
my_list.append(30)
print("After Append:", my_list)
print(my_list.index(30))