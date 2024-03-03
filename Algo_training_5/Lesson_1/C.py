"""Форматирование файла"""


def cnt_tap(lines, tab=4):
    count_res = 0
    for num in lines:
        count_tab, ost = divmod(num, tab)
        if ost == 0:
            count_res += count_tab
        elif ost in [1, 2]:
            count_res += count_tab + ost
        else:
            count_res += count_tab + 2
    return count_res


if __name__ == "__main__":
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(cnt_tap(nums))
