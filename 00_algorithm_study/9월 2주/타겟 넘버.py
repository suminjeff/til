def solution(numbers, target):
    N = len(numbers)
    co = [1, -1]
    subset_list = []
    for i in range(1 << N):
        subset1 = []
        subset2 = []
        for j in range(N):
            if i & (1 << j):
                subset1.append(j)
            else:
                subset2.append(j)
        subset_list.append([subset1, subset2])
    cnt = 0
    for subsets in subset_list:
        res = 0
        for zero_or_one in range(2):
            if subsets[zero_or_one]:
                for k in subsets[zero_or_one]:
                    res += numbers[k] * co[zero_or_one]
            else:
                continue
        if res == target:
            cnt += 1
    return cnt


numbers1 = [1, 1, 1, 1, 1]
target1 = 3                 # return 5
print(solution(numbers1, target1))

numbers2 = [4, 1, 2, 1]
target2 = 4                 # return 2
print(solution(numbers2, target2))