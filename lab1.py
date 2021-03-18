import math

import matplotlib.pyplot as plt
import numpy as np


def distance(x1: float, x2: float, y1: float, y2: float) -> float:
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def wsn(_num):
    begin = 0
    end = 100
    plt.figure(figsize=(15, 15))
    axes = plt.gca()
    axes.set_xlim([begin, end])
    axes.set_ylim([begin, end])
    plt.xticks(np.arange(0, end, 10))
    plt.yticks(np.arange(0, end, 10))
    randomList = np.random.uniform(begin, end, [2, _num])
    plt.scatter(randomList[0], randomList[1], c='r', marker="o")
    for curIndex in range(0, len(randomList[0])):
        for nextIndex in range(0, len(randomList[0])):
            x1 = randomList[0][curIndex]
            y1 = randomList[1][curIndex]
            x2 = randomList[0][nextIndex]
            y2 = randomList[1][nextIndex]
            if x1 == x2 and y1 == y2:
                continue
            dis = distance(x1, x2, y1, y2)
            if dis <= 15.0:
                plt.plot([x1, x2], [y1, y2], "b", linewidth=0.4)
    plt.title(f'{_num} Label')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    isFull = False
    number = 150
    wsn(number)
