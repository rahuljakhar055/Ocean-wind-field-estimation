import ee
from fastapi import FastAPI
from wind_data import get_era5_wind

PROJECT_ID = "wind-field-estimation"

ee.Initialize(project=PROJECT_ID)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Ocean Wind Field API is running"
    }

@app.get("/wind")
def get_wind(
    start_date: str,
    end_date: str,
    min_lon: float,
    min_lat: float,
    max_lon: float,
    max_lat: float
):
    region = ee.Geometry.Rectangle([
        min_lon, min_lat,
        max_lon, max_lat
    ])

    wind = get_era5_wind(start_date, end_date, region)

    stats = wind.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=25000,
        maxPixels=1e9
    ).getInfo()

    return {
        "start_date": start_date,
        "end_date": end_date,
        "area": {
            "min_lon": min_lon,
            "min_lat": min_lat,
            "max_lon": max_lon,
            "max_lat": max_lat
        },
        "mean_wind_speed_mps": stats["wind_speed"],
        "mean_wind_direction_degree": stats["wind_direction"]
    }