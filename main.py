import fileReader as fr
import sentences2Voc as s2v
import sentences2VecList
import train
import test

trainingPath = "./data/train.txt"
sentences, classList = fr.read(trainingPath)
print('sentences', sentences)
print('classList', classList)

voc = s2v.convert(sentences)
print('voc', voc)
print('len(voc)', len(voc))

vecList = sentences2VecList.convert(sentences, voc)
print('vecList', vecList)

pWordArray, pClassArray = train.train(vecList, classList)
print('pWordArray', pWordArray)
print('pClassArray', pClassArray)

# testingVecList = [[1,0,0,0,0,0,0,0,0,0,0,0]]
# testedClassList, pResult = test.test(testingVecList, pWordArray, pClassArray)
# print('testedClassList', testedClassList)
# print('pResult', pResult)

testingPath = "./data/dev.txt"
testingSentences, testingClassList = fr.read(testingPath)
testingVecList = sentences2VecList.convert(testingSentences, voc)
testedClassList, pResult = test.test(testingVecList, pWordArray, pClassArray)
print('testedClassList', testedClassList)
print('pResult', pResult)

#calculate the accuracy
if len(testedClassList) != len(testingClassList):
    print('the lengths of the testing class list and the tested class list are not identical!')
accurateCount = 0
for classIndex in range(len(testingClassList)):
    if testedClassList[classIndex] == testingClassList[classIndex]:
        accurateCount+=1
accuracy = accurateCount/len(testingClassList)
print('accuracy',accuracy)
