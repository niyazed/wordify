from wordcloud import WordCloud


def _keywords(words):
    """
    It takes a list of words, finds the unique words, counts the number of times each word appears,
    sorts the words by the number of times they appear, and returns the sorted wordlist and top 10 words
    
    :param words: a list of words
    :return: sorted wordlist and top 10 keywords
    """
    unique_words = sorted(set(words))

    dict={}
    for word in unique_words:
        # print(words.count(word), word)
        dict[word]=words.count(word)
    sorted_wordlist = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_wordlist.reverse()

    ten_kw = []
    max_kw = 10
    for i in range(0,max_kw):
        ten_kw.append(sorted_wordlist[i][0])

    return sorted_wordlist, ten_kw


def _wordart(words):
    """
    It takes a list of words as input, and returns a wordart object
    
    :param words: list of words
    :return: A wordart object
    """
    dict ={}
    for word in words:
        dict[word[0]]=0

    for word in words:
        dict[word[0]]=dict[word[0]]+1

    sorted_x = sorted(dict.items(), key=lambda kv: kv[1])
    sorted_x.reverse()

    word_dict={}
    for x in sorted_x:
        word_dict[x[0]]=x[1]
        
    wordart = WordCloud(font_path='kalpurush.ttf',min_font_size = 10, scale = 2.5, background_color="white").generate_from_frequencies(word_dict)

    return wordart