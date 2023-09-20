"""Markov Text Generator.

Patrick Wang, 2023

Resources:
Jelinek 1985 "Markov Source Modeling of Text Generation"
"""

import nltk
import random
from mtg import finish_sentence
import shutil

random.seed(7649)


def test_generator():
    """Test Markov text generator."""
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())

    sentence = [["she", "was", "not"], ["she", "was", "Divya"], ["the", "sensible"]]
    n = [1, 2, 3, 4]
    randomize = [False, True]
    count = 0
    with open("output.txt", "w") as f:
        for i in sentence:
            for j in n:
                for k in randomize:
                    count += 1
                    # print(i, j, k)
                    output = finish_sentence(i, j, corpus, k)
                    # print(output)
                    f.write("Test Case #" + str(count) + "\n")
                    f.write("N = " + str(j) + "\n")
                    f.write("Randomize Flag: " + " " + str(k) + "\n")
                    f.write("Input Sentence: " + str(i) + "\n")
                    f.write("Output Sentence: " + " " + str(output) + "\n")
                    f.write("==================================================")
                    f.write("\n")
                    f.write("\n")
    shutil.copyfile("output.txt", "output.md")

    words = finish_sentence(
        ["she", "was", "Divya"],
        4,
        corpus,
        randomize=False,
    )
    print(words)
    # assert words == [
    #     "she",
    #     "was",
    #     "not",
    #     "in",
    #     "the",
    #     "world",
    #     ".",
    # ] or words == [
    #     "she",
    #     "was",
    #     "not",
    #     "in",
    #     "the",
    #     "world",
    #     ",",
    #     "and",
    #     "the",
    #     "two",
    # ]


if __name__ == "__main__":
    test_generator()
