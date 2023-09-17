# Importing Packages
import nltk
import numpy as np
from typing import Optional, List

# Getting the required text files
# nltk.download("gutenberg")
# nltk.download("punkt")


# Reading the text file and tokenising it using nltk
def test_generator():
    """Test Markov text generator."""
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
    print(corpus)
    return corpus


# Splitting the list of tokens from the corpus into groups of n - returns list of tuples as a dictionary
def n_split(corpus_list, n):
    counter = 0
    corpus_dict = {}
    # text = ""
    for word in corpus_list:
        text = ()
        if counter > n:
            for i in reversed(range(n)):
                text += tuple([corpus_list[counter - i - 1]])
            # print(text)
            if text not in corpus_dict:
                corpus_dict[text] = 1
            else:
                corpus_dict[text] += 1
            pass
        counter += 1
    return corpus_dict


#   Function to create sub-dictionary with n-1 matching words - returns dictionary with counts
def get_sub_dictionary(sentence, corpus_dictionary, n):
    #   Code to get first n - 1 elements of the list
    sent = ()
    for i in range(n - 1):
        sent += tuple([sentence[i]])
    new_dict = {}
    #   Code to subset the corpus dictionary based on n-1 elements
    for s in corpus_dictionary:
        if s[: n - 1] == sent:
            new_dict[s] = corpus_dictionary[s]
    return new_dict
