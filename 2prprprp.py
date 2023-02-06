def Schet(Days):
    Full = int()
    for i in range(Days):
        if len(str(i)) == 2:
            Full = Full + int(str(i)[0]) + int(str(i)[1])
        else:
            Full += i
    return Full

Year = int(input("Введите год: "))
Sum = int()
if Year % 4 == 0:
    if Year % 100 == 0 and Year % 400 != 0:
        Sum += Schet(29)
    else:
        Sum += Schet(30)
    Sum += Schet(32)*7
    Sum += Schet(31)*4
print("Итог: ", Sum)