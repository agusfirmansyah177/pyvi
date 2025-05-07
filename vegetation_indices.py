# -*- coding: utf-8 -*-
"""
Created on Fri May 02 09:39:08 2025

@author: Syam'ani
Faculty of Forestry, Universitas Lambung Mangkurat
Banjarbaru, Indonesia

Python Vegetation Indices (PyVI)
Version 3.0

"""

import numpy as np
import scipy as sp
import ee

# Google Earth Engine-based Vegetation Indices (GEEVI) class
class Geevi:
    
    # Difference Vegetation Index (DVI)
    @staticmethod
    def dvi(red,nir):
        dvi_eq = nir.subtract(red).rename('DVI')
        print("------------------------------------------------------------------------------")
        print("You are using Difference Vegetation Index (DVI) (Richardson and Wiegand, 1977)")
        print("------------------------------------------------------------------------------")
        print("Cite as:")
        print("Richardson, A. J., Wiegand, C. L., 1977. "+
              "Distinguishing vegetation from soil background information. "+
              "Photogrammetric Engineering and Remote Sensing 43 (12), 1541-1552.")
        return dvi_eq
    
    # Weighted Difference Vegetation Index (WDVI)
    @staticmethod
    def wdvi(red,nir,a=0.46):
        wdvi_eq = nir.subtract((red).multiply(a)).rename('WDVI')
        print("-------------------------------------------------------------------------")
        print("You are using Weighted Difference Vegetation Index (WDVI) (Clevers, 1991)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Clevers, J.G.P.W., 1991. "+
              "Application of the WDVI in estimating LAI at the generative stage of barley. "+
              "ISPRS Journal of Photogrammetry and Remote Sensing 46 (1), 37-47. "+
              "doi: https://doi.org/10.1016/0924-2716(91)90005-G")
        return wdvi_eq
    
    # Ratio Vegetation Index (RVI)
    @staticmethod
    def rvi(red,nir):
        rvi_eq = nir.divide(red).rename('RVI')
        print("---------------------------------------------------------------")
        print("You are using Ratio Vegetation Index (RVI) (Major et al., 1990)")
        print("---------------------------------------------------------------")
        print("Cite as:")
        print("Major, D.J., Baret, F., Guyot, G., 1990. "+
              "A ratio vegetation index adjusted for soil brightness. "+
              "International Journal of Remote Sensing 11 (5), 727-740. "+
              "doi: https://doi.org/10.1080/01431169008955053")
        return rvi_eq
    
    # Normalized Difference Vegetation Index (NDVI)
    @staticmethod
    def ndvi(red,nir):
        ndvi_eq = (nir.subtract(red)).divide(nir.add(red)).rename('NDVI')
        print("--------------------------------------------------------------------------------")
        print("You are using Normalized Difference Vegetation Index (NDVI) (Rouse et al., 1974)")
        print("--------------------------------------------------------------------------------")
        print("Cite as:")
        print("Rouse, J. W., Jr., Haas Jr., R. H., Schell, J. A., Deering, D. W., 1974. "+
              "Monitoring vegetation systems in the Great Plains with ERTS. "+
              "In: Freden, S.C., Mercanti, E.P., Becker, M.A. (Eds.), "+
              "Third Earth Resources Technology Satellite-1 Symposium, NASA SP-351 I, Washington, DC, 309-317.")
        return ndvi_eq
    
    # Renormalized Difference Vegetation Index (RDVI)
    @staticmethod
    def rdvi(red,nir):
        rdvi_eq = (nir.subtract(red)).divide(ee.Image.sqrt(nir.add(red)).multiply(0.5)).rename('RDVI')
        print("---------------------------------------------------------------------------------------")
        print("You are using Renormalized Difference Vegetation Index (RDVI) (Broge and Leblanc, 2001)")
        print("---------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Broge, N.H., Leblanc, E., 2001. "+
              "Comparing prediction power and stability of broadband and hyperspectral vegetation indices for estimation of green leaf area index and canopy chlorophyll density. "+
              "Remote Sensing of Environment 76 (2), 156-172. "+
              "doi: https://doi.org/10.1016/S0034-4257(00)00197-8")
        return rdvi_eq
    
    # Soil Adjusted Vegetation Index (SAVI)
    @staticmethod
    def savi(red,nir,l=0.5):
        savi_eq = ((nir.subtract(red)).divide((nir.add(red).add(l))).multiply(1+l)).rename('SAVI')
        print("-----------------------------------------------------------------")
        print("You are using Soil Adjusted Vegetation Index (SAVI) (Huete, 1988)")
        print("-----------------------------------------------------------------")
        print("Cite as:")
        print("Huete, A. R., 1988. "+
              "A soil-adjusted vegetation index (SAVI). "+
              "Remote Sensing of Environment 25 (3), 295-309. "+
              "doi: https://doi.org/10.1016/0034-4257(88)90106-X")
        return savi_eq
    
    # Transformed Soil Adjusted Vegetation Index (TSAVI)
    @staticmethod
    def tsavi(red,nir,a=0.5,s=0.5,x=0.08):
        tsavi_eq = ((nir.subtract(red.multiply(s)).subtract(a)).multiply(s)).divide((nir.multiply(s)).add(red).subtract(a*s+x*(1+s**2))).rename('TSAVI')
        print("----------------------------------------------------------------------------------------")
        print("You are using Transformed Soil Adjusted Vegetation Index (TSAVI) (Baret and Guyot, 1991)")
        print("----------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Baret, F., Guyot, G., 1991. "+
              "Potentials and limits of vegetation indices for LAI and APAR assessment. "+
              "Remote Sensing of Environment 35 (2-3), 161-173. "+
              "doi: https://doi.org/10.1016/0034-4257(91)90009-U")
        return tsavi_eq
    
    # Modified Soil Adjusted Vegetation Index (MSAVI)
    @staticmethod
    def msavi(red,nir,s=0.5,a=0.46):
        ndvi = (nir.subtract(red)).divide(nir.add(red))
        wdvi = nir.subtract(red.multiply(a))
        l = ee.Image(1).subtract(ee.Image(2*s).multiply(ndvi).multiply(wdvi))
        msavi_eq = ((nir.subtract(red)).multiply(l.add(1))).divide(nir.add(red).add(l)).rename('MSAVI')
        print("-------------------------------------------------------------------------------")
        print("You are using Modified Soil Adjusted Vegetation Index (MSAVI) (Qi et al., 1994)")
        print("-------------------------------------------------------------------------------")
        print("Cite as:")
        print("Qi, J., Chehbouni, A., Huete, A.R., Kerr, Y.H., Sorooshian, S, 1994. "+
              "A modified soil adjusted vegetation index. "+
              "Remote Sensing of Environment 48 (2), 119-126. "+
              "doi: https://doi.org/10.1016/0034-4257(94)90134-1")
        return msavi_eq
    
    # Optimized Soil Adjusted Vegetation Index (OSAVI)
    @staticmethod
    def osavi(red,nir,y=0.16):
        osavi_eq = ((nir.subtract(red)).multiply(1+y)).divide(nir.add(red).add(y)).rename('OSAVI')
        print("--------------------------------------------------------------------------------------------------------------")
        print("You are using Optimized Soil Adjusted Vegetation Index (OSAVI) (Rondeaux et al., 1996; Haboudane et al., 2002)")
        print("--------------------------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Rondeaux, G., Steven, M., Baret, F., 1996. "+
              "Optimization of soil-adjusted vegetation indices. "+
              "Remote Sensing of Environment 55 (2), 95-107. "+
              "doi: https://doi.org/10.1016/0034-4257(95)00186-7")
        print("Haboudane, D., Miller, J.R., Tremblay, N., Zarco-Tejada, P.J., Dextraze, L., 2002. "+
              "Integrated narrow-band vegetation indices for prediction of crop chlorophyll content for application to precision agriculture. "+
              "Remote Sensing of Environment 81 (2-3), 416-426. "+
              "doi: https://doi.org/10.1016/S0034-4257(02)00018-4")
        return osavi_eq
    
    # Perpendicular Vegetation Index (PVI)
    @staticmethod
    def pvi(red,nir):
        pvi_eq = (nir.subtract(red)).divide(ee.Image.sqrt(nir.add(red)).multiply(0.5)).rename('PVI')
        print("---------------------------------------------------------------------------------")
        print("You are using Perpendicular Vegetation Index (PVI) (Richardson and Wiegand, 1977)")
        print("---------------------------------------------------------------------------------")
        print("Cite as:")
        print("Richardson, A. J., Wiegand, C. L., 1977. "+
              "Distinguishing vegetation from soil background information. "+
              "Photogrammetric Engineering and Remote Sensing 43 (12), 1541-1552.")
        return pvi_eq
    
    # Infrared Percentage Vegetation Index (IPVI)
    @staticmethod
    def ipvi(red,nir):
        ipvi_eq = nir.divide(nir.add(red)).rename('IPVI')
        print("-------------------------------------------------------------------------")
        print("You are using Infrared Percentage Vegetation Index (IPVI) (Crippen, 1990)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Crippen, R.E., 1990. "+
              "Calculating the vegetation index faster. "+
              "Remote Sensing of Environment 34 (1), 71-73. "+
              "doi: https://doi.org/10.1016/0034-4257(90)90085-Z")
        return ipvi_eq
    
    # Transformed Normalized Difference Vegetation Index (TNDVI)
    @staticmethod
    def tndvi(red,nir):
        tndvi_eq = ee.Image.sqrt(((nir.add(red)).divide(nir.add(red))).add(0.5)).rename('TNDVI')
        print("------------------------------------------------------------------------------------------------")
        print("You are using Transformed Normalized Difference Vegetation Index (TNDVI) (Senseman et al., 1996)")
        print("------------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Senseman, G.M., Bagley, C.F., Tweddale, S.A., 1996. "+
              "Correlation of rangeland cover measures to satellite‐imagery‐derived vegetation indices. "+
              "Geocarto International 11 (3), 29-38. "+
              "doi: https://doi.org/10.1080/10106049609354546")
        return tndvi_eq
    
    # Green Difference Vegetation Index (GDVI)
    @staticmethod
    def gdvi(green,nir):
        gdvi_eq = nir.subtract(green).rename('GDVI')
        print("----------------------------------------------------------------------------")
        print("You are using Green Difference Vegetation Index (GDVI) (Tucker et al., 1979)")
        print("----------------------------------------------------------------------------")
        print("Cite as:")
        print("Tucker, C.J., Elgin Jr., J.H., McMurtrey III, J.E., Fan, C.J., 1979. "+
              "Monitoring corn and soybean crop development with hand-held radiometer spectral data. "+
              "Remote Sensing of Environment 8 (3), 237-248. "+
              "doi: https://doi.org/10.1016/0034-4257(79)90004-X")
        return gdvi_eq
    
    # Green Normalized Difference Vegetation Index (GNDVI)
    @staticmethod
    def gndvi(green,nir):
        gndvi_eq = (nir.subtract(green)).divide(nir.add(green)).rename('GNDVI')
        print("------------------------------------------------------------------------------------------")
        print("You are using Green Normalized Difference Vegetation Index (GNDVI) (Gitelson et al., 1996)")
        print("------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Kaufman, Y.J., Merzlyak, M.N., 1996. "+
              "Use of a green channel in remote sensing of global vegetation from EOS-MODIS. "+
              "Remote Sensing of Environment 58 (3), 289-298. "+
              "doi: https://doi.org/10.1016/S0034-4257(96)00072-7")
        return gndvi_eq
    
    # Global Environmental Monitoring Index (GEMI)
    @staticmethod
    def gemi(red,nir):
        eta = ((nir.pow(2).subtract(red.pow(2))).multiply(2).add(nir.multiply(1.5)).add(red.multiply(0.5))).divide(nir.add(red).add(0.5))
        gemi_eq = eta.multiply(ee.Image(1).subtract(eta.multiply(0.25))).subtract((red.subtract(0.125)).divide(ee.Image(1).subtract(red))).rename('GEMI')
        print("---------------------------------------------------------------------------------------")
        print("You are using Global Environmental Monitoring Index (GEMI) (Pinty and Verstraete, 1992)")
        print("---------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Pinty, B., Verstraete, M.M., 1992. "+
              "GEMI: a non-linear index to monitor global vegetation from satellites. "+
              "Vegetatio 101, 15–20. "+
              "doi: https://doi.org/10.1007/BF00031911")
        return gemi_eq
    
    # Atmospherically Resistant Vegetation Index (ARVI)
    @staticmethod
    def arvi(blue,red,nir):
        arvi_eq = (nir.subtract(red.multiply(2).subtract(blue))).divide(nir.add(red.multiply(2).subtract(blue))).rename('ARVI')
        print("-----------------------------------------------------------------------------------------")
        print("You are using Atmospherically Resistant Vegetation Index (ARVI) (Kaufman and Tanre, 1992)")
        print("-----------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Kaufman, Y.J., Tanre, D., 1992. "+
              "Atmospherically resistant vegetation index (ARVI) for EOS-MODIS. "+
              "IEEE Transactions on Geoscience and Remote Sensing 30 (2), 261-270. "+
              "doi: https://doi.org/10.1109/36.134076")
        return arvi_eq
    
    # Normalized Difference Index 45 (NDI45)
    @staticmethod
    def ndi45(red,re1):
        ndi45_eq = (re1.subtract(red)).divide(re1.add(red)).rename('NDI45')
        print("----------------------------------------------------------------------------")
        print("You are using Normalized Difference Index 45 (NDI45) (Delegido et al., 2011)")
        print("----------------------------------------------------------------------------")
        print("Cite as:")
        print("Delegido, J., Verrelst, J., Alonso, L., Moreno, J., 2011. "+
              "Evaluation of Sentinel-2 Red-Edge Bands for Empirical Estimation of Green LAI and Chlorophyll Content. "+
              "Sensors 11 (7), 7063-7081. "+
              "doi: https://doi.org/10.3390%2Fs110707063")
        return ndi45_eq
    
    # Modified Chlorophyll Absorption Reflectance Index (MCARI)
    @staticmethod
    def mcari(green,red,re1):
        mcari_eq = ((re1.subtract(red)).subtract((re1.subtract(green)).multiply(0.2))).multiply(re1.divide(red)).rename('MCARI')
        print("-----------------------------------------------------------------------------------------------")
        print("You are using Modified Chlorophyll Absorption Reflectance Index (MCARI) (Daughtry et al., 2000)")
        print("-----------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Daughtry, C.S.T., Walthall, C.L., Kim, M.S., Brown de Colstoun, E., McMurtrey III, J.E., 2000. "+
              "Estimating Corn Leaf Chlorophyll Concentration from Leaf and Canopy Reflectance. "+
              "Remote Sensing of Environment 74 (2), 229-239. "+
              "doi: https://doi.org/10.1016/S0034-4257(00)00113-9")
        return mcari_eq
    
    # Enhanced Vegetation Index (EVI)
    @staticmethod
    def evi(blue,red,nir):
        evi_eq = ((nir.subtract(red)).multiply(2.5)).divide(nir.add(red.multiply(6)).subtract(blue.multiply(7.5)).add(1)).rename('EVI')
        print("-------------------------------------------------------------------")
        print("You are using Enhanced Vegetation Index (EVI) (Huete et. al., 2002)")
        print("-------------------------------------------------------------------")
        print("Cite as:")
        print("Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. "+
              "Overview of the radiometric and biophysical performance of the MODIS vegetation indices. "+
              "Remote Sensing of Environment 83 (1-2), 195-213. "+
              "doi: https://doi.org/10.1016/S0034-4257(02)00096-2")
        return evi_eq
    
    # Sentinel-2 Red-Edge Position Index (S2REP)
    @staticmethod
    def s2rep(red,re1,re2,re3):
        s2rep_eq = (((red.add(re3)).divide(2).subtract(re1)).divide(re2.subtract(re1))).multiply(35).add(705).rename('S2REP')
        print("--------------------------------------------------------------------------------")
        print("You are using Sentinel-2 Red-Edge Position Index (S2REP) (Guyot and Baret, 1988)")
        print("--------------------------------------------------------------------------------")
        print("Cite as:")
        print("Guyot, G., Baret, F., 1988. "+
              "Utilisation de la Haute Resolution Spectrale pour Suivre L'etat des Couverts Vegetaux. "+
              "Proceedings 4th Int. Coll. Spectral Signatures of Objects in Remote Sensing, Aussois, France, ESA SP-287, 195-213. ")
        return s2rep_eq
    
    # Inverted Red-Edge Chlorophyll Index (IRECI)
    @staticmethod
    def ireci(red,re1,re2,re3):
        ireci_eq = (re3.subtract(red)).divide(re1.divide(re2)).rename('IRECI')
        print("---------------------------------------------------------------------------------")
        print("You are using Inverted Red-Edge Chlorophyll Index (IRECI) (Clevers et. al., 2000)")
        print("---------------------------------------------------------------------------------")
        print("Cite as:")
        print("Clevers, J.G.P.W., De Jong, S.M., Epema, G.F., Addink, E.A., 2000. "+
              "MERIS and the Red-Edge Index. "+
              "Second EARSeL Workshop on Imaging Spectroscopy, 2000, Enschede.")
        return ireci_eq
    
    # Pigment Specific Simple Ratio (PSSRa)
    @staticmethod
    def pssra(red,re):
        pssra_eq = re.divide(red).rename('PSSRa')
        print("---------------------------------------------------------------------")
        print("You are using Pigment Specific Simple Ratio (PSSRa) (Blackburn, 1998)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Blackburn, G.A., 1998. "+
              "Quantifying Chlorophylls and Caroteniods at Leaf and Canopy Scales: An Evaluation of Some Hyperspectral Approaches. "+
              "Remote Sensing of Environment 66 (3), 273-285. "+
              "doi: https://doi.org/10.1016/S0034-4257(98)00059-5")
        return pssra_eq
    
    # Anthocyanin Reflectance Index (ARI)
    @staticmethod
    def ari(green,re1):
        ari_eq = (ee.Image(1).divide(green)).subtract(ee.Image(1).divide(re1)).rename('ARI')
        print("-------------------------------------------------------------------------")
        print("You are using Anthocyanin Reflectance Index (ARI) (Gitelson et al., 2009)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Chivkunova, O.B., Merzlyak, M.N., 2009. "+
              "Nondestructive estimation of anthocyanins and chlorophylls in anthocyanic leaves. "+
              "American Journal of Botany 96 (10), 1861-1868. "+
              "doi: https://doi.org/10.3732/ajb.0800395")
        return ari_eq
    
    # Green Leaf Index (GLI)
    @staticmethod
    def gli(blue,green,red):
        gli_eq = (ee.Image(2).multiply(green).subtract(red).subtract(blue)).divide(ee.Image(2).multiply(green).add(red).add(blue)).rename('GLI')
        print("----------------------------------------------------------")
        print("You are using Green Leaf Index (GLI) (Gobron et al., 2000)")
        print("----------------------------------------------------------")
        print("Cite as:")
        print("Gobron, N., Pinty, B., Verstraete, M.M., Widlowski, J.L., 2000. "+
              "Advanced vegetation indices optimized for up-coming sensors: Design, performance, and applications. "+
              "IEEE Transactions on Geoscience and Remote Sensing 38 (6), 2489-2505. "+
              "doi: https://doi.org/10.1109/36.885197")
        return gli_eq
    
    # Leaf Chlorophyll Index (LCI)
    @staticmethod
    def lci(red,re1,nir):
        lci_eq = (nir.subtract(re1)).divide(nir.subtract(red)).rename('LCI')
        print("---------------------------------------------------------------------")
        print("You are using Leaf Chlorophyll Index (LCI) (Datt, 1999a; Datt, 1999b)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Datt, B., 1999a. "+
              "A New Reflectance Index for Remote Sensing of Chlorophyll Content in Higher Plants: Tests using Eucalyptus Leaves. "+
              "Journal of Plant Physiology 154 (1), 30-36. "+
              "doi: https://doi.org/10.1016/S0176-1617(99)80314-9")
        print("Datt, B., 1999b. "+
              "Remote Sensing of Water Content in Eucalyptus Leaves. "+
              "Australian Journal of Botany 47 (6), 909-923. "+
              "doi: https://doi.org/10.1071/BT98042")
        return lci_eq
    
    # Chlorophyll Vegetation Index (CVI)
    @staticmethod
    def cvi(green,red,nir):
        cvi_eq = (nir.multiply(red)).divide(green.pow(2)).rename('CVI')
        print("----------------------------------------------------------------------")
        print("You are using Chlorophyll Vegetation Index (CVI) (Gobron et al., 2000)")
        print("----------------------------------------------------------------------")
        print("Cite as:")
        print("Gobron, N., Pinty, B., Verstraete, M.M., Widlowski, J.L., 2000. "+
              "Advanced vegetation indices optimized for up-coming sensors: Design, performance, and applications. "+
              "IEEE Transactions on Geoscience and Remote Sensing 38 (6), 2489-2505. "+
              "doi: https://doi.org/10.1109/36.885197")
        return cvi_eq
    
    # Carotenoid Reflectance Index 550 nm (CRI550)
    @staticmethod
    def cri550(blue,green):
        cri550_eq = (ee.Image(1).divide(blue)).subtract(ee.Image(1).divide(green)).rename('CRI550')
        print("----------------------------------------------------------------------------------")
        print("You are using Carotenoid Reflectance Index 550 nm (CRI550) (Gitelson et al., 2001)")
        print("----------------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Merzlyak, M.N., Chivkunova, O.B., 2001. "+
              "Optical properties and nondestructive estimation of anthocyanin content in plant leaves. "+
              "Photochemistry and Photobiology 74 (1), 38-45. "+
              "doi: https://doi.org/10.1562/0031-8655(2001)074%3C0038:opaneo%3E2.0.co;2")
        return cri550_eq
    
    # Carotenoid Reflectance Index 700 nm (CRI700)
    @staticmethod
    def cri700(blue,re1):
        cri700_eq = (ee.Image(1).divide(blue)).subtract(ee.Image(1).divide(re1)).rename('CRI700')
        print("----------------------------------------------------------------------------------")
        print("You are using Carotenoid Reflectance Index 700 nm (CRI700) (Merzlyak et al., 2003)")
        print("----------------------------------------------------------------------------------")
        print("Cite as:")
        print("Merzlyak, M.N., Gitelson, A.A., Chivkunova, O.B., Solovchenko, A.E., Pogosyan, S.I., 2003. "+
              "Application of Reflectance Spectroscopy for Analysis of Higher Plant Pigments. "+
              "Russian Journal of Plant Physiology 50, 704–710. "+
              "doi: https://doi.org/10.1023/A:1025608728405")
        return cri700_eq
    
    # Canopy Chlorophyll Content Index (CCCI)
    @staticmethod
    def ccci(red,re1,nir):
        ccci_eq = ((nir.subtract(re1)).divide(nir.add(re1))).divide((nir.subtract(red)).divide(nir.add(red))).rename('CCCI')
        print("------------------------------------------------------------------------------")
        print("You are using Canopy Chlorophyll Content Index (CCCI) (El-Shikha et al., 2008)")
        print("------------------------------------------------------------------------------")
        print("Cite as:")
        print("El-Shikha, D.M., Barnes, E.M., Clarke, T.R., Hunsaker, D.J., Haberland, J.A., Pinter Jr., P.J.,  Waller, P.M., Thompson, T.L., 2008. "+
              "Remote Sensing of Cotton Nitrogen Status Using the Canopy Chlorophyll Content Index (CCCI). "+
              "Transactions of the ASABE 51 (1), 73-82. "+
              "doi: https://doi.org/10.13031/2013.24228")
        return ccci_eq
    
    # Transformed Vegetation Index (TVI)
    @staticmethod
    def tvi(red,nir):
        tvi_eq = ee.Image.sqrt(((nir.add(red)).divide(nir.add(red))).add(0.5)).rename('TVI')
        print("---------------------------------------------------------------------")
        print("You are using Transformed Vegetation Index (TVI) (Rouse et al., 1974)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Rouse, J. W., Jr., Haas Jr., R. H., Schell, J. A., Deering, D. W., 1974. "+
              "Monitoring vegetation systems in the Great Plains with ERTS. "+
              "In: Freden, S.C., Mercanti, E.P., Becker, M.A. (Eds.), "+
              "Third Earth Resources Technology Satellite-1 Symposium, NASA SP-351 I, Washington, DC, 309-317.")
        return tvi_eq

# NumPy-based Vegetation Indices (NPVI) class
class Npvi:
    
    # Difference Vegetation Index (DVI)
    @staticmethod
    def dvi(red,nir):
        dvi_eq = nir - red
        print("------------------------------------------------------------------------------")
        print("You are using Difference Vegetation Index (DVI) (Richardson and Wiegand, 1977)")
        print("------------------------------------------------------------------------------")
        print("Cite as:")
        print("Richardson, A. J., Wiegand, C. L., 1977. "+
              "Distinguishing vegetation from soil background information. "+
              "Photogrammetric Engineering and Remote Sensing 43 (12), 1541-1552.")
        return dvi_eq
    
    # Weighted Difference Vegetation Index (WDVI)
    @staticmethod
    def wdvi(red,nir,a=0.46):
        wdvi_eq = nir - a*red
        print("-------------------------------------------------------------------------")
        print("You are using Weighted Difference Vegetation Index (WDVI) (Clevers, 1991)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Clevers, J.G.P.W., 1991. "+
              "Application of the WDVI in estimating LAI at the generative stage of barley. "+
              "ISPRS Journal of Photogrammetry and Remote Sensing 46 (1), 37-47. "+
              "doi: https://doi.org/10.1016/0924-2716(91)90005-G")
        return wdvi_eq
    
    # Ratio Vegetation Index (RVI)
    @staticmethod
    def rvi(red,nir):
        rvi_eq = nir / red
        print("---------------------------------------------------------------")
        print("You are using Ratio Vegetation Index (RVI) (Major et al., 1990)")
        print("---------------------------------------------------------------")
        print("Cite as:")
        print("Major, D.J., Baret, F., Guyot, G., 1990. "+
              "A ratio vegetation index adjusted for soil brightness. "+
              "International Journal of Remote Sensing 11 (5), 727-740. "+
              "doi: https://doi.org/10.1080/01431169008955053")
        return rvi_eq
    
    # Normalized Difference Vegetation Index (NDVI)
    @staticmethod
    def ndvi(red,nir):
        ndvi_eq = (nir-red)/(nir+red)
        print("--------------------------------------------------------------------------------")
        print("You are using Normalized Difference Vegetation Index (NDVI) (Rouse et al., 1974)")
        print("--------------------------------------------------------------------------------")
        print("Cite as:")
        print("Rouse, J. W., Jr., Haas Jr., R. H., Schell, J. A., Deering, D. W., 1974. "+
              "Monitoring vegetation systems in the Great Plains with ERTS. "+
              "In: Freden, S.C., Mercanti, E.P., Becker, M.A. (Eds.), "+
              "Third Earth Resources Technology Satellite-1 Symposium, NASA SP-351 I, Washington, DC, 309-317.")
        return ndvi_eq
    
    # Renormalized Difference Vegetation Index (RDVI)
    @staticmethod
    def rdvi(red,nir):
        rdvi_eq = (nir-red)/np.sqrt(nir+red)*0.5
        print("---------------------------------------------------------------------------------------")
        print("You are using Renormalized Difference Vegetation Index (RDVI) (Broge and Leblanc, 2001)")
        print("---------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Broge, N.H., Leblanc, E., 2001. "+
              "Comparing prediction power and stability of broadband and hyperspectral vegetation indices for estimation of green leaf area index and canopy chlorophyll density. "+
              "Remote Sensing of Environment 76 (2), 156-172. "+
              "doi: https://doi.org/10.1016/S0034-4257(00)00197-8")
        return rdvi_eq
    
    # Soil Adjusted Vegetation Index (SAVI)
    @staticmethod
    def savi(red,nir,l=0.5):
        savi_eq = ((nir-red)/(nir+red+l))*(1+l)
        print("-----------------------------------------------------------------")
        print("You are using Soil Adjusted Vegetation Index (SAVI) (Huete, 1988)")
        print("-----------------------------------------------------------------")
        print("Cite as:")
        print("Huete, A. R., 1988. "+
              "A soil-adjusted vegetation index (SAVI). "+
              "Remote Sensing of Environment 25 (3), 295-309. "+
              "doi: https://doi.org/10.1016/0034-4257(88)90106-X")
        return savi_eq
    
    # Transformed Soil Adjusted Vegetation Index (TSAVI)
    @staticmethod
    def tsavi(red,nir,a=0.5,s=0.5,x=0.08):
        tsavi_eq = (s*(nir-s*red-a))/(s*nir+red-a*s+x*(1+s**2))
        print("----------------------------------------------------------------------------------------")
        print("You are using Transformed Soil Adjusted Vegetation Index (TSAVI) (Baret and Guyot, 1991)")
        print("----------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Baret, F., Guyot, G., 1991. "+
              "Potentials and limits of vegetation indices for LAI and APAR assessment. "+
              "Remote Sensing of Environment 35 (2-3), 161-173. "+
              "doi: https://doi.org/10.1016/0034-4257(91)90009-U")
        return tsavi_eq
    
    # Modified Soil Adjusted Vegetation Index (MSAVI)
    @staticmethod
    def msavi(red,nir,s=0.5,a=0.46):
        ndvi = (nir-red)/(nir+red)
        wdvi = nir - a*red
        l = 1 - 2 * s * ndvi * wdvi
        msavi_eq = ((1+l)*(nir-red))/(nir+red+l)
        print("-------------------------------------------------------------------------------")
        print("You are using Modified Soil Adjusted Vegetation Index (MSAVI) (Qi et al., 1994)")
        print("-------------------------------------------------------------------------------")
        print("Cite as:")
        print("Qi, J., Chehbouni, A., Huete, A.R., Kerr, Y.H., Sorooshian, S, 1994. "+
              "A modified soil adjusted vegetation index. "+
              "Remote Sensing of Environment 48 (2), 119-126. "+
              "doi: https://doi.org/10.1016/0034-4257(94)90134-1")
        return msavi_eq
    
    # Optimized Soil Adjusted Vegetation Index (OSAVI)
    @staticmethod
    def osavi(red,nir,y=0.16):
        osavi_eq = ((1+y)*(nir-red))/(nir+red+y)
        print("--------------------------------------------------------------------------------------------------------------")
        print("You are using Optimized Soil Adjusted Vegetation Index (OSAVI) (Rondeaux et al., 1996; Haboudane et al., 2002)")
        print("--------------------------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Rondeaux, G., Steven, M., Baret, F., 1996. "+
              "Optimization of soil-adjusted vegetation indices. "+
              "Remote Sensing of Environment 55 (2), 95-107. "+
              "doi: https://doi.org/10.1016/0034-4257(95)00186-7")
        print("Haboudane, D., Miller, J.R., Tremblay, N., Zarco-Tejada, P.J., Dextraze, L., 2002. "+
              "Integrated narrow-band vegetation indices for prediction of crop chlorophyll content for application to precision agriculture. "+
              "Remote Sensing of Environment 81 (2-3), 416-426. "+
              "doi: https://doi.org/10.1016/S0034-4257(02)00018-4")
        return osavi_eq
    
    # Perpendicular Vegetation Index (PVI)
    @staticmethod
    def pvi(red,nir):
        pvi_eq = (nir-red)/(0.5*np.sqrt(nir+red))
        print("---------------------------------------------------------------------------------")
        print("You are using Perpendicular Vegetation Index (PVI) (Richardson and Wiegand, 1977)")
        print("---------------------------------------------------------------------------------")
        print("Cite as:")
        print("Richardson, A. J., Wiegand, C. L., 1977. "+
              "Distinguishing vegetation from soil background information. "+
              "Photogrammetric Engineering and Remote Sensing 43 (12), 1541-1552.")
        return pvi_eq
    
    # Infrared Percentage Vegetation Index (IPVI)
    @staticmethod
    def ipvi(red,nir):
        ipvi_eq = nir/(nir+red)
        print("-------------------------------------------------------------------------")
        print("You are using Infrared Percentage Vegetation Index (IPVI) (Crippen, 1990)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Crippen, R.E., 1990. "+
              "Calculating the vegetation index faster. "+
              "Remote Sensing of Environment 34 (1), 71-73. "+
              "doi: https://doi.org/10.1016/0034-4257(90)90085-Z")
        return ipvi_eq
    
    # Transformed Normalized Difference Vegetation Index (TNDVI)
    @staticmethod
    def tndvi(red,nir):
        tndvi_eq = np.sqrt(((nir-red)/(nir+red))+0.5)
        print("------------------------------------------------------------------------------------------------")
        print("You are using Transformed Normalized Difference Vegetation Index (TNDVI) (Senseman et al., 1996)")
        print("------------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Senseman, G.M., Bagley, C.F., Tweddale, S.A., 1996. "+
              "Correlation of rangeland cover measures to satellite‐imagery‐derived vegetation indices. "+
              "Geocarto International 11 (3), 29-38. "+
              "doi: https://doi.org/10.1080/10106049609354546")
        return tndvi_eq
    
    # Green Difference Vegetation Index (GDVI)
    @staticmethod
    def gdvi(green,nir):
        gdvi_eq = nir - green
        print("----------------------------------------------------------------------------")
        print("You are using Green Difference Vegetation Index (GDVI) (Tucker et al., 1979)")
        print("----------------------------------------------------------------------------")
        print("Cite as:")
        print("Tucker, C.J., Elgin Jr., J.H., McMurtrey III, J.E., Fan, C.J., 1979. "+
              "Monitoring corn and soybean crop development with hand-held radiometer spectral data. "+
              "Remote Sensing of Environment 8 (3), 237-248. "+
              "doi: https://doi.org/10.1016/0034-4257(79)90004-X")
        return gdvi_eq
    
    # Green Normalized Difference Vegetation Index (GNDVI)
    @staticmethod
    def gndvi(green,nir):
        gndvi_eq = (nir-green)/(nir+green)
        print("------------------------------------------------------------------------------------------")
        print("You are using Green Normalized Difference Vegetation Index (GNDVI) (Gitelson et al., 1996)")
        print("------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Kaufman, Y.J., Merzlyak, M.N., 1996. "+
              "Use of a green channel in remote sensing of global vegetation from EOS-MODIS. "+
              "Remote Sensing of Environment 58 (3), 289-298. "+
              "doi: https://doi.org/10.1016/S0034-4257(96)00072-7")
        return gndvi_eq
    
    # Global Environmental Monitoring Index (GEMI)
    @staticmethod
    def gemi(red,nir):
        eta = (2*(nir**2-red**2)+1.5*nir+0.5*red)/(nir+red+0.5)
        gemi_eq = eta*(1-0.25*eta)-((red-0.125)/(1-red))
        print("---------------------------------------------------------------------------------------")
        print("You are using Global Environmental Monitoring Index (GEMI) (Pinty and Verstraete, 1992)")
        print("---------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Pinty, B., Verstraete, M.M., 1992. "+
              "GEMI: a non-linear index to monitor global vegetation from satellites. "+
              "Vegetatio 101, 15–20. "+
              "doi: https://doi.org/10.1007/BF00031911")
        return gemi_eq
    
    # Atmospherically Resistant Vegetation Index (ARVI)
    @staticmethod
    def arvi(blue,red,nir):
        arvi_eq = (nir-(2*red-blue))/(nir+(2*red-blue))
        print("-----------------------------------------------------------------------------------------")
        print("You are using Atmospherically Resistant Vegetation Index (ARVI) (Kaufman and Tanre, 1992)")
        print("-----------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Kaufman, Y.J., Tanre, D., 1992. "+
              "Atmospherically resistant vegetation index (ARVI) for EOS-MODIS. "+
              "IEEE Transactions on Geoscience and Remote Sensing 30 (2), 261-270. "+
              "doi: https://doi.org/10.1109/36.134076")
        return arvi_eq
    
    # Normalized Difference Index 45 (NDI45)
    @staticmethod
    def ndi45(red,re1):
        ndi45_eq = (re1-red)/(re1+red)
        print("----------------------------------------------------------------------------")
        print("You are using Normalized Difference Index 45 (NDI45) (Delegido et al., 2011)")
        print("----------------------------------------------------------------------------")
        print("Cite as:")
        print("Delegido, J., Verrelst, J., Alonso, L., Moreno, J., 2011. "+
              "Evaluation of Sentinel-2 Red-Edge Bands for Empirical Estimation of Green LAI and Chlorophyll Content. "+
              "Sensors 11 (7), 7063-7081. "+
              "doi: https://doi.org/10.3390%2Fs110707063")
        return ndi45_eq
    
    # Modified Chlorophyll Absorption Reflectance Index (MCARI)
    @staticmethod
    def mcari(green,red,re1):
        mcari_eq = ((re1-red)-0.2*(re1-green))*(re1/red)
        print("-----------------------------------------------------------------------------------------------")
        print("You are using Modified Chlorophyll Absorption Reflectance Index (MCARI) (Daughtry et al., 2000)")
        print("-----------------------------------------------------------------------------------------------")
        print("Cite as:")
        print("Daughtry, C.S.T., Walthall, C.L., Kim, M.S., Brown de Colstoun, E., McMurtrey III, J.E., 2000. "+
              "Estimating Corn Leaf Chlorophyll Concentration from Leaf and Canopy Reflectance. "+
              "Remote Sensing of Environment 74 (2), 229-239. "+
              "doi: https://doi.org/10.1016/S0034-4257(00)00113-9")
        return mcari_eq
    
    # Enhanced Vegetation Index (EVI)
    @staticmethod
    def evi(blue,red,nir):
        evi_eq = 2.5*((nir-red)/(nir+6*red-7.5*blue+1))
        print("-------------------------------------------------------------------")
        print("You are using Enhanced Vegetation Index (EVI) (Huete et. al., 2002)")
        print("-------------------------------------------------------------------")
        print("Cite as:")
        print("Huete, A., Didan, K., Miura, T., Rodriguez, E.P., Gao, X., Ferreira, L.G., 2002. "+
              "Overview of the radiometric and biophysical performance of the MODIS vegetation indices. "+
              "Remote Sensing of Environment 83 (1-2), 195-213. "+
              "doi: https://doi.org/10.1016/S0034-4257(02)00096-2")
        return evi_eq
    
    # Sentinel-2 Red-Edge Position Index (S2REP)
    @staticmethod
    def s2rep(red,re1,re2,re3):
        s2rep_eq = 705+35*(((red+re3)/2-re1)/(re2-re1))
        print("--------------------------------------------------------------------------------")
        print("You are using Sentinel-2 Red-Edge Position Index (S2REP) (Guyot and Baret, 1988)")
        print("--------------------------------------------------------------------------------")
        print("Cite as:")
        print("Guyot, G., Baret, F., 1988. "+
              "Utilisation de la Haute Resolution Spectrale pour Suivre L'etat des Couverts Vegetaux. "+
              "Proceedings 4th Int. Coll. Spectral Signatures of Objects in Remote Sensing, Aussois, France, ESA SP-287, 195-213. ")
        return s2rep_eq
    
    # Inverted Red-Edge Chlorophyll Index (IRECI)
    @staticmethod
    def ireci(red,re1,re2,re3):
        ireci_eq = (re3-red)/(re1/re2)
        print("---------------------------------------------------------------------------------")
        print("You are using Inverted Red-Edge Chlorophyll Index (IRECI) (Clevers et. al., 2000)")
        print("---------------------------------------------------------------------------------")
        print("Cite as:")
        print("Clevers, J.G.P.W., De Jong, S.M., Epema, G.F., Addink, E.A., 2000. "+
              "MERIS and the Red-Edge Index. "+
              "Second EARSeL Workshop on Imaging Spectroscopy, 2000, Enschede.")
        return ireci_eq
    
    # Pigment Specific Simple Ratio (PSSRa)
    @staticmethod
    def pssra(red,re):
        pssra_eq = re/red
        print("---------------------------------------------------------------------")
        print("You are using Pigment Specific Simple Ratio (PSSRa) (Blackburn, 1998)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Blackburn, G.A., 1998. "+
              "Quantifying Chlorophylls and Caroteniods at Leaf and Canopy Scales: An Evaluation of Some Hyperspectral Approaches. "+
              "Remote Sensing of Environment 66 (3), 273-285. "+
              "doi: https://doi.org/10.1016/S0034-4257(98)00059-5")
        return pssra_eq
    
    # Anthocyanin Reflectance Index (ARI)
    @staticmethod
    def ari(green,re1):
        ari_eq = 1/green - 1/re1
        print("-------------------------------------------------------------------------")
        print("You are using Anthocyanin Reflectance Index (ARI) (Gitelson et al., 2009)")
        print("-------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Chivkunova, O.B., Merzlyak, M.N., 2009. "+
              "Nondestructive estimation of anthocyanins and chlorophylls in anthocyanic leaves. "+
              "American Journal of Botany 96 (10), 1861-1868. "+
              "doi: https://doi.org/10.3732/ajb.0800395")
        return ari_eq
    
    # Green Leaf Index (GLI)
    @staticmethod
    def gli(blue,green,red):
        gli_eq = (2*green-red-blue)/(2*green+red+blue)
        print("----------------------------------------------------------")
        print("You are using Green Leaf Index (GLI) (Gobron et al., 2000)")
        print("----------------------------------------------------------")
        print("Cite as:")
        print("Gobron, N., Pinty, B., Verstraete, M.M., Widlowski, J.L., 2000. "+
              "Advanced vegetation indices optimized for up-coming sensors: Design, performance, and applications. "+
              "IEEE Transactions on Geoscience and Remote Sensing 38 (6), 2489-2505. "+
              "doi: https://doi.org/10.1109/36.885197")
        return gli_eq
    
    # Leaf Chlorophyll Index (LCI)
    @staticmethod
    def lci(red,re1,nir):
        lci_eq = (nir-re1)/(nir-red)
        print("---------------------------------------------------------------------")
        print("You are using Leaf Chlorophyll Index (LCI) (Datt, 1999a; Datt, 1999b)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Datt, B., 1999a. "+
              "A New Reflectance Index for Remote Sensing of Chlorophyll Content in Higher Plants: Tests using Eucalyptus Leaves. "+
              "Journal of Plant Physiology 154 (1), 30-36. "+
              "doi: https://doi.org/10.1016/S0176-1617(99)80314-9")
        print("Datt, B., 1999b. "+
              "Remote Sensing of Water Content in Eucalyptus Leaves. "+
              "Australian Journal of Botany 47 (6), 909-923. "+
              "doi: https://doi.org/10.1071/BT98042")
        return lci_eq
    
    # Chlorophyll Vegetation Index (CVI)
    @staticmethod
    def cvi(green,red,nir):
        cvi_eq = (nir*red)/green**2
        print("----------------------------------------------------------------------")
        print("You are using Chlorophyll Vegetation Index (CVI) (Gobron et al., 2000)")
        print("----------------------------------------------------------------------")
        print("Cite as:")
        print("Gobron, N., Pinty, B., Verstraete, M.M., Widlowski, J.L., 2000. "+
              "Advanced vegetation indices optimized for up-coming sensors: Design, performance, and applications. "+
              "IEEE Transactions on Geoscience and Remote Sensing 38 (6), 2489-2505. "+
              "doi: https://doi.org/10.1109/36.885197")
        return cvi_eq
    
    # Carotenoid Reflectance Index 550 nm (CRI550)
    @staticmethod
    def cri550(blue,green):
        cri550_eq = 1/blue - 1/green
        print("----------------------------------------------------------------------------------")
        print("You are using Carotenoid Reflectance Index 550 nm (CRI550) (Gitelson et al., 2001)")
        print("----------------------------------------------------------------------------------")
        print("Cite as:")
        print("Gitelson, A.A., Merzlyak, M.N., Chivkunova, O.B., 2001. "+
              "Optical properties and nondestructive estimation of anthocyanin content in plant leaves. "+
              "Photochemistry and Photobiology 74 (1), 38-45. "+
              "doi: https://doi.org/10.1562/0031-8655(2001)074%3C0038:opaneo%3E2.0.co;2")
        return cri550_eq
    
    # Carotenoid Reflectance Index 700 nm (CRI700)
    @staticmethod
    def cri700(blue,re1):
        cri700_eq = 1/blue - 1/re1
        print("----------------------------------------------------------------------------------")
        print("You are using Carotenoid Reflectance Index 700 nm (CRI700) (Merzlyak et al., 2003)")
        print("----------------------------------------------------------------------------------")
        print("Cite as:")
        print("Merzlyak, M.N., Gitelson, A.A., Chivkunova, O.B., Solovchenko, A.E., Pogosyan, S.I., 2003. "+
              "Application of Reflectance Spectroscopy for Analysis of Higher Plant Pigments. "+
              "Russian Journal of Plant Physiology 50, 704–710. "+
              "doi: https://doi.org/10.1023/A:1025608728405")
        return cri700_eq
    
    # Canopy Chlorophyll Content Index (CCCI)
    @staticmethod
    def ccci(red,re1,nir):
        ccci_eq = ((nir-re1)/(nir+re1))/((nir-red)/(nir+red))
        print("------------------------------------------------------------------------------")
        print("You are using Canopy Chlorophyll Content Index (CCCI) (El-Shikha et al., 2008)")
        print("------------------------------------------------------------------------------")
        print("Cite as:")
        print("El-Shikha, D.M., Barnes, E.M., Clarke, T.R., Hunsaker, D.J., Haberland, J.A., Pinter Jr., P.J.,  Waller, P.M., Thompson, T.L., 2008. "+
              "Remote Sensing of Cotton Nitrogen Status Using the Canopy Chlorophyll Content Index (CCCI). "+
              "Transactions of the ASABE 51 (1), 73-82. "+
              "doi: https://doi.org/10.13031/2013.24228")
        return ccci_eq
    
    # Transformed Vegetation Index (TVI)
    @staticmethod
    def tvi(red,nir):
        tvi_eq = np.sqrt(((nir-red)/(nir+red))+0.5)
        print("---------------------------------------------------------------------")
        print("You are using Transformed Vegetation Index (TVI) (Rouse et al., 1974)")
        print("---------------------------------------------------------------------")
        print("Cite as:")
        print("Rouse, J. W., Jr., Haas Jr., R. H., Schell, J. A., Deering, D. W., 1974. "+
              "Monitoring vegetation systems in the Great Plains with ERTS. "+
              "In: Freden, S.C., Mercanti, E.P., Becker, M.A. (Eds.), "+
              "Third Earth Resources Technology Satellite-1 Symposium, NASA SP-351 I, Washington, DC, 309-317.")
        return tvi_eq
