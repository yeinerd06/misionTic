from multiprocessing import Condition


i = 1
n = 21

if(i % 2 != 0):
    i += 1
if(n % 2 != 0):
    n -= 1

while (i <= n):
    if (i == 8 or i == 18):
        i += 2
        continue
    print(i)
    i += 2
