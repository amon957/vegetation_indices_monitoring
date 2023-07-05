# -*- coding: utf-8 -*-
"""

@author: Amon Melly
"""

import ee
import geemap

ee.Authenticate()
ee.Initialize()


def acquire_image(start_date,end_date,study_area):
    image = (ee.ImageCollection("COPERNICUS/S2")
             .filterBounds(study_area)
             .filterDate(start_date,end_date)
             .sort('CLOUDY_PIXEL_PERCENTAGE')
             .first()
             .select('B[1-8]')
             .clip(study_area)
            )
    return image


study_area=ee.Collection.loadTable("projects/ee-amon-melly/assets/maize_plantation").geometry()

start_date=['2022-03-11','2022-04-01','2022-05-11','2022-06-11','2022-07-20',
       '2022-08-11','2022-09-11','2022-10-15','2022-11-20','2022-12-05']
end_date=['2022-03-20','2022-04-10','2022-05-20','2022-06-20','2022-07-30',
     '2022-08-20','2022-09-20','2022-10-25','2022-11-30','2022-12-15']

images={}
for i in range(len(start_date)):
    image = acquire_image(start_date[i],end_date[i],study_area)
    images['image_'+start_date[i]]=image

