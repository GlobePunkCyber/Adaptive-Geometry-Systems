import os
import pandas as pd
import matplotlib.pyplot as plt

from geometry import build_route, calculate_curvature
from vehicle import simulate_vehicle


def main():
    os.makedirs("../../outputs", exist_ok=True)

    route = build_route()
    curvature = calculate_curvature(route)
    speeds = simulate_vehicle(curvature)

    df = pd.DataFrame({
        "x": route[:, 0],
        "y": route[:, 1],
        "curvature": curvature,
        "predicted_speed_mph": speeds
    })

    df.to_csv("../../outputs/geometry_motion_output.csv", index=False)

    plt.figure()
    plt.plot(route[:, 0], route[:, 1])
    plt.title("Survey-Based Route Geometry")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(speeds)
    plt.title("Vehicle Speed Behavior Based on Curvature")
    plt.xlabel("Station Point")
    plt.ylabel("Predicted Speed mph")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
