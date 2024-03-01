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



print(task1())