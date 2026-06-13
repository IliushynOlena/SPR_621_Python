#Літерали Python

print("Hello")
print('Hello')
print("123")
print(173+1)
print(124*2)

#Data types :
# number   --->   int (100), float (3.14)
#str (string)   --> "hello"
#boolean   --> True False

#Shift + Alt + arrow down   - dublicate row
#Shift + Alt + arrow up  - дублікат рядка
print("int",type(100))
print("int",type(-5))
print("float",type(3.14))
print("float",type(2.55))
print("str",type("100"))
print("str",type("Hello"))
print("bool",type(True))
print("bool",type(False))

#Python як калькулятор
#Основні оператори   + -  / *  //  %  **
print(5 + 7)
print(5 + 7.0)
print(5.0 + 7)
print(5.0 + 7.0)

#select symbol + Ctrl+D
print(5 - 7)
print(5 - 7.0)
print(5.0 - 7)
print(5.0 - 7.0)

print(5 * 7)
print(5 * 7.0)
print(5.0 * 7)
print(5.0 * 7.0)

print(15 / 3)
print(5 / 7.0)
print(5.0 / 7)
print(5.0 / 7.0)

# // - ділення числа націло - відкидає всі числа після коми  12345
print(15 // 3)
print(17// 3)
print(18//5)
print(21//3)

# **  - підносить до ступеня  2*2*2 = 8
print(2**3) #2*2*2 = 8
print(2**3.) #2*2*2 = 8
print(2.**3) #2*2*2 = 8
print(2.**3.) #2*2*2 = 8

# % - Оператори: остача (ділення за модулем, з остачею)
#15/3 = 5.0
print(15/3)

#15//3 = 5
print(15//3)

#15%3 = 5  ---> 15/3=5.0 --> 5*3=15  --> 15 - 15 = 0
print(15%3) #0
#16%3 = ???     16/5 = 3.2 ---> 3*5 = 15 --> 16 - 15 = 1
print(16/5)

print(8%2) # 0   8/2 = 4.0  4*2 = 8   8-8 = 0
print(8/2) #4.0
print(9%2) #1        9/2 = 4.5   4*2 = 8   9-8 = 1
print(21%3)# = 0
print(25%7)# 4

print(2 + 3 * 5)
print((2 + 3 )* 5)

#print(5/0)
#print(5/0.0)
#print(5%0)

print(5 + 2.6)     #7.6
#print(5 + 'hello') #error
print("hello" + 'hello') #error
print(5 + True)    #6  --> True = 1
print(5 + False)   #5  --> False = 0

print(1_000_000)

#Змінна - іменована ділянка пам*яті, яка має певну назву та зберігає певне значення
age = 15
print(age)
print("Age = ",age)
Age = 45
ageofman = 55
print("Age of man : ", ageofman)
ageOfMan = 47
age_of_man = 68

a1 = 5
a2 = 10
#3a = 7 error
#def = 3.33 error
num = 10
num = "Hello world"
pasword = "qwerty123"

#first_number = 10
#second_number = 22

first_number = int(input("Enter first number : "))
second_number = int( input("Enter second number : "))
summa = first_number + second_number
print("Summa = ", summa)
print(first_number, " + ",second_number, " = ", summa)

