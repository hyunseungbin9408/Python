n = 15
check = 1
answer = 0
while check <= n:
    check_to_n = 0
    for i in range(check,n+1):
        check_to_n += i
        if check_to_n == n:
            answer += 1

    check += 1
print(answer)