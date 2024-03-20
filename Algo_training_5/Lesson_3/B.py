"""B. Анаграмма?"""
def is_anagram(a, b):
    if len(a) != len(b):
        return "NO"
    dict_a = {}
    dict_b = {}
    for i in a:
        if i in dict_a:
            dict_a[i] += 1
        else:
            dict_a[i] = 1
    for i in b:
        if i in dict_b:
            dict_b[i] += 1
        else:
            dict_b[i] = 1
    if dict_a == dict_b:
        return "YES"
    else:
        return "NO"


a = input()
b = input()
print(is_anagram(a, b))
