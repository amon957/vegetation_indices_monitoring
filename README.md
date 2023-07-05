# vegetation_indices_monitoring
Monitor vegetation indices in crop land from planting to post harvesting season
## Vegetation Indices
### Normalized Difference Vegetation Index (NDVI)
NDVI=(NIR-Red)/(NIR+Red)
- NIR is the reflectance in the near-infrared band
- Red is the reflectance in the red band
- Ranges from -1 to +1
### Enhanced Vegetation Index (EVI)
EVI = G * ((NIR - Red) / (NIR + C1 * Red – C2 * Blue + L))
- NIR is the reflectance in the near-infrared band
- Red is the reflectance in the red band
- Blue is the reflectance in the blue band
- G is the gain factor to normalize the EVI values
- C1 and C2 are coefficients that minimize atmospheric influences
- L is the canopy background adjustment factor
- Ranges from -1 to +1
### Soil-Adjusted Vegetation Index (SAVI)
SAVI = ((NIR - Red) / (NIR + Red + L)) * (1 + L)
- NIR is the reflectance in the near-infrared band
- Red is the reflectance in the red band
- L is the soil adjustment factor, which ranges from 0 to 1
- Ranges from -1 to +1
### Green Normalized Difference Vegetation Index (GNDVI)
GNDVI = (NIR - Green) / (NIR + Green)
- NIR is the reflectance in the near-infrared band
- Green is the reflectance in the green band
- Ranges from -1 to +1
### Normalized Difference Water Index (NDWI)
NDWI = (NIR - SWIR) / (NIR + SWIR)
- NIR is the reflectance in the near-infrared band
- SWIR is the reflectance in the shortwave infrared band
- Ranges from -1 to +1
![Sample Vegetation Indices Over Time](Vegetation_Indices_Maps.png)
## Tools
- Google Earth Engine
- QGIS
- Python
## Data
- Sentinel 2
