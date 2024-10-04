def solution(n, temp):
    temp = list(map(int, temp.split(" ")))
    temp.sort()

    array = []
    count = 1
    for i in temp:
        if i > count:
            break
        else:
            count += i
            
    
    return count

def main():
    print(solution(5, "3 2 1 1 9"))
    print(solution(3, "3 5 7"))

main()