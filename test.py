import numpy as np


def test(vecList, pWords, pC):
    pResult = np.zeros((len(vecList), len(pC)))
    for rowIndex in range(len(vecList)):
        for colIndex in range(len(pC)):
            pResult[rowIndex][colIndex] = sum(vecList[rowIndex] * pWords[colIndex]) + np.log(pC[colIndex])

    testedClassList = np.zeros(len(vecList))
    for rowIndex in range(len(pResult)):
        testedClassList[rowIndex] = findIndexOfMax(pResult[rowIndex])

    return testedClassList, pResult


def findIndexOfMax(array):
    for i in range(len(array)):
        if array[i] == np.max(array):
            return i
    return -1
