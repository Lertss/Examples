# Write a program that creates a 10!10 list of random integers between 1 and 100. Then do the following:
# (a) Print the list.
# (b) Find the largest value in the third row.
# (c) Find the smallest value in the sixth column.

import random
import numpy as np

a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(random.randint(0, 100))

print(np.array(a))
print(max(a[2]))

ars = []
for i in range(10):
    ars.append(a[i][5])
print(min(ars))
