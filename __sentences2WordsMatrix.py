import re
def convert(sentences):
    wordsMatrix = []
    for sentence in sentences:
        words =[word.lower() for word in re.split(r'\W+', sentence) if len(word)>0]
        wordsMatrix.append(words)

    return wordsMatrix