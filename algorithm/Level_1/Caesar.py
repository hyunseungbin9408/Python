def solution(s, n):
    result = ""
    from string import ascii_lowercase
    from string import ascii_uppercase
    low_alphabet_list = list(ascii_lowercase)
    up_alphabet_list = list(ascii_uppercase)

    up_z = up_alphabet_list.index('Z')
    low_z = low_alphabet_list.index('z')

    for i in s:
        if i == " ":
            result += i
        if i in up_alphabet_list:
            if up_alphabet_list.index(i) + n > up_z:
                result += up_alphabet_list[up_alphabet_list.index(i) + n - up_z - 1]
            else:
                result += up_alphabet_list[up_alphabet_list.index(i) + n]
        if i in low_alphabet_list:
            if low_alphabet_list.index(i) + n > low_z:
                result += low_alphabet_list[low_alphabet_list.index(i) + n - low_z - 1]
            else:
                result += low_alphabet_list[low_alphabet_list.index(i) + n]
    return result