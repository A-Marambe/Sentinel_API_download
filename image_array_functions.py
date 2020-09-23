########################################################
# this fiel contains functionality for raster operations
# Author: Yahampath Anuruddha Marambe
#######################################################

# imports
import rasterio as ras
from rasterio.enums import Resampling as resa
#from rasterio.warp import reproject, Resampling


# shorter function
def raster_resample(input_raster, upscale_factor=2):
    """
    resample image to an given scale
    input_raster : image path
    upscale_factor: default 2 for 20m >> 10m converstion
    """
    with ras.open(input_raster) as dataset:

        # resample data
        data = dataset.read(
            out_shape=(dataset.count,
                       int(dataset.height * upscale_factor),
                       int(dataset.width * upscale_factor)
                       ),
                       resampling = resa.bilinear)

        # sacale image transform
        transform = dataset.transform * dataset.transform.scale(
            (dataset.width/data.shape[-1]),
            (dataset.height/data.shape[-2])
        )
        return data

        
# try following gdal function specially for tiff files
#input_Dir = 'sample.tif'
#ds = gdal.Translate('', input_Dir, xres=0.1, yres=0.1, resampleAlg="bilinear", format='vrt')        


# normalizing the array
def normalize(array):
    """
    normalize an arrary : to prepare to write png
    input: array(any 2D arrray)
    output: noramalized array between 0 -1 
    """
    array_min, array_max = array.min(), array.max()
    return (array - array_min)/(array_max-array_min)

#create an alpha channel
def create_alpha_channel(array_1, array_2):
    """
    create a alpha channel for layer transperanacy
    input: array_1 = a known array, array_2 = a known array with same dimentions
    output: nan, 1 value array
    """
    # get shape of array tuple
    arr_shape = array_1.shape
    # create an zero arrya with the above dimentions
    alpha_zero = np.zeros(shape=arr_shape)
    # nan value set to zero
    alpha_zero[alpha_zero== 0.0]= np.nan
    # conditional to assign 1 instead zero
    alpha = np.where((array_1 > 0) & (array_2 > 0), 1.0, alpha_zero)
    return alpha

