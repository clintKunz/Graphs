import math

def solution(N, K):
    # write your code in Python 3.6
    if N < K: 
        return -1

    answer = math.factorial(N)/(math.factorial(K) * math.factorial(N-K))

    if answer > 1000000000:
        return -1 

    return int(answer)


print(solution(5,3))
# print(solution(testb))
# print(solution(testc))