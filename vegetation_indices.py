# -*- coding: utf-8 -*-
"""

@author: Amon Melly
"""

def getNDVI(image):
    NDVI = image.normalizedDifference(['B8','B4']).rename('NDVI')
    return(image.addBands(NDVI))

def getEVI(image):
    EVI = image.expression(
        '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
            'NIR': image.select('B8').divide(10000),
            'RED': image.select('B4').divide(10000),
            'BLUE': image.select('B2').divide(10000)
        }).rename("EVI")
    return(image.addBands(EVI))

def getSAVI(image):
    SAVI = image.expression(
        '((NIR - Red) / (NIR + Red + 0.5)) * (1 + 0.5)', {
            'NIR': image.select('B8').divide(10000),
            'RED': image.select('B4').divide(10000)
        }).rename("SAVI")
    return(image.addBands(SAVI))

def getGNDVI(image):
    GNDVI = image.normalizedDifference(['B8','B3']).rename('GNDVI')
    return(image.addBands(GNDVI))

def getNDWI(image):
    NDWI = image.normalizedDifference(['B8A','B11']).rename('NDWI')
    return(image.addBands(NDWI))