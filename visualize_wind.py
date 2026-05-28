import ee
import geemap
from wind_data import get_era5_wind

ee.Initialize(project="wind-field-estimation")

region = ee.Geometry.Rectangle([78.0, 8.0, 80.5, 13.5])

wind = get_era5_wind(
    "2024-01-01",
    "2024-01-02",
    region
)

Map = geemap.Map(center=[10.5, 79.5], zoom=7)

Map.addLayer(
    wind.select("wind_speed"),
    {"min": 0, "max": 12, "palette": ["blue", "cyan", "yellow", "red"]},
    "Wind Speed"
)

Map.addLayer(region, {}, "AOI")

Map.to_html("results/wind_speed_map.html")

print("Saved: results/wind_speed_map.html")