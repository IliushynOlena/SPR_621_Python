
i = 1 # створення лічильника
while i < 11: # використання лічильника в умові
    print(i , "Hello")
    i = i + 1 # - зміна лічильника

#5......20
i = 5
while i < 21:
    print(i, end=" ")
    i += 1 #i = i + 1

print()
#   10 ...... 0
i = 10
while i > 0:
    print(i, end=" ")
    i -= 1


# i = int(input("Enter number : "))
# while i < 21:
#     print(i, end=" ")
#     i += 1 #i = i + 1

i = int(input("Enter number : "))

if i <= 20:
    while i < 21:
        print(i, end=" ")
        i += 1 #i = i + 1
else:#30 ....20
    while i >= 20:
        print(i, end=" ")
        i -= 1 #i = i + 1

number = int(input("Enter number : "))

if number < 0 or number > 10:
    print("Error number" )
else:
    i = 1
    while i <= 10:
        print(f"{i} * {number} = {i*number}")
        i += 1
    else:
        print("="*20)
