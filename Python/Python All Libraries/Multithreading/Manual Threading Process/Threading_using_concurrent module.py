import concurrent.futures
import time
# it will give thread pool executor,
# when we use this thread pool executor, usually best use context manager


start = time.perf_counter()
def dosomething(seconds):
    print(f"Sleeping {seconds} second....")
    time.sleep(1)
    return 'Done sleeping'

with concurrent.futures.ThreadPoolExecutor() as execute:
    results = [execute.submit(dosomething,1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')