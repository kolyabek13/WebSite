from math import *
x=float(input("Введите число"))
y=float(input("Введите число"))
def f(a,b):
    return (a*a+3*a-b)/sqrt(a+b)
summ=0
p=1
for i in range(3,18):
    for j in range(3,15):
        p=p*(x*x+f(2,4))/(f(i,j)+i*j)
    summ=summ+p
print(summ)