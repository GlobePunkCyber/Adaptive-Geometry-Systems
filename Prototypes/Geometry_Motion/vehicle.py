import numpy as np


def simulate_vehicle(curvature):
    speeds = []

    for k in curvature:
        if k < 0.005:
            speed = 55
        elif k < 0.02:
            speed = 40
        else:
            speed = 25

        speeds.append(speed)

    return np.array(speeds)
