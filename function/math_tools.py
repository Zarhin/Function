import numpy as np
import pandas as pd


def get_points(point1, point2, point3, L, N=100):
    """获取指定方向的离散点
        1) 通过point1和point2确定一条直线l1
        2) 过point3做一条垂直与l1的直线l2
        3) 以point3为圆心，以L为半径，从直线l2中截取一段AB
        4) 将线段AB离散为N个点，并输出
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    if x1 == x2:
        k = 0
        p1 = [x3 - L, y3]
        p2 = [x3 + L, y3]
    elif y1 == y2:
        k = None
        p1 = [x3, y3 - L]
        p2 = [x3, y3 + L]
    else:
        k = (x2 - x1) / (y1 - y2)
        incr_x = (L / (1.0 + k**2))**0.5
        incr_y = k * incr_x
        p1 = [x3 - incr_x, y3 - incr_y]
        p2 = [x3 + incr_x, y3 + incr_y]
    points = np.linspace(p1, p2, N)
    return points


def _create_line(point1, point2):
    """通过两点确定一条直线

    理论：
        直线方程的一般式:Ax+By+C=0
    Return:
        [a, b, c]
    """
    x1, y1 = point1
    x2, y2 = point2
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return [a, b, c]


def _get_cross_point(point1, point2, point3):
    """获取两个垂直直线的交点 和 点到直线的距离
        
        1) 根据point1 和point2两点确定一条直线l1
        2) 过point3做垂直于l1的直线l2
        3) 计算l1和l2两条直线的交线和点point3到直线l1的距离
    """
    x3, y3 = point3
    a0, b0, c0 = _create_line(point1, point2)
    a1, b1, c1 = b0, -a0, -b0 * x3 + y3 * a0
    D = a0 * b1 - a1 * b0
    if D == 0:
        return None
    x = (b0 * c1 - b1 * c0) / D
    y = (a1 * c0 - a0 * c1) / D
    distance = abs(a0 * x3 + b0 * y3 + c0) / (a0**2 + b0**2)**0.5
    return x, y, distance


def _get_distance(point1, point2, point3):
    """获取点到直线的距离
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    point3 = np.array(point3)
    vec1 = point2 - point1
    vec2 = point3 - point1
    vec3 = point1 - point2
    distance = np.cross(vec1, vec2) / np.linalg.norm(vec3)
    return abs(distance)