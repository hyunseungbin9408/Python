def solution(survey, choices):
    mbti_list = {'R':0,'T':0,
             'C':0, 'F':0,
             'M':0,'J':0,
             'A':0,'N':0}

    for i in range(len(survey)):
        if choices[i] >= 5:
            mbti_list[survey[i][1]] += choices[i] - 4
        elif choices[i] <= 3:
            mbti_list[survey[i][0]] += 4 - choices[i]
    result = ''
    if mbti_list['R'] < mbti_list['T']:
        result += 'T'
    elif mbti_list['R'] >= mbti_list['T']:
        result += 'R'
    if mbti_list['C'] < mbti_list['F']:
        result += 'F'
    elif mbti_list['C'] >= mbti_list['F']:
        result += 'C'
    if mbti_list['J'] < mbti_list['M']:
        result += 'M'
    elif mbti_list['J'] >= mbti_list['M']:
        result += 'J'
    if mbti_list['A'] < mbti_list['N']:
        result += 'N'
    elif mbti_list['A'] >= mbti_list['N']:
        result += 'A'

    return result