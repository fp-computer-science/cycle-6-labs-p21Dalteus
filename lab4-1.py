# Author DA (AMDG) 10/28/2020

import time
import math

t = time.perf_counter()

math.pow(2, 2)

c = time.perf_counter()

speed1 = c - t

print(speed1)

d = time.perf_counter()

2 ** 2

a = time.perf_counter()

speed2 = a - d
print(speed2)