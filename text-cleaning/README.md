### Text Cleaning

Text cleaning is the process of preparing raw text for NLP (Natural Language Processing) so that machines can understand human language. In NLP text cleaning is done to remove unwanted text that causes noise for example, numbers, punctuations, links, etc.

1. first you need to import necessary package and download `words` using `nltk`

```py
import re
import nltk

nltk.download('words')
```

2. We define a function that deconctracts words such as `I'm` to `I am`

```py
def decontracted(phrase:str)->str:
    """
    Args:
        phrase (str): takes in a word like I'm

    Returns:
        string: a decontracted word like I am
    """
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

```

3. The the following function is the function that clean the text for us:

```py
def clean_sentence(sent:str)->str:
    """
    Args:
        sent (str): an uncleaned sentence with text, punctuations, numbers and non-english words
    Returns:
        str: returns a cleaned sentence with only english words in it.
    """
    sent = re.sub(r'https?\S+', ' ', sent, flags=re.MULTILINE) # removing url's
    sent = re.sub(r'\d', ' ', sent) # removing none word characters
    sent = re.sub(r'[^\w\s\']', ' ', sent) # removing punctuations except for "'" in words like I'm
    sent = re.sub(r'\s+', ' ', sent).strip() # remove more than one space
    words = list()
    eng = set(nltk.corpus.words.words())
    for word in sent.split(' '):
        words.append(decontracted(word)) # replace word's like "i'm -> i am"
    return " ".join(w for w in words if w.lower() in eng or not w.isalpha()) # removing non-english words

```

### Usage:

```
clean_sentence("text 1 # https://url.com/bla1/blah1/")
```

Output:

```shell
'text'
```

### Ref

1. [stackoverflow.com](https://stackoverflow.com/questions/41290028/removing-non-english-words-from-text-using-python)
2. [stackoverflow.com](https://stackoverflow.com/questions/43018030/replace-apostrophe-short-words-in-python)
