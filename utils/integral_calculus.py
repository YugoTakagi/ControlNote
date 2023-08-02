import numpy as np


def integral_calculus(x, dt):
    list_s = []
    s = 0
    for i in range(len(x)):
        if i == 0:
            sub_s = 0
        else:
            sub_s = (x[i - 1] + x[i]) * dt / 2.
        s += sub_s
        list_s.append(s)
    return np.array(list_s)
