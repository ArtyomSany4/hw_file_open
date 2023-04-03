from pprint import pprint

# def reading_recipes():
with open('recipes.txt', 'r', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        number_of_ingrnts = int(file.readline().strip())
        ignridients = []
        for _ in range(number_of_ingrnts):
            ignridient, quantity, measure = file.readline().strip().split(' | ')
            ignridients.append({
                'Название ингредиента': ignridient,
                'Количество': quantity,
                'Единица измерения': measure
            })
        file.readline()
        cook_book[dish_name] = ignridients
    # return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            el_list = []
            val_dict = {}
            for el in ingr.values():
                el_list.append(el)
            # print(el_list)
            if el_list[0] in shop_list_by_dishes.keys():
                val_dict['quantity'] = (int(el_list[1]) * person_count + int(shop_list_by_dishes[el_list[0]]['quantity']))
            else:
                val_dict['quantity'] = int(el_list[1]) * person_count
            val_dict['measure'] = el_list[2]
            shop_list_by_dishes[el_list[0]] = val_dict
    return shop_list_by_dishes
        
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2), sort_dicts=False) 


###############
# Задача №3. Про объединение трех файлов в один
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
print('Результат в файле result_file.txt в папке проекта.')