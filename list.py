list = ["my_list"]
my_list = [10,20,30,40]
print(my_list)
# inserting the value 15 at the second position
my_list.insert(1, 15)
print(my_list)
# extending the list with another list
my_list.extend([50, 60, 70])
print(my_list)
# Removing the last element from the list
my_list.remove(70)
print(my_list)
# sorting my list in ascending order
my_list.sort()
print(my_list)
# Printing the index of the value 30
print(my_list.index(30))