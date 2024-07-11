d= int(input("Введите первое число: "))
s= int(input("Введите второе число: "))
a=int(input("Введите третье число: "))
if a==s==d:
    print(3)
elif a==s or s==d or d==a:
    print(2)
else:
    print(0)
