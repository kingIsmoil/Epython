# ### Task 1
# A combine threshed A tons of grain, and the second harvested B tons less. How many tons of grain did both combiners thresh?

# ----

# Один комбайн намолотил A тонн зерна, а второй на B тонн меньше. Сколько тонн зерна намолотили оба комбайна?

# ----

# Як комбайн A тонна ғалла даравид, ва дуюмаш B тонна камтар. Ҳар ду комбайн чӣ қадар ғалла даравиданд?

# n1=int(input())
# n2=int(input())
# print(n1+n1-n2)

# ### Task 2
# There were A passengers on the bus. B passengers got off at the bus stop and C entered. How many passengers were on the bus?

# ----

# В автобусе было A пассажиров. На остановке вышло B пассажиров и вошло C. Сколько пассажиров стало в автобусе?

# ----

# Дар автобус A мусофир буд. Дар истгоҳ B мусофир фаромад ва C мусофир даромад. Дар автобус чанд мусофир шуд?

# n1=int(input())
# n2=int(input())
# n3=int(input())
# print(n1-n2+n3)

# ### Task 3
# Given a four-digit number. Find the maximum digit in this number.

# ----

# Дано четырехзначное число. Найдите максимальную цифру в этом числе.

# ----

# Адади чорхонагӣ дода шудааст. Рақами калонтаринро дар ин адад ёбед.

# n=int(input())
# a=int(n//1000)
# b=int(n//100%10)
# c=int(n//10%10)
# d=int(n%10)
# if a>b and a>c and a>d :
#     print(a)
# if b>a and b>c and b>d:
#     print(b)
# if c>a and c>b and c>d:
#     print(c)
# if d>a and d>b and d>c :
#     print(d)


# ### Task 4
# Four integers are given. Find the number of positive, negative and zeros in the original set.

# ----

# Даны четыре целых числа. Найдите количество положительных, отрицательных чисел и количество нулей в исходном наборе.

# ----

# Чор адади бутун дода шудааст. Шумораи ададҳои мусбӣ, манфӣ ва сифрҳоро дар маҷмӯи ибтидоӣ ёбед.

# n1=int(input())
# n2=int(input())
# n3=int(input())
# n4=int(input())
# cnt=0
# znt=0
# ont=0
# if n1>0:
#     cnt+=1
# if n1<0:
#     znt+=1
# if n1==0:
#     ont+=1
# if n2>0:
#     cnt+=1
# if n2<0:
#     znt+=1
# if n2==0:
#     ont+=1
# if n3>0:
#     cnt+=1
# if n3<0:
#     znt+=1
# if n3==0:
#     ont+=1
# if n4>0:
#     cnt+=1
# if n4<0:
#     znt+=1
# if n4==0:
#     ont+=1
# print("Positive",cnt)
# print("Negative",znt)
# print("Zero",ont)


# ### Task 5
# Write a program to display the next and previous even number of the given number.

# ----

# Напишите программу для отображения следующего и предыдущего четного числа для заданного числа.

# ----

# Барномае нависед, ки адади ҷуфти навбатӣ ва пешинаро барои адади додашуда нишон диҳад.

# n=int(input())
# print("The next number for the number",n,"is",n-n%2+2)
# print("The previous number for the number",n,"is",n+n%2-2)


# ### Task 6
# Given a five-digit number. Find the sum and product of its digits.

# ----

# Дано пятизначное число. Найдите сумму и произведение его цифр.

# ----

# Адади панҷхонагӣ дода шудааст. Сумма ва ҳосили зарби рақамҳои онро ёбед.

# n=int(input())
# a=int(n//10000)
# b=int(n//1000%10)
# c=int(n//100%10)
# d=int(n//10%10)
# e=int(n%10)
# print("The sum of the digits is:",a,"+",b,"+",c,"+",d,"+",e,"=",a+b+c+d+e)
# print("The product of the digits is:",a,"*",b,"*",c,"*",d,"*",e,"=",a*b*c*d*e)


# ### Task 7
# Write a program to display n terms of natural numbers and their sum.

# ----

# Напишите программу для отображения n членов натурального ряда чисел и их суммы.

# ----

# Барномае нависед, ки n ҷумлаи ададҳои натуралӣ ва суммаи онҳоро нишон диҳад.

# n=int(input())
# i=1
# sum=0
# print("The natural numbers up to",n,"th terms are:",end=" ")
# while i<=n:
#     sum=sum+i
#     print(i,end=" ")
#     i=i+1
# print()
# print("The sum of the natural numbers is:",sum)


# ### Task 9
# Write a program to find the factorial of a number.

# ----

# Напишите программу для нахождения факториала числа.

# ----

# Барномае нависед, ки факториали ададро ёбад.

# n=int(input())
# i=1
# f=1
# while n>=i:
#     f=f*n
#     n=n-1
# print("The factorial of the given number is:",f)


# ### Task 8
# Given a real number — the price of 1 kg of sweets. Output cost of 1, 2, ..., 10 kg of sweets.

# ----

# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.

# ----

# Адади ҳақиқӣ — нархи 1 кг қанд дода шудааст. Арзиши 1, 2, ..., 10 кг қандро нишон диҳед.

# n=float(input())
# i=1
# while i<=10:
#     print(i,"kg -",i*n)
#     i=i+1


# ### Task 10
# Write a program to display the pattern like right angle triangle with numbers.

# ----

# Напишите программу для отображения узора в виде прямоугольного треугольника с числами.

# ----

# Барномае нависед, ки нақшро дар шакли секунҷаи росткунҷа бо рақамҳо нишон диҳад.

# n=int(input())
# i=1
# while i<=n:
#     i=i+1
#     j=1
#     while j<=i-1:
#         print(j,end="")
#         j=j+1
#     print()
  
   