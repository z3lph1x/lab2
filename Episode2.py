
import numpy as np
import matplotlib.pyplot as plt

with open(input(), 'r') as f:
    nums = f.read().splitlines()
N = np.zeros(len(nums))
for i in range(len(nums)):
    N[i] = float(nums[i])
data = np.array([N])
l = data.size
lx = np.arange(l)
new_data = np.zeros(l)
k = 0.
new_data = new_data.T
data = data.T
for i in range(l):
    if i < 10:
        k = data[i] + k
        new_data[i] = k / (i + 1)
    else:
        k = k - data[i-10] + data[i]
        new_data[i] = k / 10
fig, ax = plt.subplots(1, 2)
ax[0].plot(lx, data)
ax[0].set_title("Сырой сигнал")
ax[1].plot(lx, new_data)
ax[1].set_title("После фильтра")

plt.show()
