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

    return common_len - (need_max - need_min + 1)  # works


def task2():
    class Team:
        def __init__(self, first_score, second_score, is_first_home, is_second_home):
            self.first_score = first_score
            self.second_score = second_score
            self.is_first_home = is_first_home
            self.is_second_home = is_second_home
            self.advantage = False

        def get_first_score(self):
            return self.first_score

        def get_second_score(self):
            return self.second_score

        def get_is_first_home(self):
            return self.is_first_home

        def get_is_second_home(self):
            return self.is_second_home

        def get_advantage(self):
            return self.advantage

        def set_second_score(self, number):
            self.second_score = number

        def set_advatage(self, advantage):
            self.advantage = advantage

    def check_for_advantage(team1, team2):
        if team1.get_is_first_home():  # second game in guests
            if team1.get_second_score() > team2.get_first_score():
                team1.set_advatage(True)
            if team1.get_second_score() < team2.get_first_score():
                team2.set_advatage(True)
        else:  # first game in guests
            if team1.get_first_score() > team2.get_second_score():
                team1.set_advatage(True)
            if team1.get_first_score() < team2.get_second_score():
                team2.set_advatage(True)

    str1 = input()
    str2 = input()
    if int(input()) == 1:
        fst_home = True
    else:
        fst_home = False

    team1 = Team(int(str1.split(':')[0]), int(str2.split(':')[0]), fst_home, not fst_home)
    team2 = Team(int(str1.split(':')[1]), int(str2.split(':')[1]), not fst_home, fst_home)

    common_score_first_team = team1.first_score + team1.second_score
    common_score_second_team = team2.first_score + team2.second_score
    difference = common_score_second_team - common_score_first_team

    team1.second_score = team1.second_score + difference

    check_for_advantage(team1, team2)

    if team1.get_advantage():
        return difference if difference >= 0 else 0
    else:
        return difference + 1 if difference >= 0 else 0


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


def task4():
    global rem_r, rem_b
    board = []
    rem_b_ex = False
    rem_r_ex = False
    for line in range(8):
        board.append([])
        string = input()
        for col in range(8):
            cur_symb = string[col]
            if cur_symb == 'R':
                board[line].append('R')
                rem_r = [line, col]
                rem_r_ex = True
            if cur_symb == 'B':
                board[line].append('B')
                rem_b = [line, col]
                rem_b_ex = True
            else:
                board[line].append('*')
    k = 0
    for line in range(8):
        for col in range(8):
            if rem_r_ex and line == rem_r[0]:
                board[line][col] = 'R'
            if rem_r_ex and col == rem_r[1]:
                board[line][col] = 'R'
            if rem_b_ex and abs(line - rem_b[0]) == abs(col - rem_b[1]):
                board[line][col] = 'B'
    for i in range(8):
        for j in range(8):
            print(board[i][j], end='')
        print()
    for i in range(8):
        for j in range(8):
            if board[i][j] == '*':
                k += 1
    return k

def task5():
    profit, numbers_quantity, days = input().split()
    profit, numbers_quantity, days = int(profit), int(numbers_quantity), int(days)
    new_profit = -1
    for i in range(10):
        if (profit * 10 + i) % numbers_quantity == 0:
            new_profit = profit * 10 + i
    if new_profit == -1:
        return -1
    else:
        return str(new_profit) + '0' * (days - 1)

def task9():
    num_from_day_of_week = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    day_of_week_by_num = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    celeb_num = int(input())
    year = int(input())
    holydays = []
    holydays_in_digit = []
    busy_week_days = [0]*7
    for i in range(celeb_num):
        holydays.append(input().split())
    start_day = input()

    if year % 4 == 0 and year != 1900:
        is_wis = True
        days_in_year = 366
    else:
        is_wis = False
        days_in_year = 365
    num_from_month = {
        "January": 31,
        "February": 29 if is_wis else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    for i in range(len(holydays)):
        days = 0
        for cur_num_by_month in num_from_month:
            if holydays[i][1] != cur_num_by_month:
                days += num_from_month[cur_num_by_month]
            else:
                days += int(holydays[i][0]) - 1
                break
        holydays_in_digit.append(days)

    for i in range(num_from_day_of_week[start_day], days_in_year + num_from_day_of_week[start_day]):
        real_i = i - num_from_day_of_week[start_day]
        busy_week_days[i % 7] += 1
        for j in range(len(holydays_in_digit)):
            if real_i == holydays_in_digit[j]:
                busy_week_days[i % 7] -= 1
    res1 = day_of_week_by_num[busy_week_days.index(max(busy_week_days))]
    res2 = day_of_week_by_num[busy_week_days.index(min(busy_week_days))]
    return res1 + " " + res2

print(task9())