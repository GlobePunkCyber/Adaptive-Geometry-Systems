import numpy as np


def generate_line(start, end, spacing=1.0):
    x1, y1 = start
    x2, y2 = end

    length = np.hypot(x2 - x1, y2 - y1)
    n = max(int(length / spacing), 2)

    x = np.linspace(x1, x2, n)
    y = np.linspace(y1, y2, n)

    return np.column_stack((x, y))


def generate_curve(center, radius, start_angle_deg, end_angle_deg, spacing=1.0):
    start = np.radians(start_angle_deg)
    end = np.radians(end_angle_deg)

    arc_length = abs(radius * (end - start))
    n = max(int(arc_length / spacing), 2)

    angles = np.linspace(start, end, n)

    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)

    return np.column_stack((x, y))


def build_route():
    line1 = generate_line((0, 0), (100, 0))

    curve1 = generate_curve(
        center=(100, 50),
        radius=50,
        start_angle_deg=-90,
        end_angle_deg=0
    )

    line2 = generate_line((150, 50), (250, 50))

    return np.vstack((line1, curve1, line2))


def calculate_curvature(points):
    dx = np.gradient(points[:, 0])
    dy = np.gradient(points[:, 1])

    ddx = np.gradient(dx)
    ddy = np.gradient(dy)

    curvature = np.abs(dx * ddy - dy * ddx) / np.maximum(
        (dx**2 + dy**2) ** 1.5,
        1e-6
    )

    return curvature



    return np.array(distances)


def format_station(distance):
    hundreds = int(distance // 100)
    remainder = int(distance % 100)

    return f"Sta {hundreds}+{remainder:02d}"
