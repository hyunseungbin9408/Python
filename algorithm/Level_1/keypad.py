def solution(numbers, hand):
    import collections

    left_tump = [1, 4, 7]
    right_tump = [3, 6, 9]
    midle_number = [2, 5, 8, 0]

    pad_dic = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1],'*':[3,0],'#':[3,2]}
    tump_location_right = pad_dic['#']
    tump_location_left = pad_dic['*']

    left_tump_check = collections.Counter(left_tump)
    right_tump_check = collections.Counter(right_tump)
    result = ""
    for j,i in enumerate(numbers):
        check_tump = pad_dic[i]
        if left_tump_check[i]:
            result += "L"
            tump_location_left = pad_dic[i]
        elif right_tump_check[i]:
            result += "R"
            tump_location_right = pad_dic[i]
        else:
            if abs(check_tump[0] - tump_location_left[0]) + abs(check_tump[1] - tump_location_left[1]) > \
                    abs(check_tump[0] - tump_location_right[0]) + abs(check_tump[1] - tump_location_right[1]):
                result += "R"
                tump_location_right = pad_dic[i]
            elif abs(check_tump[0] - tump_location_left[0]) + abs(check_tump[1] - tump_location_left[1]) < \
                    abs(check_tump[0] - tump_location_right[0]) + abs(check_tump[1] - tump_location_right[1]):
                result += "L"
                tump_location_left = pad_dic[i]
            elif abs(check_tump[0] - tump_location_left[0]) + abs(check_tump[1] - tump_location_left[1]) == \
                    abs(check_tump[0] - tump_location_right[0]) + abs(check_tump[1] - tump_location_right[1]):
                if hand == "right":
                    tump_location_right = pad_dic[i]
                    result += "R"
                elif hand == "left":
                    tump_location_left = pad_dic[i]
                    result += "L"
    return result