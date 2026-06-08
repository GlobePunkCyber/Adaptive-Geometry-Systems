import os
import pandas as pd
import matplotlib.pyplot as plt

from geometry import (
    build_route,
    calculate_curvature,
    calculate_stationing,
    format_station
)

from vehicle import (
    simulate_vehicle,
    calculate_risk
)


def main():
    os.makedirs("../../outputs", exist_ok=True)

    route = build_route()
    curvature = calculate_curvature(route)
    stations = calculate_stationing(route)
    speeds = simulate_vehicle(curvature)
    risk = calculate_risk(curvature, speeds)

    df = pd.DataFrame({
        "station_distance": stations,
        "station_label": [format_station(s) for s in stations],
        "x": route[:, 0],
        "y": route[:, 1],
        "curvature": curvature,
        "predicted_speed_mph": speeds,
        "risk_score": risk
    })

    df.to_csv("../../outputs/geometry_motion_output.csv", index=False)

    plt.figure()
    scatter = plt.scatter(
        route[:, 0],
        route[:, 1],
        c=curvature,
        cmap="plasma",
        s=12
    )

    plt.colorbar(scatter, label="Curvature")
    plt.title("Curvature-Aware Route Geometry")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True)

    for i in range(0, len(route), 25):
        plt.text(
            route[i, 0],
            route[i, 1],
            format_station(stations[i]),
            fontsize=8
        )

    plt.show()

    plt.figure()
    plt.plot(stations, speeds)
    plt.title("Vehicle Speed Behavior by Station")
    plt.xlabel("Station Distance")
    plt.ylabel("Predicted Speed mph")
    plt.grid(True)
    plt.show()

    plt.figure()
    risk_plot = plt.scatter(
        route[:, 0],
        route[:, 1],
        c=risk,
        cmap="inferno",
        s=12
    )

    plt.colorbar(risk_plot, label="Risk Score")
    plt.title("Geometry-Based Motion Risk")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
