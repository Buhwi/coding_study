def solution(n, array):
    answer = 0
    array.sort()
    
    while True:
        if not array:
            break

        a = max(array)
        n = len(array)

        if n-a >= 0:
            answer += 1
            array = array[:n-a:]
        else:
            answer += 1
            break
        
    return answer


import time
import psutil

def mem_usage():
    p = psutil.Process()
    #byte를 사람이 인지하기 쉬운 megabyte로 변환
    #megabyte이므로 1024 * 1024의 값을 나눠줌
    print(f'mem usage : {p.memory_info().rss/2**20}MB')

def main(big_array, big_len):
    print(solution(5, [2, 3, 1, 2, 2]))
    print(solution(big_len, big_array))



start_time = time.process_time()

main(big_array, big_len)

mem_usage()

end_time = time.process_time()


print(f"time elapsed : {round((end_time - start_time) * 1000, 3)}ms")