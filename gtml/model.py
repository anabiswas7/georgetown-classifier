
import time
import random
import pickle

from string import punctuation
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from nltk.classify.util import accuracy
from nltk.classify import NaiveBayesClassifier, MaxentClassifier

def timeit(func):

    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        finit  = time.time()
        delta  = finit - start # In seconds

        return result, delta

    return wrapper

class Model(object):
    """
    Builds a classifier model, or loads it from a pickle
    """

    def __init__(self):
        pass

    def load(self, path):
        pass

    def save(self, path):
        pass

    def featurize(self, row):
        pass

    def featuresets(self, corpus):
        pass

    def train(self, training):
        pass

    def test(self, testing):
        pass

    def classify(self, name):
        pass

    def explain(self, name):
        pass
