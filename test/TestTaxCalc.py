'''
Created on Jan 12, 2017

@author: medowd
'''
import unittest
from TaxCalc import *
from Enum import TaxFilingStatus

class TestTaxCalc(unittest.TestCase):
 
    def setUp(self):
        pass
    
    def test_fed_single_0(self):
        bracket = FEDERAL_BRACKETS[0]
        self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.SINGLE), 0)
        self.assertEqual(fedTaxIncremental(bracket, TaxFilingStatus.SINGLE), 907.5)
        with self.assertRaises(Exception) as context:
            fedTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE)
        self.assertTrue('Cannot calculate previous bracket tax total for lowest tax bracket.' in context.exception)
 
    def test_fed_single_3(self):
        bracket = FEDERAL_BRACKETS[3]
        self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.SINGLE), 89350)
        self.assertEqual(fedTaxIncremental(bracket, TaxFilingStatus.SINGLE), 27160.000000000004)
        self.assertEqual(fedTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE), 18193.75)
        
    def test_fed_single_6(self):
        bracket = FEDERAL_BRACKETS[6]
        self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.SINGLE), 406750)
        with self.assertRaises(Exception) as context:
            fedTaxIncremental(bracket, TaxFilingStatus.SINGLE)
        self.assertTrue('Cannot calculate incremental tax for highest tax bracket.' in context.exception)
        self.assertEqual(fedTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE), 118118.75)

    def test_state_single_0(self):
        bracket = STATE_BRACKETS[0]
        self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.SINGLE), 0)
        self.assertEqual(stateTaxIncremental(bracket, TaxFilingStatus.SINGLE), 75.82000000000001)
        with self.assertRaises(Exception) as context:
            stateTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE)
        self.assertTrue('Cannot calculate previous bracket tax total for lowest tax bracket.' in context.exception)
 
    def test_state_single_3(self):
        bracket = STATE_BRACKETS[3]
        self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.SINGLE), 28371)
        self.assertEqual(stateTaxIncremental(bracket, TaxFilingStatus.SINGLE), 660.78)
        self.assertEqual(stateTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE), 699.5)
        
    def test_state_single_8(self):
        bracket = STATE_BRACKETS[8]
        self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.SINGLE), 508500)
        with self.assertRaises(Exception) as context:
            stateTaxIncremental(bracket, TaxFilingStatus.SINGLE)
        self.assertTrue('Cannot calculate incremental tax for highest tax bracket.' in context.exception)
        self.assertEqual(stateTaxPrevBracketTotal(bracket, TaxFilingStatus.SINGLE), 49429.498)
    
#     def test_fed_mfj_0(self):
#         bracket = FEDERAL_BRACKETS[0]
#         self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.MFJ), 0)
#         self.assertEqual(fedTaxIncremental(bracket, TaxFilingStatus.MFJ), 907.5)
#         with self.assertRaises(Exception) as context:
#             fedTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ)
#         self.assertTrue('Cannot calculate previous bracket tax total for lowest tax bracket.' in context.exception)
#  
#     def test_fed_mfj_3(self):
#         bracket = FEDERAL_BRACKETS[3]
#         self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.MFJ), 89350)
#         self.assertEqual(fedTaxIncremental(bracket, TaxFilingStatus.MFJ), 27160.000000000004)
#         self.assertEqual(fedTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ), 18193.75)
#         
#     def test_fed_mfj_6(self):
#         bracket = FEDERAL_BRACKETS[6]
#         self.assertEqual(fedTaxActive(bracket, TaxFilingStatus.MFJ), 406750)
#         with self.assertRaises(Exception) as context:
#             fedTaxIncremental(bracket, TaxFilingStatus.MFJ)
#         self.assertTrue('Cannot calculate incremental tax for highest tax bracket.' in context.exception)
#         self.assertEqual(fedTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ), 118118.75)
# 
#     def test_state_mfj_0(self):
#         bracket = STATE_BRACKETS[0]
#         self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.MFJ), 0)
#         self.assertEqual(stateTaxIncremental(bracket, TaxFilingStatus.MFJ), 75.82000000000001)
#         with self.assertRaises(Exception) as context:
#             stateTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ)
#         self.assertTrue('Cannot calculate previous bracket tax total for lowest tax bracket.' in context.exception)
#  
#     def test_state_mfj_3(self):
#         bracket = STATE_BRACKETS[3]
#         self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.MFJ), 28371)
#         self.assertEqual(stateTaxIncremental(bracket, TaxFilingStatus.MFJ), 660.78)
#         self.assertEqual(stateTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ), 699.5)
#         
#     def test_state_mfj_8(self):
#         bracket = STATE_BRACKETS[8]
#         self.assertEqual(stateTaxActive(bracket, TaxFilingStatus.MFJ), 508500)
#         with self.assertRaises(Exception) as context:
#             stateTaxIncremental(bracket, TaxFilingStatus.MFJ)
#         self.assertTrue('Cannot calculate incremental tax for highest tax bracket.' in context.exception)
#         self.assertEqual(stateTaxPrevBracketTotal(bracket, TaxFilingStatus.MFJ), 49429.498)
        
if __name__ == '__main__':
    unittest.main()