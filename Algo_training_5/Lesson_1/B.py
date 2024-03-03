"""Футбольный комментатор"""

K1g1, K2g1 = list(map(int, input().split(':')))
K1g2, K2g2 = list(map(int, input().split(':')))
idn = int(input())


def win_g(k1_game_1, k2_game_1, k1_game_2, k2_game_2, where):
    sum_goals_k1 = k1_game_1 + k1_game_2
    sum_goals_k2 = k2_game_1 + k2_game_2

    if sum_goals_k1 > sum_goals_k2:
        return 0

    if where == 1:
        k1_home, k2_guest = k1_game_1, k2_game_1

        k1_guest, k2_home = k1_game_2, k2_game_2

    else:
        k1_guest = k1_game_1
        k2_home = k2_game_1

        k1_home = k2_game_2
        k2_guest = k2_game_2

    if sum_goals_k1 == sum_goals_k2:
        if k1_guest > k2_guest:
            return 0
        else:
            return 1

    n = sum_goals_k2 - sum_goals_k1

    if where == 1 and k1_guest + n > k2_guest:
        return n
    elif where == 2 and k1_guest > k2_guest:
        return n
    else:
        return n + 1


print(win_g(K1g1, K2g1, K1g2, K2g2, idn))
