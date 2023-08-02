import numpy as np


def trapezoid(t, distance, vel, acc_max):
    t1 = vel / acc_max
    t2 = distance / vel
    t3 = t2 + t1

    if (0 <= t) and (t < t1):
        return acc_max * t
    elif (t1 <= t) and (t <= t2):
        return vel
    elif (t2 < t) and (t <= t3):
        return -acc_max * t + (acc_max * t3)
    else:
        return 0


def make_vel_prof(t, distance, vel, acc_max):
    u = []
    for _t in t:
        u.append(trapezoid(_t, distance=distance, vel=vel, acc_max=acc_max))
    u = np.array(u)
    return u
