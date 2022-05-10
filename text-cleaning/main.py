import re
import nltk

nltk.download('words')

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
