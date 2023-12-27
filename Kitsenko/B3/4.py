A, B = int(input()), int(input())
summ = 0
summ_chet = 0
summ_nechet = 0

for i in range(A, B + 1):
    summ += i
    if i % 2 == 0:
        summ_chet += i
    else:
        summ_nechet += i
print(f"""Сумма чисел от {A} до {B} = {summ}
Сумма четных чисел от {A} до {B} = {summ_chet}
Сумма нечетных чисел от {A} до {B} = {summ_nechet}""")