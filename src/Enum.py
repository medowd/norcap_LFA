'''
Created on Jan 12, 2017

@author: medowd
'''

def enum(**named_values):
    return type('Enum', (), named_values)

TaxFilingStatus = enum(SINGLE='single', MFJ = 'mfj')