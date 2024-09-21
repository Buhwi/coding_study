def solution():
    #실제 코드를 작성하는 부분
    return 0


import time
import psutil

def mem_usage():
    p = psutil.Process()
    #byte를 사람이 인지하기 쉬운 megabyte로 변환
    #megabyte이므로 1024 * 1024의 값을 나눠줌
    print(f'mem usage : {p.memory_info().rss/2**20}MB')

def main():
    start_time = time.process_time()

    print(solution())

    end_time = time.process_time()
    print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")

main()
mem_usage()