# creating an empty list
my_list = []

# Appending values to the list
for i in (10,20,30,40):
    my_list.append(i)
print(my_list)

# Adding value 15 to the index 2
my_list.insert(1,15)
print(my_list)

# Extending the list with a new list
my_second_list = [50,60,70]
my_list.extend(my_second_list)
print(my_list)

# Deleting the last item of the list
my_list.pop()
print(my_list)

# Arranging the list in ascending order
my_list.sort()
print(my_list)

# printing the index of number 30
index = my_list.index(30)
print(index)
