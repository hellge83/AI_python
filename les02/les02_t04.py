str = input('input string\n')
str = str.split(' ')
for i in range(0, len(str)):
    print(f'{i+1} : {str[i][:10]} \n')