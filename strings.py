# 1. Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string
n = "Terry"
m = "Chozi"
print(n, m)

new_string1 = m[:2] + n[2:]
new_string2 = n[:2] + m[2:]

swap_string = new_string1 + " " + new_string2
print(swap_string)

# 2.  Write a Python function that takes a list of words and 
# returns the longest word and the length of the longest one
def longest_word(words):
    longest = ""
    length_of_longest_word = 0
    for x in words:
        if len(x) > length_of_longest_word:
         longest = words
         length_of_longest_word = len(x)
    return longest, length_of_longest_word
my_list = ["Jayden", "Fiona", "Edgar", "May", "Gabriel Kimeu"]
result = longest_word(my_list)
print(result[0], result[1])

# Write a Python function that takes two lists and returns 
# True if they have at least one common member.
def two_lists(list1, list2):
   answer = False
   answer = True
   for x in list1:
      for y in list2:
         if x ==y:
          return True
   return False
list1 = ["apple","berry","kiwi"]
list2 = ["berry", "Dates", "orange"]
if two_lists:
   print("Have common members")
else:
   print("have no common members")

# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
my_list = ["Pink", "Joyce", "Tesla"], ["color", "Name", "Make"]

keys = ["Pink", "Joyce", "Tesla"]
values = ["color", "Name", "Make"]
list_of_dictionaries = [{keys[i]: values[i]} for i in range(len(keys))]
print(list_of_dictionaries)

# 6. Write a Python program to check whether all dictionaries in a list are empty or not

empty_dictionaries = [{},{},{}]
if empty_dictionaries == []:
   print("The dictionary is empty")
else:
   print("The dictionary is not empty")

# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:

numbers = [3,5,45,97,32,22,10,19,39,43]
even_numbers = [num for num in numbers if num % 2 ==0]
print(even_numbers)

# 8. Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
common_numbers = [a for a in list_b]
print(common_numbers)

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)
def divisible_by_single_digits(numbers):
    for m in range(1, 100):
     for i in range(2,10):
       if m% i == 0:
          i=numbers.add(m)
print(numbers)
result = [number for number in range(1,1000) if True in [True for x in range(2,10) if number % x == 0]]
print(result)

# Write a Python function to remove all vowels in a string
def removeVowels(string):
    vowel = 'aeiou'
    string="Patricia"
    for ch in string.lower():
        if ch in vowel:
            string = string.replace(ch, '')
    print(removeVowels(string))

























 
   

