# Importing Packages
import numpy as np
import random


# Splitting the list of tokens from the corpus into groups of n - returns list of tuples as a dictionary
def n_split(corpus_list, n):
    counter = 0
    corpus_dict = {}
    for word in corpus_list:
        text = ()
        if counter > n:
            for i in reversed(range(n)):
                text += tuple([corpus_list[counter - i - 1]])
            if text not in corpus_dict:
                corpus_dict[text] = 1
            else:
                corpus_dict[text] += 1
            pass
        counter += 1
    return corpus_dict


#   Function to create sub-dictionary with n-1 matching words
def get_sub_dictionary(sentence, corpus_dictionary, n):
    #   Code to get first n - 1 elements of the list
    sent = ()
    for i in reversed(range(1, n)):
        sent += tuple([sentence[n - i - 1]])
    #   Code to subset the corpus dictionary based on n-1 elements
    new_dict = {}
    for s in corpus_dictionary:
        if s[: n - 1] == sent:
            new_dict[s] = corpus_dictionary[s]
    return new_dict


# Creating test sentence
def get_test_sent(sentence, n):
    test_sent = ()
    l = len(sentence)
    if l - n + 1 < 0:
        return get_test_sent(sentence, l + 1)
    if n == 1:
        return sentence[-1]
    for i in reversed(range(0, n - 1)):
        test_sent += tuple([sentence[l - i - 1]])
    return test_sent


#   Getting the most likely token based on the dictionary counts
def get_most_common(new_dict, randomise):
    if new_dict == {}:
        return None
    if randomise == False:
        highest_token = max(new_dict, key=new_dict.get)
        # print(highest_token)
    else:
        # m = max(new_dict.values())
        td = {}
        for i in new_dict:
            # if new_dict[i] == m:
            if new_dict[i] > 0:
                td[i] = new_dict[i]
        # print(m, td)
        highest_token = random.choice(list(td.keys()))
    return highest_token


def finish_sentence(sentence, n, corpus, randomize=False):
    if n == 0:
        n = 1
    output_sentence = sentence
    test_sent = sentence
    l = len(sentence)
    while l < 10:
        n1 = min(n, len(test_sent) + 1)
        test_sentence = get_test_sent(test_sent, n1)
        sub_dictionary = get_sub_dictionary(test_sentence, n_split(corpus, n1), n1)
        if sub_dictionary == {}:
            n2 = n1
        while sub_dictionary == {}:
            n2 -= 1
            test_sentence = get_test_sent(test_sent, n2)
            # print("inside", n2, test_sentence)
            sub_dictionary = get_sub_dictionary(test_sentence, n_split(corpus, n2), n2)

        most_common_occurrence = get_most_common(sub_dictionary, randomize)
        # print(test_sentence, "->", most_common_occurrence)
        output_sentence.append(most_common_occurrence[-1])
        l += 1
        if most_common_occurrence[-1] in [".", "!", "?"]:
            break
        test_sent = output_sentence[-n1:]
    return output_sentence
