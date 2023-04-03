import subprocess as sp
import time

sp.run('python3 test_nn.py', shell = True) # Warm start

times = []

for _ in range(3):
    start = time.time()
    sp.run('python3 test_nn.py', shell = True)
    times.append(time.time() - start)

time2 = []
for _ in range(3):
    start = time.time()
    sp.run('python3 test_nn.py', shell = True)
    times2.append(time.time() - start)



