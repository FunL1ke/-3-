def check_na_prostotu(chislo):
    count = 0
    flag = True
    for i in range(1, chislo + 1):
        if chislo % i == 0:
            count += 1
        if count > 2:
            flag = False
    return(flag)