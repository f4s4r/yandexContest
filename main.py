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


def task4():
    def show(board):
        for i in range(8):
            cur_line = ''
            for j in range(8):
                cur_line += board[i][j]
            print(cur_line)
    board = []
    for line in range(8):
        board.append([])
        string = input()
        for col in range(8):
            cur_symb = string[col]
            if cur_symb == 'R':
                board[line].append('R')
            elif cur_symb == 'B':
                board[line].append('B')
            else:
                board[line].append('*')

    for line in range(8):
        for col in range(8):
            if board[line][col] == "R":
                for in_right in range(col + 1, 8):
                    if board[line][in_right] != "B" and board[line][in_right] != "R":
                        board[line][in_right] = "r"
                    elif board[line][in_right] == "R":
                        pass
                    else:
                        break

                for in_left in range(col - 1, -1, -1):
                    if board[line][in_left] != "B" and board[line][in_left] != "R":
                        board[line][in_left] = "r"
                    elif board[line][in_left] == "R":
                        pass
                    else:
                        break

                for in_up in range(line-1, -1, -1):
                    if board[in_up][col] != "B" and board[in_up][col] != "R":
                        board[in_up][col] = "r"
                    elif board[in_up][col] == "R":
                        pass
                    else:
                        break
                for in_down in range(line + 1, 8):
                    if board[in_down][col] != "B" and board[in_down][col] != "R":
                        board[in_down][col] = "r"
                    elif board[in_down][col] == "R":
                        pass
                    else:
                        break
    #show(board)
    for line in range(8):
        for col in range(8):
            if board[line][col] == "B":
                # right down
                right = col + 1
                down = line + 1
                stop = False
                while right < 8 and down < 8 and not(stop):
                    if board[down][right] != "R" and board[down][right] != "B":
                        board[down][right] = "b"
                    elif board[down][right] == "B":
                        pass
                    else:
                        stop = True
                    right += 1
                    down += 1
                # right up
                right = col + 1
                up = line - 1
                stop = False
                while right != 8 and up != -1 and not(stop):
                    if board[up][right] != "R" and board[up][right] != "B":
                        board[up][right] = "b"
                    elif board[up][right] == "B":
                        pass
                    else:
                        stop = True
                    right += 1
                    up -= 1
                # left up
                left = col - 1
                up = line - 1
                stop = False
                while left != -1 and up != -1 and not(stop):
                    if board[up][left] != "R" and board[up][left] != "B":
                        board[up][left] = "b"
                    elif board[up][left] == "B":
                        pass
                    else:
                        stop = True
                    left -= 1
                    up -= 1
                # left down
                left = col - 1
                down = line + 1
                stop = False
                while left != -1 and down != 8 and not(stop):
                    if board[down][left] != "R" and board[down][left] != "B":
                        board[down][left] = "b"
                    elif board[down][left] == "B":
                        pass
                    else:
                        stop = True
                    left -= 1
                    down += 1
    #show(board)
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "*":
                count += 1
    return count

def task6():
    n = int(input())
    res = ""
    list_num = list(map(int, input().split(" ")))
    summ = list_num[0] % 2
    for i in range(1, n):
        cur_num = list_num[i]
        if (cur_num % 2 == 0 and summ == 1) or (cur_num % 2 == 1 and summ == 0):
            summ = 1
            res += "+"
        elif cur_num % 2 == 0 and summ == 0:
            res += "+"
        elif cur_num % 2 == 1 and summ == 1:
            res += "x"
    return res
    

def task8():
    def search_dis(L, pos):
        return pos if (pos <= L / 2) else (pos - L / 2)

    def dist_after_time(time, L, x1, v1, x2, v2):
        res1 = (x1 + v1 * time) % L
        res2 = (x2 + v2 * time) % L
        return res1, res2

    L, x1, v1, x2, v2 = list(map(int, input().split(" ")))

    dist_ratio = v1 / v2

    start_dist1 = search_dis(L, x1)
    start_dist2 = search_dis(L, x2)

    dist_difference = abs(start_dist1 - start_dist2)

    needed_dist1 = v1 * (dist_difference / (v1 + v2))
    # needed_dist2 = v2 * (dist_difference / (v1 + v2))

    return needed_dist1 / v1


print(task8())