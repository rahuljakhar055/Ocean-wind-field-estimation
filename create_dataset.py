import ee
import pandas as pd
from wind_data import get_era5_wind

PROJECT_ID = "YOUR_PROJECT_ID"
ee.Initialize(project=PROJECT_ID)

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

# Sentinel-1 SAR
sar = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-01-01", "2024-02-01")
    .filter(ee.Filter.eq("instrumentMode", "IW"))
    .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV"))
    .median()
    .select("VV")
)

# ERA5 wind
wind = get_era5_wind("2024-01-01", "2024-01-02", region)

# Combine SAR + wind bands
combined = sar.addBands(wind)

samples = combined.sample(
    region=region,
    scale=25000,
    geometries=True
)

features = samples.getInfo()["features"]

rows = []

for f in features:
    lon, lat = f["geometry"]["coordinates"]
    props = f["properties"]

    rows.append([
        lon,
        lat,
        props.get("VV"),
        props.get("wind_speed"),
        props.get("wind_direction")
    ])

df = pd.DataFrame(
    rows,
    columns=["lon", "lat", "VV", "wind_speed", "wind_direction"]
)

df = df.dropna()

print(df.head())
print("Rows:", len(df))

df.to_csv("results/ml_dataset.csv", index=False)

print("Saved: results/ml_dataset.csv")