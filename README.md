# Python Vegetation Indices (PyVI)

The PyVI is used to automate the computation of vegetation indices using the Python language. PyVI is designed with two formulas, namely Google Earth Engine (GEE)-based and NumPy-based. Therefore, you can directly use this code on data in Earth Engine Image format (ee.Image) or NumPy array accessed using GDAL or Rasterio.

This code is free to use. For now, only 30 vegetation indices are available. However, vegetation indices will continue to be updated. Of course, you are required to cite every literature of the vegetation indices you use.

## Instructions:

### Cloning:

```
!git clone https://github.com/syamaniulm/pyvi
```

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

#### Note:

You must install Git software (https://git-scm.com/) beforehand if you want to clone the code into your computer.
