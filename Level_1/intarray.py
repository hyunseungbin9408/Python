
numbers = []
numbers = [2,1,3,4,1]
numbers_list = []

for i,number in enumerate(numbers):
    j = i + 1
    if j+1 > len(numbers):
        pass
    else:
        while j < len(numbers):
            numbers_list.append(number + numbers[j])
            j = j + 1

test2 = sorted(list(set(numbers_list)))
print(test2)

## 정답
def solution(numbers):
    numbers_list = []
    for i,number in enumerate(numbers):
        j = i + 1
        if j+1 > len(numbers):
            pass
        else:
            while j < len(numbers):
                numbers_list.append(number + numbers[j])
                j = j + 1
    result = sorted(list(set(numbers_list)))
    return result