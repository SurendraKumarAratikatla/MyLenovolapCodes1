# insteading of doing in therading_ex1.py code this is
# something needed using threading module
import time
import threading

start = time.perf_counter()
def dosomething():
    print("Sleeping 1 second....")
    time.sleep(1)
    print('Done sleeping')

#dosomething()
#dosomething()

t1 = threading.Thread(target=dosomething)
t2 = threading.Thread(target=dosomething)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')