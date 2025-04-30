"""1. Write a program to find the length of the string without using inbuilt function (len)**"""

# s="hello world"
# count=0
# for i in s:
#     count+=1
# print(count)


"""2. Write a program to reverse a string without using any inbuilt functions.**"""

# s="hello welcome to python"
# res=""
# for i in s:
#     res=i+res
# print(res)


"""3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".**"""
# s="hello world"
# s_=s.replace('world','universe')
# print(s_)

"""4. How to convert a string to a list and vice-versa.**"""
# s="hello"
# s_=s.split()
# s1="".join(s_)
# print(s_)
# print(s1)


"""5. Covert the string "Hello welcome to Python" to a comma separated string.**"""
# s="Hello welcome to Python"
# s1=",".join(s)
# print(s1)

"""6. Write a program to print alternate characters in a string.**"""
# s="Hello welcome to Python"
# s1=s[::2]
# print(s1)

"""7. Write a Program to print ascii values of the characters present in a string.**"""
# s="hello world"
# for i in s:
#     print(i,ord(i))
"""8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.**"""
# s="HeLLo WorlD"
# s1=""
# for i in s:
#     if 'a'<=i<='z':
#         s1=s1+(chr(ord(i)-32))
#     elif 'A'<=i<='Z':
#         s1=s1+(chr(ord(i)+32))
#     else:
#         s1=s1+i
# print(s1)



"""9. Write program to swap two numbers without using 3rd variable.**"""
# a=10
# b=20
# a,b=b,a
# print(a,b)

"""10. Write program to merge two different lists.**"""
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c)
#
# l=[*a,*b]
# print(l)



"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)**"""

"""12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)**"""

"""13 Program to print last "N" lines of a file.**"""

"""14. Write a program to check if the given string is Palindrome or not without using reversed method."""

# s='madam'
# if s==s[::-1]:
#     print("it is a palendrome")
# s='helo'
# s1=""
# for i in s:
#     s1=i+s1
# if s1==s:
#     print('it is a palendrome')
# else:
#     print('it is not a palendrome')


"""15 Write a program to search for a character in a given string and return the corresponding index.**"""
s='hello world'
# p='w'
# for index,char in enumerate(s):
#     if p==char:
#         print(char,index)



"""16 Write a program to get the below output**"""
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# d={}
# for item in sentence.split():
#     if item[0] not in d:
#         d[item[0]]=[item]
#     else:
#         d[item[0]]+=[item]
# print(d)


"""17 Write a to replace all the characters with - if the character occurs more than once in a string**"""
# s="hello world welcome to python"
# res=""
# for char in s:
#     if s.count(char)>1:
#         res=res+"-"
#     else:
#         res=res+char
# print(res)

"""18 write a decorator that returns only positive values of subtraction**"""

# def positive(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return abs(res)
#     return wrapper
# @positive
#
# def sub(a,b):
#     return a-b
#
# print(sub(1,2))


"""19 How to get the count of number of instances of a class that is being created.**"""

"""20 Write a function which takes a list of strings and integers.If the item is a string it 
should print as is and if the item is integer of float it should reverse it.**"""

# s=['hello',123,'howr',4673,'456']
#
# for item in s:
#     if isinstance(item, (int, float)):
#         print(str(item)[::-1])
#     else:
#         print(item)




"""21 Write a class named Simple and it should have iteration capability.**"""

"""22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**"""

"""23 Write a python program to get the below output**"""

# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
# sen=sentence.split()
# l=[]
# for i in sen:
#     l.append(i[::-1])
# print(" ".join(l))




"""25 Write a lambda function to add two numbers (a, b)**"""

# s=lambda a,b:a+b
# print(s)

#
"""26 What is the output of the following**"""
# sentence = "Hi How are you"
# 	# o/p should be "ouy era woH iH"
# res=""
# for i in sentence:
#     res=i+res
# print(res)


"""27 How to remove duplicates from the list without using inbuilt functions**"""
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# res=[]
#
# for item in items:
# 	if item not in res:
# 		res.append(item)
#
# print(res)


#
"""28 Find the longest word in the sentence**"""
# sentence = "Hello world. Welcome to Python"
# sen=sentence.split()
# res=""
# for i in sen:
#     if len(i)>len(res):
#         res=i
#     else:
#         res=res
# print(res)

"""29 write a program to reverse the values in the dictionary if the value is of type String**"""
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for i,j in d.items():
#     if  isinstance(j,str):
#         d[i]=d[i][::-1]
#     else:
#         d[i]=j
# print(d)



"""30 write a program to get 1234**"""
# t = ('1', '2', '3', '4')
# res=""
# for i in t:
#     res=res+i
# print(res)




"""31 How to get the elements that are in list b but not in list a**"""
a = [1, 2, 3]
b = [1, 2, 3, 4]

print(set(b)-set(a))



"""32 A function takes variable number of positional arguments as input.
How to check if the arguments that are passed are more than 5"""

# def func(*args):
#     if len(args)>5:
#         print("the number of arguments is more than 5")
#     else:
#         print("the number of arguments is less than 5")
# func(1,2,3,4)
# func(3,4,5,6,6,7)


# """33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file."""
# # Assume Below is the contents of the log file

# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
#
"""34 Write a function to reverse any iterable without using reverse function.**"""
# a = [1, 2, 3, 4, 5]
# def reverse(ver):
#    return ver[::-1]
#
# print(reverse(a))




"""35 Write a function to print the below output"""
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
# def func(string,n):
#     if n==0:
#         print(string[1::2])
#     elif n==1:
#         print(string[0::2])
# func("TRACXN",0)
"""36 Sum all the numbers in the below string."""
# s = "Sony12India567Pvt2ltd"
# res=""
# for i in s:
#     if i.isdigit():
#         res+=i
#     else:
#         res+=""
# s=" ".join(res)
# s1=s.split()
# sum = 0
# for j in s1:
#     sum =int(j)+sum
# print(sum)
"""37 Write a program to sum all the numbers in below string."""
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
# res=""
# for i in s:
#     if i.isdigit():
#         res+=i
#     else:
#         res+=" "
# print(res)
# s=res.split()
# sum = 0
# for j in s:
#     sum =int(j)+sum
# print(sum)
"""38 Print all the numbers in the below list"""
# a = ['abc', '123', 'hello', '23']
# for i in a:
#     if i.isdigit():
#         print(i)


"""39 Program to print the number of occurrences of characters in a String without using inbuilt functions."""
s = 'helloworld'
# d={}
# for char in s:
#     if char not in d:
#         d[char]=1
#     else:
#         d[char]+=1
# print(d)




"""40 Program to print only the repeated characters and count of the same.**"""
s = 'helloworld'
# d={}
# for char in s:
#     if char not in d:
#         d[char]=1
#     else:
#         d[char]+=1
# s={}
# for i,j in d.items():
#     if j>1:
#         s[i]=j
#
# print(s)


# for char in s:
# 	if s.count(char) > 1:
# 		print(char, s.count(char))



"""41 Write a program to get alternate characters of a string in list format."""
# s = 'hello world welcome to python'
# s_=[]
# s_.extend(s[::2])
#
#
# print(s_)

"""###alternative answer"""
# s = 'hello world welcome to python'
# s1=s[::2]
# print(list(s1))


"""42 Write a program to get square of list of number's using lambda function ."""
# a = [1, 2, 3, 4, 5]
# s=lambda iterable:[i**2 for i in a]
# print(s(a))


"""43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other."""

"""44 Write a program to iterate through list and build a new list, only if the items
of the list has even number of characters."""
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# even_length=[]
# for item in names:
#     if len(item)%2==0:
#         even_length.append(item)
# print(even_length)

"""45 Write a program to iterate through list and build a new dictionary,
only if the items of the list has even number of characters."""
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# even_length={}
# for item in names:
#     if len(item)%2==0:
#         even_length[item]=len(item)
# print(even_length)



"""46 Write a program which squares the numbers in a list using map object"""
# a = [1, 2, 3, 4, 5]
# square=lambda num:num**2
# print(list(map(square,a)))

"""47 Count number of lines in a file without loading the file to the memory"""
# with open("sample.txt") as file:
#     count=0
#     for i in file:
#         count+=1
#     print(count)

"""48 Printing line and line no's"""
# with open("sample.txt") as file:
#     for lineno,line in enumerate(file,start=1):
#         print(lineno,line)

"""49 Write a Program to print the sum of entire list and sum of only internal list"""
l = [[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in l:
#     for j in i:
#         sum=sum+j
#
# print(sum)
# for i in l:
#     sum=0
#     for j in i:
#         sum=sum+j
# print(sum)
# total_sum = 0
#
# for list_ in l:     # [1, 2, 3]
# 	internal_sum = 0
# 	for num in list_:   # 1, 2, 3
# 		total_sum += num
# 		internal_sum += num
# 	print(f"internal_sum is {internal_sum}")
# print(total_sum)
"""50 Write a program to reverse the list as below"""
words = ["hi", "hello", "python"]
# o/p ['nohtyp', 'olleh', 'ih']
# word=words[::-1]
# s=[]
# for i in word:
#     s.append(i[::-1])
# print(s)


# """51 Write a program to update the tuple"""
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # # o/p (1, 2, 3, 4, 100, 200, 300)
# print((t1+t2))

"""52 Write a program to replace value present in nested dictionary.# # Replace "nose" with "net"""""
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# d['b']['n']='net'
# print(d)
"""53 Write a program to count the number of white spaces in a file."""
# with open("sample.txt", "r") as file:
#     count=0
#     for line in file:
#         if " " in line:
#             count=count+line.count(" ")
#     print(count)



"""54 Grouping anagrams."""
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']

# print(word)
d={}
for i in words:
    w=sorted(i)
    w1="".join(w)
    if w1 not in d:
        d[w1]=[i]
    else:
        d[w1]+=[i]
print(d)

#

"""55 What is the difference between defaultdict and normal dictionary."""
# Defaultdict
# -----------
# 1. When each key is encountered for the first time, it will not be there in the mapping.
# 2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
# 3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
# 4. So, in defaultdict, creation of key, initialisation will happen simultaneously.
#
# Normal Dictionary
# ------------------
# 1. In case of normal dictionary, if the key does not exist, "KeyError" is raised.
# 2. In order to work on the value, first the key needs to be created and initialised.
# """
# """
# **56 Explain property decorator in python.**
# ```python
# #
# """
# """57 What is Mutable and Immutable datatypes.**
# ```python
#
# 1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
# 2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
# """
# """
# **58 Explain get() method in dictionaries.**
# ```python
#
# point =  {'a': 1, 'b': 2}
# 1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
# 2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
# 3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
# 4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
#            e.g. profile.get('c', 'Sorry the key does not exist')
# """
#
"""59 Write a list comprehension to get a list of even numbers from 1-50**"""
# numbers=[i for i in range(1,51) if i%2==0]
# print(numbers)
# l=[]
# for i in range(1,51):
#     if i%2==0:
#         l.append(i)
# print(l)


"""60 Find the longest non-repeated substring in the below string"""
s = "This is a Programming language and Programming is fun"
# s1=s.split()
#
# res=""
# for i in s1:
#     if len(res)< len(i):
#         res=i
# print(res)
#
# lenght=sorted(s1,key=len)
# print(lenght)
# d={}
# res=""
# for i in s1:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for i,j in d.items():
#     if j == 1:
#         if len(i) > len(res):
#             res=i
# print(res)

"""61 Write a program to find the duplicate elements in the list without using inbuilt functions**"""
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# d={}
# for i in names:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
#     if d[i]>1:
#         print(i)
"""62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions"""
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
# d={}
# for i in names:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)



"""63 Write a function to check if the number is Prime**"""
# def prime_num(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("it is not a prime number")
#             break;
#     else:
#         print("it is a prime number")
#
# prime_num(19)
"""64 How to create a tuple using range function"""
# tuple=()
# for i in range(1,5):
#     tuple+=(i,)
# print(tuple)

"""65 Write a program to find the largest number in the list without using any inbuilt functions**"""
# numbers = [10, 20, 30, 40, 50]
# res=0
# for i in numbers:
#     if i>res:
#         res=i
# print(res)
# **66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.**
#
"""67 Write a program to find most common words in a given list."""
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under']
# d= {}
# for i in words:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# # item=d.items()
# # count=lambda item:item[1]
# sort_func=sorted(d.items(),key=lambda item:item[-1])
# print(sort_func[-1])



"""68 Make a function named tail that takes a sequence (like a list, string, or tuple) and
 a number n and returns the last n elements from the given sequence, as a list."""
# sequence=[2,4,5,6,7,1,2,4,5,6]
# def tail(sequence,n):
#      return sequence[n::1]
#
# tail((2,4,2,4,5,6,6,7,7,8),3)


"""
69 Write function named is_perfect_square that accepts a number and
 returns True if it's a perfect square and False if it's not."""
# def is_perfect_square(n):
#     square=int(n**0.5)
#     if square**2==n:
#         return True
#     else:
#         return False
# print(is_perfect_square(4))

"""70 Write a program to get all the duplicate items and the number of times the item is repeated in the list."""
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d={}
# for i in names:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# **71 Write a program to count the number of occurrences of each word in a file.**
#
# **72 Write a program to count the number of occurrences of vowels in a file.**
#
# **73 Write a program to print all numeric values in a list**
# items = ['apple', 1.2, 'google', '12.6', 26, '100']"""


# s="aaaaaabbbbcccaa"
# #o/p="6a4b3c2a"
# res=""
# previous_char=s[0]
# count=1
# for char in s[1:]:
#     if char==previous_char:
#         count+=1
#     else:
#         res+=str(count)+previous_char
#         count=1
#         previous_char=char
# res+=str(count)+previous_char
# print(res)
"""prime number"""
# def is_prime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# l=[]
#
# for j in range(1,101):
#     if is_prime(j):
#         l.append(j)
# print(l)

"""febanacco series"""
# def fibonacco_series(n):
#     fib1=0
#     fib2=1
#     print(fib1,fib2,end=" ")
#     for _ in range(3,n+1):
#         fib3=fib1+fib2
#         print(fib3,end=" ")
#         fib1=fib2
#         fib2=fib3
# fibonacco_series(10)



# l=["python","interview","score","exam"]
# res=lambda a:a[::-1]
# print(list(map(res,l)))
# from collections import defaultdict
# s="price system is post screen"
# s1=s.split()
# for i in s1:
#     d=defaultdict(list)
#     d[i[0]]+=i
# print(d)


import ipaddress

def validate(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False
print(validate("212.10.94.231"))










