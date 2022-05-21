import time

start_time = time.time()
prew = cur = 1
n = int(input())
for i in range(n-2):
    tmp = prew + cur
    prew = cur
    cur = tmp
print(tmp)
print("--- %s seconds ---" % (time.time() - start_time))
