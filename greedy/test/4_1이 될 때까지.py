def solution(n, k):
    count = 0
    while True:
        if n == 1:
            break
        if n%k == 0:
            n = n // k
        else :
            n -= 1
        count += 1
    return count

def main():
    print(solution(25, 5))

main()