from osgeo import gdal

filename = r"C:\Desktop\area\shouguang_predict.tif"
input_raster = gdal.Open(filename)
output_raster = r"C:\Desktop\NEW_shouguang_predict.tif"
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:4326')
warp = None # Closes the files
