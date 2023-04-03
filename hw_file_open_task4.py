content_dict = {}
with open('1.txt', 'r', encoding="utf-8") as file1, open('2.txt', 'r', encoding="utf-8") as file2, open('3.txt', 'r', encoding="utf-8") as file3:
    content_dict['1.txt'] = file1.readlines()
    content_dict['2.txt'] = file2.readlines()
    content_dict['3.txt'] = file3.readlines()

for k, v in dict(sorted(content_dict.items(), reverse=True, key=lambda item: item[1])).items():
    with open('result_file.txt', 'a', encoding="ANSI") as file:
        file.write(k + '\n')
        file.write(str(len(v))+ '\n')
        file.writelines(v)
        file.writelines('\n')
print('Результат в файле result_file.txt')