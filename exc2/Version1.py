import numpy as np
import matplotlib.pyplot as plt


class Visualising:
    def __init__(self, t_range):
        self.t = t_range
        self.lambdat = 5 * np.sin(2 * np.pi * self.t)
        self.ht = 3 * np.pi * np.exp(-self.lambdat)

    def plot(self):
        plt.plot(self.t, self.ht)
        plt.title('h(t) Graph')
        plt.xlabel('t')
        plt.ylabel('h(t)')
        plt.show()


f1 = Visualising(np.arange(0, 1, 0.02))  # adjust the range and step of t. The minimal positive period is 1
f1.plot()