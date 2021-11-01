def solution(a, b):
    answer_list = [i * j for i, j in zip(a, b)]
    return sum(answer_list)


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
