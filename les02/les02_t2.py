list = []
while True:
    length = input('input length of list:\n')
    if not length.isdigit():
        continue
    while len(list) < int(length):
        list.append(input('Add a new element:\n'))
    print('Your list:', list)
    for i in range(0, int(length)-1, 2):
        list[i], list[i+1] = list[i+1], list[i]
    print ('New list:', list)
    break