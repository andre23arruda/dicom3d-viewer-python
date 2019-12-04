# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:29:42 2019

@author: alca0
"""
#%%
import pydicom

dicom_obj = pydicom.dcmread(r"C:\Users\alca0\Downloads\img_example\136_BIOIMAGEM_ARC_45_20190713_CC_L_2.dcm")
dicom_obj.add_new(0x999999,'HUE', 'HARPIA' )
dicom_obj