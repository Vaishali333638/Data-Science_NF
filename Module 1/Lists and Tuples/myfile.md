#Find the largest and smallest element in a list
"""numbers = [10, 20, 30, 40, 50]
largest = max(numbers)
smallest = min(numbers)
print("Largest element is:", largest)
print("Smallest element is:", smallest)"""

#Remove duplicate elements from a list
numbers= [1, 2, 2, 3, 3, 5]
new_list= list(set(numbers))
print(new_list)

#Reverse a list without using reverse() method
numbers =[1,2,3,4,5]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

#Count even and odd numbers in a list
numbers = [1,2,3,4,5,6]
even = 0
odd = 0
for num in numbers:
    if num%2 == 0:
        even +=1
    else:
        odd +=1
print("Even numbers:", even)
print("Odd numbers:", odd)

#Merge two lists and sort the final list 
list1 = [1,5,3]
list2 = [4,2,6]
merged_list = list1 + list2
merged_list.sort()
print("Sorted merged list:", merged_list)

#Find the second largest element in a list
numbers = [10,20,30,40,50]
numbers.sort()
print("Second largest number:", numbers[-2])

#Check whether an element exists in a tuple
data = (10,20,30,40,50)
element = 20
if element in data:
    print("Element exists")
else:
    print("Element does not exist")

#Count occurrence of an element in a tuple
data = (1,2,3,2,4,2)
element = 2
count = data.count(element)
print("Occurrence of 2:", count)

#Sort a list of tuples based on tuple values
data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
data.sort()
print("Sorted list of tuples:", data)

#Convert tuple into list and list into tuple
my_tuple = (1,2,3)
my_list = list(my_tuple)
print("Tuple to list:", my_list)

number = [4,5,6]
new_tuple = tuple(number)
print("List to tuple:", new_tuple)
