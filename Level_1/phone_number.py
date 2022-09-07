def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number) - 4):
        answer += "*"
    result = phone_number.replace(phone_number[0:len(phone_number) - 4], answer)
    return result