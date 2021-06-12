import concurrent.futures
import time

start = time.perf_counter()

def dosomething(second):
    print(f'sleeping {second} seconds...')
    time.sleep(second)
    return f'Done sleeping...{second}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    #result = executor.map(dosomething,seconds)

    # for f in result:
    #     print(f)

    # or

    executor.map(dosomething,seconds)

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')