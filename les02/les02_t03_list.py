seasons2 = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
while True:
    month = input('input month\'s number (1-12):\n')
    if (not month.isdigit()) | int(month)>12:
        continue
    print(seasons2[int(month)-1])
    break