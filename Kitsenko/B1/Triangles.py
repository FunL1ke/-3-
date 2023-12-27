from math import sqrt, sin, radians

print ('''Площадь треугольника
Cпособы вычисления площади треугольника:
1 - формула Герона
2 - через основание и высоту
3 - через две стороны и угол между ними''')

print ("Выберите желаемый способ вычисления площади треугольника:")
f = int(input())

if f == 1:
    print('Введите сторону a')
    a = float(input())
    print('Введите сторону b')
    b =  float(input())
    print('Введите сторону c')
    c =  float(input())
    p = (a + b + c) / 2
    s = sqrt(p*(p - a)*(p - b)*(p - c))
elif f == 2:
    print('Введите основание a')
    a = float(input())
    print('Введите высоту h')
    h = float(input())
    s = (a*h)/2
else:
    print('Введите сторону a')
    a = float(input())
    print('Введите сторону b')
    b =  float(input())
    print('Введите угол ab')
    ab =  float(input())
    u = sin(radians(ab))
    s = abs(1/2 * a * b * round(u, 3))
print(s)