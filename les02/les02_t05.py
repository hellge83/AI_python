start_list = [7, 5, 3, 3, 2]
while True:
    num = input('input number:\n')
    if not month.isdigit():
        continue
    start_list.append(int(num))
    start_list.sort(reverse=True)
    print(start_list)
    break