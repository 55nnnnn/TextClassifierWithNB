import __sentences2WordsMatrix as s2w


def convert(sentences):
    wordsMatrix = s2w.convert(sentences)
    vocSet = set([])
    for words in wordsMatrix:
        vocSet = vocSet | set(words)

    # only keep words
    delSet = set([])
    for vocEle in vocSet:
        if vocEle.isalpha() == False:
            delSet.add(vocEle)
    for delEle in delSet:
        vocSet.remove(delEle)

    #remove top 30 words
    top30Words = __calMostFreq(vocSet, wordsMatrix)
    for word in top30Words:
        vocSet.remove(word[0])

    voc = list(vocSet)
    voc.sort()
    return voc


def __calMostFreq(voc, wordsMatrix):
    import operator
    freqDict = {}
    for vocEle in voc:
        freqDict[vocEle] = 0
        for wordsRow in wordsMatrix:
            freqDict[vocEle] += wordsRow.count(vocEle)
    sortedFreqDic = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)
    return  sortedFreqDic[:40]
