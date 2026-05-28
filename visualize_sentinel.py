import ee
import geemap

ee.Initialize(project="wind-field-estimation")

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

collection = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-01-01", "2024-02-01")
    .filter(ee.Filter.eq("instrumentMode", "IW"))
    .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV"))
)

image = collection.median().select("VV")

Map = geemap.Map(center=[10.5, 79.5], zoom=7)

Map.addLayer(
    image,
    {"min": -25, "max": 0},
    "Sentinel-1 VV"
)

Map.addLayer(region, {}, "AOI")

Map.to_html("results/sentinel1_map.html")

print("Map saved to results/sentinel1_map.html")