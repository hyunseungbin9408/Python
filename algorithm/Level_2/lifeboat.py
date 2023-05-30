people = [70, 50, 80, 50, 50]
limit = 100
# from collections import deque
#
# people.sort(reverse=True)
# deque_people = deque(people)
# i = 0
# j = 1
# count = 0
# while len(deque_people) >= 2:
#     if deque_people[0] + deque_people[-1] <= limit:
#         count += 1
#         deque_people.popleft()
#         deque_people.pop()
#     else:
#         if len(deque_people) - 1 == j:
#             deque_people.popleft()
#             j = 1
#         else:
#             j += 1
# print(count)
def solution(people, limit):
    from collections import deque
    people.sort(reverse=True)
    deque_people = deque(people[:])
    i = 0
    j = 1
    count = 0
    while len(deque_people) >= 2:
        if deque_people[0] + deque_people[-1] <= limit:
            count += 1
            deque_people.popleft()
            deque_people.pop()
        elif deque_people[0] + 40 > limit:
            deque_people.popleft()
        else:
            if len(deque_people) - 1 == j:
                deque_people.popleft()
                j = 1
            else:
                j += 1
    return(len(people) - count)
print(solution(people,limit))