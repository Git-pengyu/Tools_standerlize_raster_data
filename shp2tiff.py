# -*- coding: UTF-8 -*-

from osgeo import ogr
from osgeo import gdal
import rasterio
import os


def main(image, shapefile, label_file):

    # making the shapefile as an object.
    input_shp = ogr.Open(shapefile)

    # getting layer information of shapefile.
    shp_layer = input_shp.GetLayer()
    print('shengh')
    # pixel_size determines the size of the new raster.
    # pixel_size is proportional to size of shapefile.
    pixel_size = 1

    # get extent values to set size of output raster.
    # x_min, x_max, y_min, y_max = shp_layer.GetExtent()

    bounds = get_image_bonds(image)
    x_min = -1 * bounds.left
    y_min = -1 * bounds.bottom
    x_max = bounds.right
    y_max = bounds.top
    # calculate size/resolution of the raster.
    x_res = int(abs(x_max - x_min))
    y_res = int(abs(y_max - y_min))

    # get GeoTiff driver by
    image_type = 'GTiff'
    driver = gdal.GetDriverByName(image_type)

    # passing the filename, x and y direction resolution, no. of bands,
    # new raster.
    output_raster = label_file
    new_raster = driver.Create(output_raster, x_res, y_res, 1, gdal.GDT_Byte)

    # transforms between pixel raster space to projection coordinate space.
    new_raster.SetGeoTransform((x_min, pixel_size, 0, y_min, 0, pixel_size))

    # get required raster band.
    band = new_raster.GetRasterBand(1)

    # assign no data value to empty cells.
    no_data_value = -9999
    band.SetNoDataValue(no_data_value)
    band.FlushCache()

    # main conversion method
    gdal.RasterizeLayer(new_raster, [1], shp_layer, burn_values=[255])

    return gdal.Open(output_raster)


def get_image_bonds(image: str):
    dataset = rasterio.open(os.path.abspath(image))
    print(dataset.bounds)
    return dataset.bounds


if __name__ == '__main__':
    input_path = r'C:\Desktop\水体\image'
    shp_path = r'C:\Desktop\水体\shp'
    label_path = r'C:\Desktop\水体\label'

    content = [f for f in os.listdir(input_path)
               if os.path.isfile(os.path.join(input_path, f))]

    for each in content:    # 路径里的文件名

        img_file = os.path.join(input_path, each)
        print(img_file)
        shp_file = os.path.join(shp_path, each[0:-4]+'.shp')
        label_file = os.path.join(label_path, each[0:-4]+'.tif')
        main(img_file, shp_file, label_file)
