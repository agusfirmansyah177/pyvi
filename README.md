# Python Vegetation Indices (PyVI)

The PyVI is used to automate the computation of vegetation indices using the Python language. PyVI is designed with two formulas, namely Google Earth Engine (GEE)-based and NumPy-based. Therefore, you can directly use this code on data in Earth Engine Image format (ee.Image) or NumPy array accessed using GDAL or Rasterio.

This code is free to use. For now, only 30 vegetation indices are available. However, vegetation indices will continue to be updated. Of course, you are required to cite every literature of the vegetation indices you use.

## Instructions:

### Cloning:

```
!git clone https://github.com/syamaniulm/pyvi
```

##### Note:

You must install Git software (https://git-scm.com/) beforehand if you want to clone the code into your computer.

### Examples of use in GEE environment:

```
...

red = s2_image.select('B4')
nir = s2_image.select('B8')

from pyvi.vegetation_indices import Geevi

ndvi_image = Geevi.ndvi(red,nir)

```

### Examples of use in NumPy Array:

```
...

red = image_array[:,:,3]
nir = image_array[:,:,7]

from pyvi.vegetation_indices import Npvi

ndvi_array = Npvi.ndvi(red,nir)

```

## List of Vegetation Indices:

1. Difference Vegetation Index (DVI)
2. Weighted Difference Vegetation Index (WDVI)
3. Ratio Vegetation Index (RVI)
4. Normalized Difference Vegetation Index (NDVI)
5. Renormalized Difference Vegetation Index (RDVI)
6. Soil Adjusted Vegetation Index (SAVI)
7. Transformed Soil Adjusted Vegetation Index (TSAVI)
8. Modified Soil Adjusted Vegetation Index (MSAVI)
9. Optimized Soil Adjusted Vegetation Index (OSAVI)
10. Perpendicular Vegetation Index (PVI)
11. Infrared Percentage Vegetation Index (IPVI)
12. Transformed Normalized Difference Vegetation Index (TNDVI)
13. Green Difference Vegetation Index (GDVI)
14. Green Normalized Difference Vegetation Index (GNDVI)
15. Global Environmental Monitoring Index (GEMI)
16. Atmospherically Resistant Vegetation Index (ARVI)
17. Normalized Difference Index 45 (NDI45)
18. Modified Chlorophyll Absorption Reflectance Index (MCARI)
19. Enhanced Vegetation Index (EVI)
20. Sentinel-2 Red-Edge Position Index (S2REP)
21. Inverted Red-Edge Chlorophyll Index (IRECI)
22. Pigment Specific Simple Ratio (PSSRa)
23. Anthocyanin Reflectance Index (ARI)
24. Green Leaf Index (GLI)
25. Leaf Chlorophyll Index (LCI)
26. Chlorophyll Vegetation Index (CVI)
27. Carotenoid Reflectance Index 550 nm (CRI550)
28. Carotenoid Reflectance Index 700 nm (CRI700)
29. Canopy Chlorophyll Content Index (CCCI)
30. Transformed Vegetation Index (TVI)
