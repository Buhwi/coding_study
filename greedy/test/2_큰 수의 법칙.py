"""
def solution(n, m, k, array):
    answer = 0

    array.sort()
    a = array[n-1]
    b = array[n-2]
    
    while True:
        for i in range(k):
            if m == 0:
                break
            answer += a
            m -= 1
        if m == 0:
            break
        answer += b
        m -= 1

    return answer
"""

def solution(n, m, k, array):
    answer = 0
    array.sort()
    a = array[n-1]
    b = array[n-2]

    answer += a*(k*(m//k))
    answer += b*(m%k)


    return answer


def main():
    temp = [5, 8, 3]
    array = [2, 4, 5, 4, 6]
    print(solution(5, 8, 3, array))

main()