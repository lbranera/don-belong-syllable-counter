import random

file = open("syllables.txt")
syllables = [line.strip() for line in file.readlines()]
file.close()

file = open("vocabulary.txt")
vocab = [line.strip() for line in file.readlines()]
file.close()

def get_sample(n):
    sample = random.sample(vocab, n)
    return sample

def get_doc(filename):
    file = open(filename)
    doc = [line.strip().split(" ") for line in file.readlines()]
    file.close()

    return doc