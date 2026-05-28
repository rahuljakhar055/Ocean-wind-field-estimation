import ee
import math

def get_era5_wind(start_date, end_date, region):
    era5 = (
        ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY")
        .filterBounds(region)
        .filterDate(start_date, end_date)
        .select([
            "u_component_of_wind_10m",
            "v_component_of_wind_10m"
        ])
        .mean()
    )

    u = era5.select("u_component_of_wind_10m")
    v = era5.select("v_component_of_wind_10m")

    wind_speed = u.pow(2).add(v.pow(2)).sqrt().rename("wind_speed")

    wind_direction = (
        v.atan2(u)
        .multiply(180 / math.pi)
        .add(180)
        .rename("wind_direction")
    )

    return wind_speed.addBands(wind_direction)