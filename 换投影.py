# from re import M
# from osgeo import gdal
# import rasterio as rio
# from rasterio.windows import Window
# from rasterio.transform import Affine
# from rasterio.warp import reproject, Resampling
# # filename = r"C:\Desktop\GF2_PMS2_E118.7_N36.8.tif "  # "C:\Desktop\GF2_PMS2_E118.7_N36.8_20190404_L1A0003922071-MSS2.tiff"   
# # input_raster = gdal.Open(filename,gdal.GA_ReadOnly)
# # output_raster = r"C:\Desktop\GF2_PMS2_E118.7_N36.8.tif " 
# # warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:3857')
# # warp = None # Closes the files
# # fn_GF2 = r'C:\Desktop\GF2_PMS2_E118.7_N36.8.tif'

# # fn_google = r'C:\Desktop\area\shouguang_predict.tif'
# # with rio.open(fn_google) as input_file:
# #         meta_google = input_file.meta
# #         print(meta_google)
# with rio.open(fn_GF2) as input_file:
#         meta_GF = input_file.meta
#         print(meta_GF)
import numpy as np
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

dst_crs = 'EPSG:4326'

with rasterio.open(r'C:\Desktop\shouguang_predict.tif') as src:
    transform, width, height = calculate_default_transform(
        src.crs, dst_crs, src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open('4236test2.tif', 'w', **kwargs) as dst:
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)