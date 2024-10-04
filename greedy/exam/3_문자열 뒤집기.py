def solution(temp):
    answer = 0
    m = temp[0]

    for i in list(temp):
        if i == m:
            continue
        else:
            m = i
            answer += 1

    return answer//2 if answer%2 == 0 else answer//2 + 1

def main():
    print(solution("0001100"))

main()