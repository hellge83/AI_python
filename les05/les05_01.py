f = open("new_file.txt", 'x')
line = True
while line:
   line = input('input line:\n')
   f.write(line + '\n')

f.close()


