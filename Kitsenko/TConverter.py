def temperature_checking(temperature):
    while True:
        try:
            temp = float(temperature.replace(',', '.'))
            return temp
        except ValueError:
            print('Неверное значение температуры (число).')
            temperature = input()

def scale_checking(scale):
    while True:
        try:
            temp = int(scale)
            if temp in (1, 2, 3):
                return(temp)
            else:
                print('Ошибка.')
                scale - input()
        except ValueError:
            print('Ошибка.')
            scale = input()
print('''Конвертер температур.
      Шкалы температур:
      1. Цельсий
      2. Фаренгейт
      3. Кельвин
      Выберите шкалу вводимой температуры,
      а затем выберите шкалу, в которую будут
      конвертированы значения температуры.
      В конце введите значение температуры''')

print('Выберите шкалу вводимой температуры:')
scale1 = input()
scale1 = scale_checking(scale1)

print('Выберите шкалу выводимой температуры:')
scale2 = input()
scale2 = scale_checking(scale2)

print('Введите темпуратуру:')
temperature = input()
temperature = temperature_checking(temperature)

tm = []
if scale1 == 1:
    tm.append(temperature)
    tm.append(temperature + 273.15)
    tm.append((temperature * 1.8) + 32)
elif scale1 == 2:
    tm.append((temperature - 32) / 1.8)
    tm.append((temperature + 459.67) / 1.8)
    tm.append(temperature)
else:
    tm.append(temperature - 273.15)
    tm.append(temperature)
    tm.append(temperature * 1.8 - 459.67)
tm_scale = ["'Цельсий'", "'Кельвин'", "'Фаренгейт'"]
print(f"Перевод температуры из шкалы {tm_scale[scale1 - 1]} в шкалу {tm_scale[scale2 - 1]}:")
print(tm[scale2 - 1])