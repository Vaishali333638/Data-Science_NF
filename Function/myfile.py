#Function in python
#1.Check whether two strings are Anagrams
def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
print(anagram("listen","silent"))

#2.Find Second largest number in a list
def second_largest(numbers):
    numbers.sort()
    return numbers[-2]
list1 = [10, 25, 37, 54, 70]
print("Second Largest Number:", second_largest(list1))

#3.Count Vowels in a Sentence

def count_vowels(sentence):
    vowels = "aeiou"
    for ch in vowels:
        print(ch,":", sentence.lower().count(ch))
text = "Python Programming"
count_vowels(text)

#4.Check whether a Number is an Armstrong Number
def armstrong(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp%10
        total = total + digit **3
        temp = temp //10
    if total == num:
        return True
    else:
        return False
print(armstrong(153))

#5.
Find Common Elements between multiple lists
def common_elements(list1, list2, list3):
    common = []
    for i in list1:
        if i in list2 and i in list3:
            common.append(i)
    return common
a = [1,2,3,4]
b = [2,3,5,6]
c = [2,3,7,8]
print("Common Elements:", common_elements(a, b, c))
