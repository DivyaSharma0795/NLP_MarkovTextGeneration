# This is a Python repository for my Markov Test Generation Project

This project implements a Markov chain-based text generation function, `finish_sentence()`, in Python, trained on Jane Austen's "Sense and Sensibility." 

```
finish_sentence(sentence, n, corpus, randomize=False)
```

This function employs n-grams to predict the next word in a given sentence, mimicking the author's style. It takes four arguments:

* **`sentence` (list):** The partial sentence to be completed.
* **`n` (int):** The n-gram length used for prediction (e.g., 2 for bigrams, 3 for trigrams).
* **`corpus` (list):** The tokenized source text ("Sense and Sensibility").
* **`randomize` (bool):** Flag to deterministically choose the most probable next word (False) or randomly sample from the n-gram probability distribution (True).

The function iterates through the following steps:

1. **Extract the n-gram context:** From the current sentence, extract the last n-1 words as the context.
2. **Predict next word:**
    * **Deterministic (False):** Identify the word with the highest probability following the given context in the n-gram model.
    * **Random (True):** Sample a word from the n-gram probability distribution for the given context.
3. **Append and check termination:** Add the predicted word to the sentence. Stop if a punctuation mark (. ? !) is encountered or the sentence reaches 10 tokens. Otherwise, repeat steps 1-3.

This implementation utilizes **stupid backoff:** if an exact n-gram is not found in the corpus, the model falls back to lower-order n-grams (bigrams if trigrams fail, unigrams if bigrams fail). Additionally, **no smoothing** is applied to avoid introducing artificial probabilities.

**Overall, this project showcases a Markov chain text generation algorithm with n-gram prediction, offering control over randomization and n-gram order. It provides a fun and technical tool for exploring Jane Austen's writing style and experimenting with text generation in Python.**

*Sample Input:* 'She was not'

*Sample Output:* 'She was not in the world.'





Files in this repository include:


## 1. Readme
  The `README.md` file is a markdown file that contains basic information about the repository, what files it contains, and how to consume them


## 2. Requirements
  The `requirements.txt` file has a list of packages to be installed for any required project. Currently, my requirements file contains some basic python packages.


## 3. Codes
  This folder contains all the code files used in this repository - the files named "Test_" will be used for testing and the remaining will define certain functions


## 4. Resources
  This folder contains any other files relevant to this project. Currently, I have added -
  -  `MTG.ipynb` - this file has the function
  -  `generate_cases.py` - this file generates test cases for the above function

## 5. CI/CD Automation Files


  ### 5(a). Makefile
  The `Makefile` contains instructions for installing packages (specified in `requirements.txt`), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term *'Check...'* ), and linting the code using pylint


  ### 5(b). Github Actions
  Github Actions uses the `main.yml` file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions


  ### 5(c). Devcontainer
  The `.devcontainer` folder mainly contains two files - 
    * `Dockerfile` defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues
    * `devcontainer.json` is a json file that specifies the environment variables including the installed extensions in the virtual environment
