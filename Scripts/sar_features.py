import ee
import pandas as pd

PROJECT_ID = "wind-field-estimation"

ee.Initialize(project=PROJECT_ID)

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

collection = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-01-01", "2024-02-01")
    .filter(ee.Filter.eq("instrumentMode", "IW"))
    .filter(ee.Filter.listContains(
        "transmitterReceiverPolarisation",
        "VV"
    ))
)

image = collection.median().select("VV")

samples = image.sample(
    region=region,
    scale=25000,
    geometries=True
)

features = samples.getInfo()["features"]

rows = []

for f in features:
    lon, lat = f["geometry"]["coordinates"]
    vv = f["properties"]["VV"]

    rows.append([lon, lat, vv])

df = pd.DataFrame(rows, columns=["lon", "lat", "VV"])

print(df.head())

df.to_csv("results/sar_features.csv", index=False)

print("Saved: results/sar_features.csv")