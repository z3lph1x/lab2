
import numpy as np
import matplotlib.pyplot as plt

with open(input(), 'r') as f:
    nums = f.read().splitlines()
N = np.zeros(len(nums))
for i in range(len(nums)):
    N[i] = float(nums[i])
U = np.array([N])
l = U.size
lx = np.arange(l)
t = np.zeros(l)
A = np.array([np.zeros(l)]*l)
for i in range(l-1):
    A[i][i] = A[i][i] + 1
    A[i+1][i] = A[i+1][i] -1
plt.ion()
for i in range(255):
    plt.clf()
    plt.plot(lx,U.T)
    plt.axis([0,50,0,10])
    plt.draw()
    plt.gcf().canvas.flush_events()
    plt.pause(0.1)
    U = U - 0.5 * U.dot(A)
plt.ioff()
plt.show()

