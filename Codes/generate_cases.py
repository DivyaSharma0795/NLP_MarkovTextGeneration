import nltk
from mtg import finish_sentence
import shutil

corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())


sentence = [["she", "was", "not"], ["she", "was", "Divya"], ["the", "sensible"]]
n = [1, 2, 3, 4]
randomize = [False, True]

count = 0
with open("./Resources/output.txt", "w") as f:
    for i in sentence:
        for j in n:
            for k in randomize:
                count += 1
                output = finish_sentence(i, j, corpus, k)
                print(output)
                f.write("Test Case : " + " " + str(count) + "\n")
                f.write("Input Sentence :" + " " + str(i) + "\n")
                f.write("Value of n :" + " " + str(j) + "\n")
                f.write("Randomize:" + " " + str(k) + "\n")
                f.write("Output :" + " " + str(output) + "\n")
                f.write("-------------------------------------------------------------")
                f.write("\n")
                f.write("\n")


shutil.copyfile(
    "./Resources/output.txt", "./Resources/IDS703_NLP_Assignment1_TestCases.md"
)
