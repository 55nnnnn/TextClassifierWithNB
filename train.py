import numpy as np


def train(vecList, classList):
    n = len(vecList[0])  # feature count
    m = len(vecList)  # set count

    classSet = set(classList)
    pWordArray = np.ones((len(classSet), n))
    for c in classSet:
        for classIndex in range(m):
            if classList[classIndex] == c:
                pWordArray[c] += vecList[classIndex]

    for pIndex in range(len(pWordArray)):
        pWordArray[pIndex] /= sum(pWordArray[pIndex])
        pWordArray[pIndex] = np.log(pWordArray[pIndex])

    pClassArray = np.zeros(len(classSet))
    for c in classSet:
        for cc in classList:
            if cc == c:
                pClassArray[c] += 1
    pClassArray /= sum(pClassArray)

    return pWordArray, pClassArray
