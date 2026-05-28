import ee
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wind_data import get_era5_wind

PROJECT_ID = "wind-field-estimation"

ee.Initialize(project=PROJECT_ID)

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

wind = get_era5_wind(
    "2024-01-01",
    "2024-01-02",
    region
)

points = wind.sample(
    region=region,
    scale=25000,
    geometries=True
)

features = points.getInfo()["features"]

rows = []

for f in features:
    lon, lat = f["geometry"]["coordinates"]
    speed = f["properties"]["wind_speed"]
    direction = f["properties"]["wind_direction"]

    u = speed * np.cos(np.deg2rad(direction))
    v = speed * np.sin(np.deg2rad(direction))

    rows.append([lon, lat, speed, direction, u, v])

df = pd.DataFrame(
    rows,
    columns=["lon", "lat", "speed", "direction", "u", "v"]
)

plt.figure(figsize=(8, 8))

plt.quiver(
    df["lon"],
    df["lat"],
    df["u"],
    df["v"],
    df["speed"]
)

plt.colorbar(label="Wind Speed (m/s)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Wind Field Vectors - Tamil Nadu Coast")
plt.grid(True)

plt.savefig("results/wind_vectors.png", dpi=300)
plt.show()

print("Saved: results/wind_vectors.png")
print(df.head())    