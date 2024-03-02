def task1():
    list1 = input().split()
    list2 = input().split()
    vas_start = int(list1[0])
    vas_steps = int(list1[1])
    mas_start = int(list2[0])
    mas_steps = int(list2[1])

    vas_left = vas_start - vas_steps
    vas_right = vas_start + vas_steps

    mas_left = mas_start - mas_steps
    mas_right = mas_start + mas_steps

    max_right = max(mas_right, vas_right)
    min_left = min(mas_left, vas_left)

    vas_len = vas_right - vas_left + 1
    mas_len = mas_right - mas_left + 1
    common_len = vas_len + mas_len

    if mas_left > vas_right or vas_left > mas_right:
        return common_len
    it = min_left
    count = 0

    need_min = max(mas_left, vas_left)
    need_max = min(mas_right, vas_right)

    return common_len - (need_max - need_min + 1)

def task2():
    str1 = input()
    str2 = input()
    is_first_home = True if input() == "1" else False
    fst_match = list(map(int, str1.split(":")))
    snd_match = list(map(int, str2.split(":")))
    need_goals = fst_match[1] + snd_match[1] - fst_match[0] - snd_match[0]
    if is_first_home:
        if snd_match[1] < snd_match[0] + need_goals:
            return (need_goals)
        else:
            return (need_goals + 1)
    else:
        if fst_match[0] > fst_match[1]:
            advantage = True
        else:
            advantage = False
        if advantage:
            return need_goals
        else:
            return (need_goals + 1)


def task3():
    def calc_quantity(number):
        k = 0
        if number == 0:
            return 0
        dic = {0: 1,
               1: 1,
               2: 2,
               3: 2
               }
        if number > 4:
            l = number // 4
            k += l
            number -= 4 * l
        if number != 0:
            k += dic[number % 4]
        return k

    n = int(input())
    res = 0
    for i in range(n):
        res += calc_quantity(int(input()))
    return res


def task7():
    my_sold = int(input())
    tower_hp = int(input())
    sold_per_round = int(input())

    cur_enemy_sold = 0
    rounds = 0
    if my_sold == sold_per_round and tower_hp == my_sold + 1:
        return -1
    if my_sold < sold_per_round:
        while True:
            rounds += 1
            cur_enemy_sold -= my_sold - min(my_sold, tower_hp)
            tower_hp -= min(my_sold, tower_hp)

            my_sold -= cur_enemy_sold

            if tower_hp != 0:
                cur_enemy_sold += sold_per_round
            if tower_hp == 0 and cur_enemy_sold <= 0:
                return rounds
            if my_sold <= 0:
                return -1
    if my_sold >= sold_per_round:
        while True:

            rounds += 1
            tower_hp -= my_sold - min(cur_enemy_sold, my_sold)
            cur_enemy_sold -= min(cur_enemy_sold, my_sold)

            my_sold -= cur_enemy_sold
            if tower_hp <= 0 and cur_enemy_sold == 0:
                return rounds
            if tower_hp != 0:
                cur_enemy_sold += sold_per_round
            if my_sold <= 0:
                return -1



print(task7())