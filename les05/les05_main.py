import json
from os import path
import os
import shutil
import sys

#sys.exit(1)
#print(sys.executable)
print(sys.platform)


# print(path.dirname(__file__))
#
file_name = 'some_file.txt'
file_name2 = 'some_file2.txt'
#
# print(path.join(path.dirname(__file__), file_name))
file_path = path.join(path.dirname(__file__), file_name)
file_path2 = path.join(path.dirname(__file__), file_name2)

dir_path = path.join(path.dirname(__file__), 'some_dir')
#
# print(path.isdir(path.dirname(__file__)))
#
#
# some_list = [1, 2, 3, 4, 5]
# #
# j_str = json.dumps(some_list)
# # #print(type(j_str))
# #
# # file = open(file_path, 'w')
# # file.write(j_str)
# # file.close()
# #
# # j_data = file.read()
# # data = json.loads(j_data)
# # print(type(data))
# # file = open('test.txt', 'rb', encoding='UTF-8')
# #
# # print(file.read())
# # #file.write('222')
# #
# #
# # file.close()
#
# #file = open(file_path, 'w')
# with open(file_path, 'w') as file:
#     file.write(j_str)
#
# with open(file_path, 'r') as file:
#     data = json.loads(file.read())
# print(data)

#shutil.copy(file_path, file_path2)
#