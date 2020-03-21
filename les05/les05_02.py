f = open("my_file.txt", 'r', encoding='UTF-8')
lines = 0
tmp = 0
for line in f:
    lines += 1

    words = 0
    flag = False
    for symbol in line:
        if symbol == '\n':
            tmp +=1
        elif symbol != ' ' and not flag:
            words += 1
            flag = True
        elif symbol == ' ':
            flag = False
    print(f'line {lines}: {words} words\n')

if lines == tmp: #если число строк равно числу переводов строк, есть еще одна строка, пустая
    print(f'line {lines+1}: 0 words\n')

print(lines)
print(tmp)
f.close()