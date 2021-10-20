def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            signs[i] = 1
        else:
            signs[i] = -1
        print(signs[i])
        sum += absolutes[i] * signs[i]

    return sum