from codecs import ascii_decode
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
import textract
import string
import nltk
import re

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('omw-1.4')



def extract_text(file):
    """
    It takes a file and returns the text in that file
    
    :param file: The path to the file you want to extract text from
    :return: A string of the text in the file.
    """
    text = textract.process(file)
    
    return text.decode()


def clean_text(text):
    """
    It takes a string as input, and returns a string with all the non-alphanumeric characters removed,
    and all the words converted to lowercase
    
    :param text: The text to be cleaned
    :return: cleaned text
    """
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    
    printable = set(string.printable)
    text = filter(lambda x: x in printable, text) #filter funny characters, if any.
    text = "".join(text)

    return text


def process_text(text):
    """
    It takes in a string of text, tokenizes it, tags it with POS tags, removes stopwords, punctuation,
    and words that are not nouns, adjectives, or verbs, and returns a list of the remaining words
    
    :param text: The text that you want to process
    :return: A list of words that are not stopwords or punctuation.
    """
    text = nltk.word_tokenize(text)
    POS_tags = nltk.pos_tag(text)
    stopwords = []
    wanted_POS = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBG','FW'] 

    for word in POS_tags:
        if word[1] not in wanted_POS:
            stopwords.append(word[0])

    punctuations = list(str(string.punctuation))
    stopwords = stopwords + punctuations
    stopword_file = set(STOPWORDS)

    lots_of_stopwords = []
    for line in stopword_file:
        lots_of_stopwords.append(str(line.strip()))

    # stopwords_plus contain total set of all stopwords
    stopwords_plus = []
    stopwords_plus = stopwords + lots_of_stopwords
    stopwords_plus = set(stopwords_plus)


    processed_text = []
    for word in POS_tags:
        if word not in stopwords_plus:
            processed_text.append(word[0])
    
    
    return processed_text

