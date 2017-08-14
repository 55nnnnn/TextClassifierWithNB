def read(path):
    sentences = []

    # sentences=['0 Good! That is excellent!',
    #            '1 This product is very bad ']
    #classList = [0, 1]

    # sentences = ['a b',
    #              'c d',
    #              'e f',
    #              'g h',
    #              'i j',
    #              'k l']
    # classList = [0, 1, 2, 0, 1, 2]


    file = open(path)
    lines = [line for line in file.readlines()]
    sentences = [line[1:] for line in lines]
    classList = [int(line[0]) for line in lines]

    return sentences, classList
