# insteading of doing in therading_ex1.py code this is
# something needed using threading module
import time
import threading

start = time.perf_counter()
def dosomething(seconds):
    print(f"Sleeping {seconds} second....")
    time.sleep(1)
    print('Done sleeping')

threads = []

for _ in range(10):
    t = threading.Thread(target=dosomething, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')