import ee
from wind_data import get_era5_wind

ee.Initialize(project="wind-field-estimation")

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

wind = get_era5_wind(
    "2024-01-01",
    "2024-01-02",
    region
)

print(wind.getInfo())