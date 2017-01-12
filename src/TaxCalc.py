'''
Created on Jan 12, 2017

@author: medowd
'''
from Enum import TaxFilingStatus

SS_PERCENT_COST = 6.2
SS_MAX = 113700
MEDICARE_BASE_RATE = 1.45
MEDICARE_EXTRA_RATE = 0.9

FEDERAL_BRACKETS = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
STATE_BRACKETS = [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123]

FED_SINGLE = [0, 9075, 36900, 89350, 186350, 405100, 406750]
FED_MFJ = [0, 18151, 73800, 148850, 226850, 405100, 457600]

STATE_SINGLE = [0, 7582, 17976, 28371, 39384, 49774, 254250, 305100, 508500]
STATE_MFJ = [0, 15164, 35952, 56742, 78768, 99548, 508500, 610200, 1017000]

def medicareRollOverLevel(filingStatus):
    return 200000 if filingStatus == TaxFilingStatus.SINGLE else 250000

def fedTaxActive(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxActive(bracket, FEDERAL_BRACKETS, FED_SINGLE)
    return taxActive(bracket, FEDERAL_BRACKETS, FED_MFJ)

def fedTaxIncremental(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxIncremental(bracket, FEDERAL_BRACKETS, FED_SINGLE)
    return taxIncremental(bracket, FEDERAL_BRACKETS, FED_MFJ)

def fedTaxPrevBracketTotal(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxPrevBracketTotal(bracket, FEDERAL_BRACKETS, FED_SINGLE)
    return taxPrevBracketTotal(bracket, FEDERAL_BRACKETS, FED_MFJ)

def stateTaxActive(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxActive(bracket, STATE_BRACKETS, STATE_SINGLE)
    return taxActive(bracket, STATE_BRACKETS, STATE_MFJ)

def stateTaxIncremental(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxIncremental(bracket, STATE_BRACKETS, STATE_SINGLE)
    return taxIncremental(bracket, STATE_BRACKETS, STATE_MFJ)

def stateTaxPrevBracketTotal(bracket, filingStatus):
    if filingStatus == TaxFilingStatus.SINGLE:
        return taxPrevBracketTotal(bracket, STATE_BRACKETS, STATE_SINGLE)
    return taxPrevBracketTotal(bracket, STATE_BRACKETS, STATE_MFJ)

def taxActive(bracket, bracketsArray, incomeArray):
    bracketIdx = bracketsArray.index(bracket)
    return incomeArray[bracketIdx]

def taxIncremental(bracket, bracketsArray, incomeArray):
    if bracketsArray.index(bracket)+1 >= len(bracketsArray):
        raise Exception('Cannot calculate incremental tax for highest tax bracket.')
    nextBracket = bracketsArray[bracketsArray.index(bracket)+1]
    return bracket * (taxActive(nextBracket, bracketsArray, incomeArray)-taxActive(bracket, bracketsArray, incomeArray))

def taxPrevBracketTotal(bracket, bracketsArray, incomeArray):
    bracketIdx = bracketsArray.index(bracket)
    if bracketIdx == 0:
        raise Exception('Cannot calculate previous bracket tax total for lowest tax bracket.')
    if bracketIdx == 1:
        return taxIncremental(bracketsArray[0], bracketsArray, incomeArray)
    prevBracket = bracketsArray[bracketIdx-1]
    return taxIncremental(prevBracket, bracketsArray, incomeArray) + taxPrevBracketTotal(prevBracket, bracketsArray, incomeArray)







