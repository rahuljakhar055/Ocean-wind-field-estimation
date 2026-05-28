import ee

ee.Initialize(project="wind-field-estimation")

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

collection = (
    ee.ImageCollection("COPERNICUS/S1_GRD")
    .filterBounds(region)
    .filterDate("2024-01-01", "2024-02-01")
    .filter(ee.Filter.eq("instrumentMode", "IW"))
    .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV"))
)

print("Image count:", collection.size().getInfo())

first = collection.first()
print("First image:", first.getInfo())

image = collection.select("VV").median()
print("Final image:", image.getInfo())