seasons = {'1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer', '7': 'summer', '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'autumn', '12': 'winter'}
while True:
    month = input('input month\'s number (1-12):\n')
    if (not month.isdigit()) | int(month)>12:
        continue
    print(seasons[month])
    break
