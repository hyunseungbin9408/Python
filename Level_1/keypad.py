numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
import collections

left_tump = [1, 4, 7]
right_tump = [3, 6, 9]
midle_number = [2, 5, 8, 0]

pad_dic = {1:[0,0],}

left_tump_check = collections.Counter(left_tump)
right_tump_check = collections.Counter(right_tump)
result = ""

tump_location_left = 0
tump_location_right = 0

for j,i in enumerate(numbers):
    if left_tump_check[i]:
        result += "L"
        tump_location_left = i
        print()
    elif right_tump_check[i]:
        result += "R"
        tump_location_right = i
        print(tump_location_right, 'R')
    elif i == 5:
        if hand == "right":
            tump_location_right = i
            print(tump_location_right, 'R')
            result += "R"
        else:
            result += "L"
            tump_location_left = i
            print(tump_location_left, 'L')
    else:
        if abs(tump_location_left - i) > abs(tump_location_right - i):
            result += "R"
            tump_location_right = i
            print(tump_location_right,'R')
        elif abs(tump_location_left - i) < abs(tump_location_right - i):

            result += "L"
            tump_location_left = i
            print(tump_location_left, 'L')
        elif abs(tump_location_left - i) == abs(tump_location_right - i):
            if hand == "right":
                tump_location_right = i
                print(tump_location_right, 'R')
                result += "R"
            else:
                result += "L"
                tump_location_left = i
                print(tump_location_left, 'L')
print(result)