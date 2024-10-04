def solution(temp):
    array = list(temp)
    answer = 0
    for i in array:
        if i == '0' or i == '1':
            answer += int(i)
        else:
            if answer == 0:
                answer += 1
            answer *= int(i)
    return answer

def main():
    print(solution("02984"))
    print(solution("567"))

main()