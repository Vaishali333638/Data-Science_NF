#Write a program to create a dictionary from two lists: one of keys and one of values.
keys = ['name', 'age', 'city']
values = ['rohan', 25, 'delhi']
my_dict = dict(zip(keys, values))
print(my_dict)

#Merge two dictionaries into one.
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

#Write a program to sort a dictionary by its values.
my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)

#Given two sets, check if one set is a subset of another.
set1 = {1,2,3}
set2 = {1,2,3,4,5}
if set1.issubset(set2):
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")

#Write a program to check whether two lists have at least one common element using sets.
list1 = [1,2,3]
list2 = [4,5,3]
set1 = set(list1)
set2 = set(list2)
if set1.intersection(set2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common element.")
