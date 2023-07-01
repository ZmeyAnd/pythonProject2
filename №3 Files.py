import os
from pprint import pprint
import os
current = os.getcwd()
folder_name = 'HW'

full_path = os.path.join(current, folder_name)


my_files = os.listdir(full_path)

common_txt_file_list = []

for file_name in my_files:
  with open(f'{full_path}\{file_name}', 'r', encoding="utf8") as f:
     file_lines = f.readlines()

     common_txt_file_list.append([str(len(file_lines)), file_name, file_lines])
common_txt_file_list.sort()
with open('result.txt', 'w') as new_file:
    for i in common_txt_file_list:
        print(i[1])
        print(i[0])
        print(''.join(i[2]))
        new_file.write(i[1] + '\n')
        new_file.write(i[0] + '\n')
        new_file.write(''.join(i[2]))

# pprint(common_txt_file_list)
