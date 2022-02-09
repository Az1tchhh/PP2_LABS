def check_good(a):
    good_pos = len(a) - 1
    for i in range(len(a) - 2, -1, -1):
        if i + a[i] >= good_pos:
            good_pos = i
    return good_pos == 0


print(check_good(list(map(int, input().split()))) + 0)