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

# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            el_list = []
            val_dict = {}
            for el in ingr.values():
                el_list.append(el)
            # print(el_list)
            val_dict['measure'] = el_list[2]
            val_dict['quantity'] = int(el_list[1]) * person_count
            shop_list_by_dishes[el_list[0]] = val_dict
            pprint(shop_list_by_dishes, sort_dicts=False)
            # print()
    # pprint(shop_list_by_dishes, sort_dicts=False)
    return shop_list_by_dishes
            # val = ingr.values()

        
        # if dish in cook_book.keys():
        #     shop_list_by_dishes[cook_book[dish]] = cook_book.get(dish)
        #     print(shop_list_by_dishes)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) 
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

