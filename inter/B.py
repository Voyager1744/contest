def count_fructs(fructs):
    fr_dict = dict()
    for fruct in fructs:
        if fruct in fr_dict:
            fr_dict[fruct] += 1
        else:
            fr_dict[fruct] = 1

    new_dict = dict(sorted(fr_dict.items(), key=lambda x: x[1], reverse=True))

    return [frut for frut in new_dict.keys()]

f = ['banana', 'apple', 'grapefruit', 'apple', 'grapefruit', 'grapefruit']

print(count_fructs(f))