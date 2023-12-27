import math

def plata(km):
    metr = km * 1000
    metraj = metr / 140
    money = 240 + (metraj * 15)
    return(round(money))

print(plata(float(input())))