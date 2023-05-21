#%% My First Programming Line :)
# dict1 = {
#     "student1": {"name": "javad",
#                  "age": 23},
#     "student2": {"name": "maryam",
#                  "age": 33
#                  },
#     "student3": {"name": "amir",
#                  "age": 44,
#                  }
# }
# # print(dict1)
# # print(dict1)
# # print(dict1["student1"])
# # print(dict1)
# print(dict1["student1"]["age"])








# if dict1["student1"]["age"] > dict1["student2"]["age"]:
#     if dict1["student1"]["age"] > dict1["student3"]["age"]:
#         print(dict1["student1"]["name"])
# if dict1["student2"]["age"] > dict1["student1"]["age"]:
#     if dict1["student2"]["age"] > dict1["student3"]["age"]:
#         print(dict1["student2"]["name"])
# if dict1["student3"]["age"] > dict1["student1"]["age"]:
#     if dict1["student3"]["age"] > dict1["student2"]["age"]:
#         print(dict1["student3"]["name"])


#%% The other way

# dict1 = {
# "student1" : {input("name: "), input("age: ")},
# "student2" : {input("name: "), input("age: ")},
# "student3" : {input("name: "), input("age: ")}
# }

# dict1 = {
# input("javad: "),
# input("maryam: "),
# input("amir: ")
# }
# print(dict1)
# dict1 = list(dict1)
# print(dict1)
# if dict1[2] > dict1[1]:
#     if dict1[2] > dict1[0]:
#         print("javad")
# if dict1[1] > dict1[0]:
#     if dict1[1] > dict1[2]:
#         print("maryam")
# if dict1[0] > dict1[2]:
#     if dict1[0] > dict1[1]:
#         print("amir")



# myDict2 = {}
# name = input("name: ")
# age = int(input("age: "))
# myDict2[name] = age


# name = input("name: ")
# age = int(input("age: "))
# myDict2[name] = age


# name = input("name: ")
# age = int(input("age: "))
# myDict2[name] = age

# dictItems = list(myDict2.items())
# print(dictItems)

# if dictItems[0][1]>dictItems[1][1]:
#     if dictItems[0][1]>dictItems[2][1]:
#         print(dictItems[0][0])
#     else: 
#         print(dictItems[2][0])
# else:
#     if dictItems[1][1]>dictItems[2][1]:
#         print(dictItems[1][0])
#     else: 
#         print(dictItems[2][0])






#%% Loops
# While

# myList = [12,13,14,1,54,23,45]
# counter = 0
# while counter<len(myList):
    # print(myList[counter])
    # counter+=2

# myDict1 = {}
# i=0
# while i<3:
#     name = input("name: ")
#     age = int(input("age: "))
#     i+=1
#     myDict1[name] = age
# dictItems2 = list(myDict1.items()) 
# print(dictItems2)

# mylist = []
# i = 0
# while True:
#     name = input("Enter your name (Enter E01 to exit): ")
#     if name == "E01":
#         break
#     mylist.append(name)
# print(mylist)

# myDict2 = {}
# num = int(input("How many inputs do you need: "))
# i = 0
# while i<num:
#     name = input("Enter name (Write EE to exit): ")
#     if "EE" in name:
#         break
#     age = int(input("Enter age: "))
#     Confirmation = input(f"name: {name} age: {age} Do you confirm the information?(y/n)")
#     if "n" in Confirmation:
#         continue
#     myDict2[name] = age
#     i+=1
# else: 
#     print("All data have been successfully added")
# print(myDict2)


# Practice
# Total = int()
# i=0
# while True:
    # num1 = int(input("Enter your number: "))
    # num2 = int(input("Enter your number: "))
    # Total = sum([Total,num1,num2])
    # Equal = input("Do you want to continue? (+/=): ")
    # if "=" in Equal:
        # break
# print(Total)

# Total = [Total,num1,num2] #I know it doesn't work! I tried though!
# i=0
# while i<len(Total):
    # print("Hamid Ghalandari")
    # i+=1
#%% Loops (for)

# for x in range(0,10,2):
    # print(x)

# n = int(input("Enter number: "))
# counter = 1
# for n in range(1,n+1):
#     counter = counter*n
#     print(counter)

# n = int(input("Enter the number: "))
# import math
# print(math.factorial(n))

# n = int(input("Enter number: "))
# num = 1
# for i in range(1,n+1):
#     num*=i
#     print(num)

# n = int(input())
# text1 = input()
# text2 = input()
# j = 0
# for i in range(len(text1)):
#     if text1[i] != text2[i]:
#         j+=1
# print(j)

#%% functions and methods

# def my_function(*names):
#     print(names)
# my_function("ali", "hossein")

# def my_lib(**A):
#     print(A)
# my_lib(name = "zahra", surname = "Jones", age = 23)

# def myfunc(name = "Hamid", surname = "Ghalandari"):
#     print(name,surname)

# myfunc("atefe","mavadaati")
# myfunc()
# myfunc("ahmad","zamani")

# def func1(a,b):
#     c = a*b
#     return c,b-a
# multip = func1(5,24)
# print(multip)

# PI = 3.14

# def C(r):
#     C = 2*PI*r
#     return C
# def A(r):
#     A = PI*r*r
#     return A
# Circum = C(5)
# print(Circum)
# Area = A(5)
# print(Area)


# global mylist

# def biggest_num(*numbers):
#     biggest_num = numbers[0]
#     for number in numbers:
#         if number > biggest_num:
#             biggest_num = number
#     return biggest_num

# maxim = biggest_num(1,2,3,4,5,32,43,12,46,75,86)
# print(maxim)


# def my_function(info):
#     for input in info:
#         str(input)
#     return info

# num = 23,12
# Data = my_function(f"Hi my name is Hamid {num} we")
# print(Data)

# def fact(number):
#     counter = 1
#     for number in range(1,number+1):
#         counter*=number
#     return counter

# ex = fact(30)
# print(ex)


#%% Strings


# car_name = "volvo"
# car_color = "black"
# text = "my favorite car is {0} colored {1}"
# print(text.format(car_name,car_color))

#%% RegEx

# import re
# txt = "My name is hamid"
# n = re.search("^M.*",txt)
# print(n)

# text1 = "This is a test"
# text2 = """Email1 : arjbld@kjd.cod
# Email2 : sdfsdf@dk.slc
# Email3 : popou@sa,js
# Email4 : ljklsd@gmail.com
# """
# text3 = "The rain in Spain"
# xan = re.findall(r"\b[a-z]+[@].+[.].+",text2)
# print(xan)

# List1 = re.split(",", text3)
# print(List1)

# List2 = re.sub(r"\b[a-z]+[@].+[.].+","Correct Email", text2)
# print(List2)

#%% Practice
# Square root

# import math
# n = int(input())
# i = math.sqrt(n)
# print("%.4f" % i)

# Stone Pile
# https://acm.timus.ru/problem.aspx?space=1&num=1005
# n = 5
# w = [5,8,13,27,14]
# for i in range(0,len(w)-1):
#     if w[i] > w[i+1]:
#         n1 = w[i] - w[i+1]
#     else:
#         n1 = w[i+1] - w[i]
#     if w[i+1] > w[i+2]:
#         n2 = w[i+1] - w[i+2]
#     else:
#         n2 = w[i+2] - w[i+1]
#     if n1 < n2:
#         print(n1)
#     else:
#         print(n2)

#%% JSON Javascript Object Notation

# import json
# mJson = '{ "name": "hamid", "age": 23}'
# mValue = json.loads(mJson)
# print(mValue)


# x = {
#     "firstName": "Rack",
#     "lastName": "Jackon",
#     "gender": "man",
#     "age": 24,
#     "address": {
#         "streetAddress": "126",
#         "city": "San Jone",
#         "state": "CA",
#         "postalCode": "394221"
#     },
#     "phoneNumbers": [
#         { "type": "home", "number": "7383627627" }
#     ]
# }

# print(json.dumps(x, indent=3, sort_keys=True)) 


#%% 

# myFile = open("..//a//MyFile.json", "w")


# u = json.loads(myFile.read())
# print(myFile.read())

# print(u["age"])

# myFile = open("MyFile.txt", "a")
# myFile.write("\nMy name is Hamid!")
# print(myFile)


# myFile = open("MyFile.json")
# v = json.loads(myFile.read())
# myFile.close()
# print(v)

# v["age"]=34
# print(v)
# myFile = open("MyFile.json", "w")
# value = json.dumps(v, indent=3)
# myFile.write(value)
# myFile.close()
# print(value)


#%% Classes

# class Person:
#     name = ""
#     surname = ""
#     age = None
    
# p1 = Person()
# p1.name = "hamid"
# p1.surname = "ghalandari"
# p1.age = 34

# p2 = Person()
# p2.name = "amir"
# p2.surname = "sohra"
# p1.age = 25

# print(p2.age)

# class Person:
#     def __init__(self, name, surname, age, weight, height):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.wt = weight
#         self.ht = height
        
        
#     def __str__(self) -> str:
#         return f"{self.name} {self.surname} {self.age}"
        
    
#     def BMI(self):
#         return self.wt / self.ht**2
       
        
# p1 = Person("amir", "abadi", 24, 73, 1.74)
# print(p1)

# class Student(Person):
#     def __init__(self, name, surname, age, weight, height, sID):
#         super().__init__(name, surname, age, weight, height)
#         self.sID = sID
        
#     def __str__(self) -> str:
#           return f"{self.name} {self.surname} {self.age} {self.wt} {self.ht} {self.sID}"
        
# st1 = Student("ali", "ghafar", 34, 98, 2.10, 87001298)
# print(st1)
# print(st1.BMI())

# class MyNumber:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#     def __iter__(self):
#         self.a = self.x
#         return self
#     def __next__(self):
#         if self.a < self.y:
#             n = self.a
#             self.a +=1
#             return n
#         else:
#             raise StopIteration
# for i in MyNumber(0,20):
#     print(i)
    





        
    























    













    


 

