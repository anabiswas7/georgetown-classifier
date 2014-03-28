
import unicodecsv as csv
from nltk import wordpunct_tokenize

class CorpusReader(object):
    """
    Normally would extend nltk.corpus.reader.api.CorpusReader but that
    seems like a bit much for now- on other corpora you might do this.

    In this case, the job of this class to yield text, label pairs for
    the annotated corpus - which hopefully won't be too tough to do!
    """

    def __init__(self, path):
        pass

    def rows(self, categories=None):
        """
        Does the work of reading the CSV file for each row.
        """
        pass

    def categories(self):
        """
        Finds the categories in the CSV file.
        """
        pass

    def words(self, categories=None):
        """
        Iterates through all the words in the corpus
        """
        pass

    def vocab(self, categories=None):
        """
        returns the vocabulary, the set of unique words
        """
        pass

    def count(self, categories=None):
        """
        Returns the word count of the corpus
        """
        pass

    def metrics(self, categories=None):
        """
        Returns statistics about the corpus like word count, vocab count,
        lexical diversity for the given categories requested.
        """
        pass

    def pprint(self, categories=None):
        """
        Pretty prints the metrics of the corpus
        """
        pass
