def solution(n, m, array):
    temp = []
    for i in range(len(array)):
        temp.append(min(array[i]))
    return max(temp)

def main():

    print(solution(3, 3, [[3,1,2], [4,1,4], [2,2,2]]))
    print(solution(2, 4, [[7,3,1,8], [3,3,3,4]]))

main()