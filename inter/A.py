"""

# 1. На вход приходит список типа
# ['banana', 'apple', 'grapefruit', 'apple', 'grapefruit', 'grapefruit']
# 2. Функция должна вывести массив уникальных значений, отсортированных
# по убыванию, то есть ['grapefruit', 'banana', 'apple']

"""

def sort_fruct(fructs: list):
    new_list = list(set(fructs))
    new_list.sort(reverse=True)
    return new_list

f = ['banana', 'apple', 'grapefruit', 'apple', 'grapefruit', 'grapefruit']
print(sort_fruct(f))
