import h5py
import pandas as pd
from astropy.table import Table
from astropy.io import fits


"""This is a function that takes fits and hdf data and return them to pandas dataframe"""

# detect = fits.open('/lsst/troxel/balrog/balrog_detection_catalog-v1.2.fits')[-1]
phot   = fits.open('/lsst/troxel/balrog/balrog_matched_catalog_flatten.fits')
id_balrog = fits.open('/lsst/troxel/balrog/balrog_mcal_bal_ids_v1.2.fits')

#load true catalogs in pandas
# detectp_table=Table.read('/lsst/troxel/balrog/balrog_detection_catalog-v1.2.fits').to_pandas()
phot_table=Table.read('/lsst/troxel/balrog/balrog_matched_catalog_flatten.fits').to_pandas()
id_balrog = Table.read('/lsst/troxel/balrog/balrog_mcal_bal_ids_v1.2.fits').to_pandas



#all objects riz
mcal0= h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-riz-mcal-v1.2.h5','r')['catalog'] #with neighbor
mcal1= h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-riz-noNB-mcal-v1.2.h5','r')['catalog'] #no neighbor
##only matched balrog object riz
mcal2=h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-riz-mcal-1.3.h5','r')['catalog'] #with neighbor
mcal3=h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-riz-noNB-mcal-1.3.h5','r')['catalog'] #no neighbor
#only matched balrog object griz
mcal4=h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-griz-mcal-1.3.h5','r')['catalog'] #with neighbor
mcal5=h5py.File('/lsst/troxel/balrog/balrog_mcal_stack-y3v02-0-griz-noNB-mcal-1.3.h5','r')['catalog'] #no neighbor

mcal_list=[mcal0,mcal1,mcal2,mcal3,mcal4,mcal5]

#load mcal catagories in pandas df

for catalog in mcal_list:
    for key in catalog:
        