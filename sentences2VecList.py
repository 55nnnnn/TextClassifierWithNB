import numpy as np
import __sentences2WordsMatrix as s2w

def convert(sentences, voc):
    wordsMatrix = s2w.convert(sentences)
    vecList = []

    for words in wordsMatrix:
        wordsVec = __words2Vec(words, voc)
        vecList.append(wordsVec)

    return vecList




def __words2Vec(words, voc):
    vec = np.zeros(len(voc))
    for word in words:
        if word in voc:
            vec[voc.index(word)] = 1
    return vec
