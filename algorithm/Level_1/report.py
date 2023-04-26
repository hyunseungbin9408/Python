def solution(id_list, report, k):
    report_id = {}
    report_list = {}
    report_check = set(report)
    result_list = []
    answer = []

    for i in id_list:
        report_list[i] = 0
        report_id[i] = ""
    for i in report_check:
        report_list[i.split(" ")[1]] += 1
        report_id[i.split(" ")[0]] += i.split(" ")[1] + ','
    for i in report_list.items():
        if i[1] >= k:
            result_list.append(i[0])
    for i in report_id.items():
        answer_num = 0
        for j in i[1].split(','):
            if j in result_list:
                answer_num += 1
        answer.append(answer_num)
    return answer