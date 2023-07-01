

import os
current = os.getcwd()
folder_name = 'venv'
file_name = 'recipes.txt'
full_path = os.path.join(current, folder_name, file_name)

from pprint import pprint


with open(full_path, 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        food_name = line.strip()
        ingredient_count = int(f.readline().strip())
        food_name_list = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = f.readline().strip().split('|')
            food_name_list.append({
                'ingredient_name': ingredient_name,
                'quantity' : int(quantity),
                'measure' : measure
            })
        f.readline()
        cook_book[food_name] = food_name_list
# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for item in cook_book[dish]:
            if item['ingredient_name'] not in res:
                res[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity'] * person_count}
            else:
                res[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
    pprint(res)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)

