# Ocean Wind Field Estimation using Sentinel-1 SAR Imagery

## Project Overview

This project focuses on estimating ocean wind fields over Indian coastal regions using Sentinel-1 SAR (Synthetic Aperture Radar) imagery and meteorological datasets. The system is designed for offshore wind farm planning applications along the Tamil Nadu or Gujarat coast.

The user provides:

* Date range
* Area of interest (AOI)

The system processes:

* Sentinel-1 SAR imagery
* ERA5 wind datasets

And returns:

* Wind speed
* Wind direction
* Wind vector visualization
* API-based JSON response

---

# Objectives

* Retrieve Sentinel-1 SAR imagery using Google Earth Engine
* Estimate ocean wind fields over coastal regions
* Generate wind speed maps and vector plots
* Build an API for automated wind field retrieval
* Visualize wind vectors for wind farm planning

---

# Dataset Used

## 1. Sentinel-1 SAR Imagery

Source:

* Google Earth Engine
* Dataset: `COPERNICUS/S1_GRD`

Bands used:

* VV polarization

## 2. ERA5 Wind Data

Source:

* ECMWF ERA5 Land Hourly dataset

Parameters used:

* u_component_of_wind_10m
* v_component_of_wind_10m

---

# Technologies Used

* Python
* Google Earth Engine (GEE)
* FastAPI
* Geemap
* Matplotlib
* NumPy
* Pandas

---


# Example API Response

```json id="wyjlwm"
{
  "start_date": "2024-01-01",
  "end_date": "2024-01-02",
  "mean_wind_speed_mps": 5.2,
  "mean_wind_direction_degree": 118.4
}
```

---

# Methodology

1. User provides date and area of interest
2. Sentinel-1 SAR imagery is fetched from Google Earth Engine
3. ERA5 wind data is retrieved
4. Wind speed and direction are calculated
5. Wind vectors are visualized
6. API returns JSON response

---

# Results

The project generates:

* Sentinel-1 SAR visualization
* Wind speed heatmaps
* Wind vector arrows
* API-based wind estimation results

---

# Applications

* Offshore wind farm planning
* Coastal wind analysis
* Marine meteorology
* Renewable energy studies

---

# Future Work

* Machine Learning based wind estimation
* Deep Learning using ResNet/CNN
* Real-time wind field estimation
* Web dashboard deployment

---

# References

1. Sentinel-1 SAR Dataset – Google Earth Engine
2. ECMWF ERA5 Wind Dataset
3. ESA SNAP Toolbox Documentation
4. Wind Direction Retrieval from Sentinel-1 SAR Images using ResNet
