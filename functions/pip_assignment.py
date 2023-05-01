# Write a Python function that takes two arguments (a and b) and returns their sum.
def sum(a,b):
   answer = a+b
   return answer
a=12
b=8
print(sum(a,b))

# Write a Python function that takes a list of integers as input and returns 
# the sum of all the integers in the list.
def list_of_intergers(nums):
    sum = 0
    for num in nums:
        sum+=num
        return sum
    
    print(list_of_intergers(1,2,3,4,5))

# Write a Python function that takes a list of integers as input and 
# returns a new list with all the even numbers removed.
def remove_even(num1):
    for i in num1:
        if i%2==0:
            num1.remove(i)
        print(remove_even(2,4,5,8,9,7,15))

# Write a Python function that takes a list of integers as input and 
# returns the highest value in the list.
def max_num(value):
   num = 0
   for m in value:
      if m > num:
         num = m
   return num
     
print(max_num(18,15,14,25,60))

# Write a Python function that takes a list of strings as input and returns a
# new list with all the strings capitalized.
def capitalize_string(name1):
  name = name1.upperCase()
  return name
print(capitalize_string("Hello Trizah"))

   