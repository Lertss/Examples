# Roll four dice.

# What is the probability that the four outcomes are all different?
# Compare this probability to the experiment: Roll three dice.

# What is the probability that the sum of four outcomes is equal to 13?


from random import randint as randi

import matplotlib.pyplot as plt
import numpy as np

three = []
four = []
thirteen = []

for j in range(10):
    N = 100000
    counts = 0
    count = 0
    count_sum = 0
    for k in range(1, N + 1):
        d1 = randi(1, 6)
        d2 = randi(1, 6)
        d3 = randi(1, 6)
        d4 = randi(1, 6)
        if d1 != d2 & d2 != d3 & d3 != d4 & d4 != d1:
            count += 1
        if k % 100000 == 0:
            ratios = count / k
            four.append(ratios)

        sums = d1 + d2 + d3 + d4
        if sums == 13:
            count_sum += 1
        if k % 100000 == 0:
            ratios = count_sum / k
            thirteen.append(ratios)

    for k in range(1, N + 1):
        d1 = randi(1, 6)
        d2 = randi(1, 6)
        d3 = randi(1, 6)
        if d1 != d2 & d2 != d3 & d3 != d1:
            counts += 1
        if k % 100000 == 0:
            ratio = counts / k
            three.append(ratio)

res = (four[0] + four[1] + four[2] + four[3] + four[4] + four[5] + four[6] + four[7] + four[8] + four[9]) / 10
res_thirteen = (thirteen[0] + thirteen[1] + thirteen[2] + thirteen[3] + thirteen[4] + thirteen[5] + thirteen[6] +
                thirteen[7] + thirteen[8] + thirteen[9]) / 10
print("Prawdopodobieństwo, że wszystkie cztery wyniki będą różne jest ", res)
print("Prawdopodobieństwo, że suma wszystkich czterech wyników wyniesie 13 jest ", res_thirteen)
# Porównanie
labels = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10"]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, three, width, label='three')
rects2 = ax.bar(x + width / 2, four, width, label='four')

ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3, rotation=70)
ax.bar_label(rects2, padding=3, rotation=70)

fig.tight_layout()

plt.show()
