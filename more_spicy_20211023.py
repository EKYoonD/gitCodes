import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7


# heapq 안쓰면 효율성 검사 통과 못함
def solution_no_heap(scoville, K):
    count_scoville = 0
    while True:
        for scov in scoville:
            if scov < K:
                break
            else:
                return count_scoville
        scov1 = scoville.pop(scoville.index(min(scoville)))
        scov2 = scoville.pop(scoville.index(min(scoville)))
        new_scov = scov1 + (scov2 * 2)
        scoville.append(new_scov)
        count_scoville += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return count_scoville


# heapq 사용
def solution_heap(scoville, k):
    heapq.heapify(scoville)
    i = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            i += 1
        else:
            return -1
    return i


print(solution_no_heap(scoville, K))