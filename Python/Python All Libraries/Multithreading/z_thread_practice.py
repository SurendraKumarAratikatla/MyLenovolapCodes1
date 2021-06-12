import concurrent.futures
import time

start = time.perf_counter()

def dosomthing():
    print(f'sleeping 1 second')
    time.sleep(1)
    return 'Done sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(dosomthing) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

final = time.perf_counter()

print(f"Finished in {round(final-start,2)} seconds")
