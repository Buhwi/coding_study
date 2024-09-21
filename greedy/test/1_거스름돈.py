def solution(n):
    answer = []
    coin = [500, 100, 50, 10]

    for i in coin:
        answer.append(n//i)
        n %= i
    return answer

def main():
    print(solution(1260))

main()