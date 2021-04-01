# 落在某圆的点
import math

import matplotlib.pyplot as plt
import numpy as np


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def wsn(_pNum, _rNum, _radius):
    # 生成圆
    # 生成点
    # 判断在圆内的点
    # 最后画圆和画点

    begin = 0
    end = 100
    step = 10
    axes = plt.gca()
    plt.figure(figsize=(5, 5), dpi=80)
    # 设置x, y轴限制
    axes.set_xlim([begin, end])
    axes.set_ylim([begin, end])
    # 设置x, y轴精度
    plt.xticks(np.arange(begin, end, step))
    plt.yticks(np.arange(begin, end, step))
    pList = np.random.uniform(begin, end, [2, _pNum])
    # rList = np.random.uniform(begin, end, [2, _rNum])
    # 如果圆必须全部在坐标轴里
    rList = np.random.uniform(begin + _radius, end - _radius, [2, _rNum])
    # 画圆
    for rIndex in range(0, len(rList[0])):
        x1 = rList[0][rIndex]
        y1 = rList[1][rIndex]
        plt.gca().add_artist(plt.Circle((x1, y1), _radius, fill=False))
    # 画点
    for pIndex in range(0, len(pList[0])):
        x1 = pList[0][pIndex]
        y1 = pList[1][pIndex]

        for rIndex in range(0, len(rList[0])):
            x2 = rList[0][rIndex]
            y2 = rList[1][rIndex]
            dis = distance(x1, y1, x2, y2)
            if dis <= _radius:
                plt.scatter([x1], [y1], c='r', marker=".", s=2)
                break

    plt.show()


if __name__ == '__main__':
    wsn(500, 5, 10)
