import math

import matplotlib.pyplot as plt
import numpy as np


def head(p: float, r: int) -> float:
    """
    触头选举
    :param p: 期望触头在所有节点中的百分比
    :param r: 选举轮数
    :return: 阈值
    """
    return p / (1 - p * np.mod(r, 1 / p))


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def initDraw(begin, end, step):
    plt.figure(figsize=(5, 5))  # 画布大小
    axes = plt.gca()
    # 设置x, y轴限制
    axes.set_xlim([begin, end])
    axes.set_ylim([begin, end])
    # 设置x, y轴精度
    plt.xticks(np.arange(begin, end, step))
    plt.yticks(np.arange(begin, end, step))


def wsn():
    # 生成节点
    # 🐢️判断触头
    # 生成100个节点
    # 分类成触头和非触头
    # 非触头连接最近触头
    # 🔗️连接触头
    xm = 100  # x的范围
    ym = 100  # y的范围
    n = 100  # 传感器节点的数量
    p = 0.08  # 期望触头在所有节点中的百分比
    r = 1  # 选举轮数
    initDraw(0, xm, 10)  # 初始化画布
    tn = head(p, r)
    pList = np.random.uniform(0, ym, [2, n])
    pRandList = np.random.uniform(0, 1, [1, n])  # 每个节点产生0-1的随机数
    headList = []
    noHeadList = []
    for i in range(0, n):
        plt.scatter(pList[0][i], pList[1][i], c='r', marker=".")
    for i in range(0, n):
        if pRandList[0][i] < tn:
            headList.append([pList[0][i], pList[1][i]])
        else:
            noHeadList.append([pList[0][i], pList[1][i]])

    for i1 in range(0, noHeadList.__len__()):
        x1 = noHeadList[i1][0]
        y1 = noHeadList[i1][1]
        dis = 9999
        tx = -1
        ty = -1
        isConnect = False
        for i2 in range(0, headList.__len__()):
            x2 = headList[i2][0]
            y2 = headList[i2][1]
            tempDis = distance(x1, y1, x2, y2)
            if tempDis < dis:
                isConnect = True
                dis = tempDis
                tx = x2
                ty = y2
        if isConnect:
            plt.plot([x1, tx], [y1, ty], "b", linewidth=0.8)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    wsn()
