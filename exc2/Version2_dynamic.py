import numpy as np
import matplotlib.pyplot as plt


def simple_plot():
    plt.figure(figsize=(8, 6), dpi=80)
    plt.ion()
    for index in range(100):
        plt.cla()
        plt.title("Graph")
        plt.grid(True)
        x = np.linspace(-1.5 + 0.1*index, 1.5+0.1*index, 256, endpoint=True)
        y = 3 * np.pi * np.exp(-5 * np.sin(2 * np.pi * x))
        # set x axis
        plt.xlabel("X")
        plt.xlim(-3 + 0.1*index, 3 + 0.1*index)
        plt.xticks(np.linspace(-3 + 0.1*index, 3+0.1*index, 9, endpoint=True))
        # set y axis
        plt.ylabel("Y")
        plt.ylim(-1.0, 1400.0)
        plt.yticks(np.linspace(0, 1400, 20, endpoint=True))
        plt.plot(x, y, "g-", linewidth=2.0, label="h(t)")
        plt.legend(loc="upper left", shadow=True)
        plt.pause(0.1)
    plt.ioff()
    plt.show()
    return


simple_plot()