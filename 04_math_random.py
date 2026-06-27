# #створення змінної і
# a = 5
# b = 6
# c = 7
# '''
# print(a, b , c)
# print("a =", a, " b =", b, " c =", c)
# print("Numbers : a = {}. b = {}. c = {}".format(a,b,c))
# print("Numbers : a = {}. b = {}. c = {}".format(c,b,a))
# print(f"Numbers : a = {a}. b = {b}. c = {c}")
# '''

# print(a)
# print(a)
# print(a)
# if a > b:
#     print("a > b")
# else:
#     print("a < b")

# print("HEllo world")
# print("HEllo world")
# print('HEllo world')

# str1 = "Happy"
# str2 = " New Year"
# print(str1+str2)

# # str1 = "Happy New Year"
# # str2 = 2026
# # print(str1+str2)
# x = 22
# y = 45
# print(x+y)
# # = - оператор присвоєння vs  == оператор порівняння
# x = 5
# y = 55
# z = 34
# a == b
# x == y

# import math

# print(math.ceil(2.5))# 2.5 ===> 3
# print(math.floor(2.5)) # 2.5 ===> 2
# print(math.pow(2,5))  # 2**5
# print(math.sqrt(16))  # 16 ==> 4   4*4 = 16

# import random

# print(random.random())  #0......1  float
# print(random.randint(0,10))  #0......10  
# print(random.randint(100,200))  #100......200  

# import math
# price_1 = 270
# price_2 = 220
# gramm = int(input("Enter weight of candies (gram): "))

# kg = gramm / 1000
# print(f"Your want to buy {kg} kg candies")

# if kg < 0.5:
#     total = kg*price_1
# else:
#     total = kg*price_2
# print(f"You have to pay : { math.ceil(total)} grn")


day = int(input("Enter number day [1-7]: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Error number day")





    

day = int(input("Enter number day [1-7]: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Error number day")
