def solution(number):
    count = 0
    for n in range(1, number):
        if (n % 3 == 0 or n % 5 == 0):
            count += n

    return count

print(solution(10))