a , b , c = 1  ,2, 3 
print(a)
print(b)
print(c)
a = b = c = 3#<---------------------
print(a)
print(b)
print(c)

login = 'olena'
print(login)

#оператори + - / *
# унарні(1) оператори  +5    -5
# бінарні(2) оператори +  (3+5)  - * / // ** %
# бінарні(2) оператори < > <= >=   ==(дорівнює)   !=(не дорівнює)  True False
# тернарні оператори

a = 5 #(=) - оператор присвоєння
b = a
# ==  - оператор порівняння

print("1 == 1", 1 == 1) #True
print("3 == 1", 3 == 1) #Fasle
print("3 != 1", 3 != 1) #True
print("5 != 5", 5 != 5) #False

print("5 > 5", 5 > 5) #False
print("5 > 2", 5 > 2) #True
print("1 > 2", 1 > 2) #False

print("5 < 5", 5 < 5) #False
print("5 < 2", 5 < 2) #False
print("1 < 2", 1 < 2) #True

print("5 >= 5", 5 >= 5) #True  5 > 5 or 5 == 5
print("5 >= 2", 5 >= 2) #True
print("1 >= 2", 1 >= 2) #False

print("5 <= 5", 5 <= 5) #True  5 < 5 or 5 == 5
print("5 <= 2", 5 <= 2) #False
print("1 <= 2", 1 <= 2) #True


print(bool(0))# False
print(bool(0.0))# False
print(bool(''))# False
print(bool(None))# False



print(bool(1))# True
print(bool(0.01))# True
print(bool(100))# True
print(bool(55))# True
print(bool("a"))# True
print(bool("adsdg"))# True

#логічні оператори поєднання умов and (логічне І ), or (логічне або) ,
#  not (логічна інверсія) not True = False   not False = False

competent = True
responsible = True
print(competent and responsible) #True

competent = True
responsible = False
print(competent and responsible) #False

competent = False
responsible = True
print(competent and responsible) #False

competent = False
responsible = False
print(competent and responsible) #False


#or
competent = True
responsible = True
print(competent or responsible) #True

competent = True
responsible = False
print(competent or responsible) #True

competent = False
responsible = True
print(competent or responsible) #True

competent = False
responsible = False
print(competent or responsible) #False

#not 
competent = True
print(not competent)

competent = False
print(not competent)

# Ctrl + K + C - comment
# Ctrl + K + U - uncomment
# Ctrl + / - comment/uncomment

# age = int(input("Enter age : "))
# if age >= 18 and age <= 65:# 18 > 18..False    age > 18 --> 19 === age > 18 or age == 18
#     print("Adult")
# else:
#     print("Error age ")

# day = int(input("Enter number day [1-7] : "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")    
# elif day == 3:
#     print("Wendesday")
# else:
#     print("Error number day ")
a = 8
a%2 == 0
a%2 != 0
a%2 == 1
print("Menu . 1 - add number . 2 - minus. 3 - multy. 4 - divide")
num = 1

login = input("Enter login : ")
if login == 'admin':
    password = input("Enter password : ")
    if password == "itstep":
        print("Welcome to the system")
    else:
        print("Password is invalid!")  

elif login == 'exit':
    print("Have a nice day!!!")
else:
    print("Error input")

