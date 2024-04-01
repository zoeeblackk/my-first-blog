# class Library:
#     def __init__(self, name, location, author, books):
#         self.name = name
#         self.location = location
#         self.author = author
#         self.books = books

#     def methods(self):
#         self.books.append()
#         self.books.remove()
#         self.books.input()

# list = ['romeo', 'juliet', 'wizard']

# def search():
#     userinput = input("Enter a book: ")
#     if userinput in list:
#         print(list[0])
#     else:
#         print('Book not found')

# search()

# def add()

# CONDITIONAL TASKS

# def AgeCheck():
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("You're not old enoug to vote :( Try again next year.)")
#     elif age >= 18:
#         print("You are old enough to vote! Don't be a trump supporter!")
#     else:
#         print("Error")

# AgeCheck()

# def MaxNumber():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     num3 = int(input("Enter last number: "))

#     if num1 > num2 and num1 > num3:
#         print(num1)
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#     elif num3 > num1 and num3 > num2:
#         print(num3)

# MaxNumber()

# def Palindrome():
#     string = input("Enter your string: ")
#     charlist = []

#     for i in string:
#         charlist.append(i)

#     listcopy = charlist.copy()
#     charlist.reverse()

#     if listcopy == charlist:
#         print("String is a palindrome!")
#     else:
#         print("String is NOT  a palindrome")

# Palindrome()

# def between():
#     start = int(input("Enter a starting value: "))
#     end = int(input("Enter an ending value: "))

#     numlist = list(range(start, end + 1))
#     print(numlist)

# between()

# def incs():
#     start = int(input("Enter starting value: "))
#     step = int(input("Enter increments: "))

#     nums = list(range(start, 100, step))
#     print(nums)

# incs()

# def string(x):
#     b = x[::-1]
#     return b

# print(string(input("Enter: ")))

# def string():
#     num = input("Enter: ")
#     rev = num[::-1]
#     print(rev)

# string()

# def numlist(nums):
#     sum = 0
#     count = 0
#     while count != len(nums):
#         for num in nums:
#             sum += num
#             count += 1
#     return sum
    
# x = [3, 6, 24, 56]
# print(numlist(x))

# def numberslist(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum

# x = [4, 6, 7]
# print(numberslist(x))

# def stringcon(strlist):
#     result = ''
#     for wrd in strlist:
#         result += wrd
#     return result

# x = ['string', 'word', 'sentence']
# print(stringcon(x))

# def intlist(numbers):
#     newlist = []
#     for i in numbers:
#         if i % 2 == 0:
#             newlist.append(i)
#         else:
#             pass
#     return newlist

# x = [4, 3, 5635, 76, 8, 9]
# print(intlist(x))

# def strlist(wrds):
#     result = []
#     for wrd in wrds:
#         if len(wrd) > 5:
#             result.append(wrd)
#     return result

# x = ['zozo', 'testies', 'strawberry', 'poke']
# print(strlist(x))

# def intsum(ints):
#     sum = 0
#     for i in ints:
#         sum += int(i)
#     return sum

# x = ['4', '43', '69', '100']
# print(intsum(x))

def diclist(people):
    agesum = 0
    count = 0
    currentdict = {}

    for person in people:
        currentdict = person
        agesum += currentdict['age']
        count += 1

    avg = agesum / count
    return avg

ppl_name_age = [
    {'name': 'Grace', 'age': 14},
    {'name': 'Claire', 'age': 37},
    {'name': 'Newborn', 'age': 0},
    {'name': 'Rebecca', 'age': 29}
]
print(diclist(ppl_name_age))