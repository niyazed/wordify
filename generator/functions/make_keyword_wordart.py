import nltk
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
class generate:
    def __init__(self, text):
            self.text = text
    def clean(self):
        text = self.text.lower()
        printable = set(string.printable)
        text = filter(lambda x: x in printable, text) #filter funny characters, if any.
        self.text = "".join(text)
    def process_text(self):
        self.clean()
        Cleaned_text = self.text
        text = word_tokenize(Cleaned_text)
        POS_tag = nltk.pos_tag(text)
        wordnet_lemmatizer = WordNetLemmatizer()
        adjective_tags = ['JJ','JJR','JJS']
        lemmatized_text = []

        for word in POS_tag:
            if word[1] in adjective_tags:
                lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
            else:
                lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0]))) #default POS = noun
                
        # print ("Text tokens after lemmatization of adjectives and nouns: \n")
        #  print (lemmatized_text)

        POS_tag = nltk.pos_tag(lemmatized_text)


        stopwords = []
        wanted_POS = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBG','FW'] 

        for word in POS_tag:
            if word[1] not in wanted_POS:
                stopwords.append(word[0])

        punctuations = list(str(string.punctuation))
        stopwords = stopwords + punctuations


        # stopword_file = open("long_stopwords.txt", "r")   edit maybe
        #Source = https://www.ranks.nl/stopwords
        stopword_file = set(STOPWORDS)

        lots_of_stopwords = []

        for line in stopword_file:
            lots_of_stopwords.append(str(line.strip()))

        stopwords_plus = []
        stopwords_plus = stopwords + lots_of_stopwords
        stopwords_plus = set(stopwords_plus) #Stopwords_plus contain total set of all stopwords


        processed_text = []
        for word in lemmatized_text:
            if word not in stopwords_plus:
                processed_text.append(word)
        self.text = processed_text     
    def generate_keyword(self):
        self.process_text()
        words = self.text #read the words into a list.
        uniqWords = sorted(set(words)) #remove duplicate words and sort
        dict={}
        for word in uniqWords:
            #print(words.count(word), word)
            dict[word]=words.count(word)
        sd = sorted(dict.items(), key=lambda kv: kv[1])
        sd.reverse()
        return sd


    def generate_wordart(self):
        words = self.text #read the words into a list.
        dict ={}
        for word in words:
            dict[word]=0
        for word in words:
            dict[word]=dict[word]+1
        sorted_x = sorted(dict.items(), key=lambda kv: kv[1])
        sorted_x.reverse()
        l = []
        max_kw = 10
        for i in range(0,max_kw):
            l.append(sorted_x[i][0])

        dictionary={}
        for x in sorted_x:
            dictionary[x[0]]=x[1]
            
        wordcloud = WordCloud(font_path='kalpurush.ttf',min_font_size = 10, background_color="white").generate_from_frequencies(dictionary)
        wordcloud.to_file('cloud.png')
