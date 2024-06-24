import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

def summarize(text):

    from definitions import remove_sw, sentence_vector, sentence_rank

    sentences = sent_tokenize(text)

    tokens_without_sw = remove_sw(text)
    vocabulary = sorted(tokens_without_sw)
    if len(vocabulary) == 0:
        return 'Enter full larger text'
    sens_vec = sentence_vector(sentences,vocabulary)

    m = np.transpose(np.array(sens_vec))
    dis = 1-pairwise_distances(m, metric="cosine") 
    sum_cs = list(sum(dis))
    similarity = dict(zip(vocabulary, sum_cs))

    rank = sentence_rank(sentences, similarity)

    l = sorted(rank, key=rank.get, reverse = True)


    leng = []
    for sen in l:
        leng.append(len(sen.split()))

    # we can change max number of words allowed. For now, it is 80
    n = 60

    if n < max(leng):
        n = max(leng)


    summary = ''

    if len(text.split()) <= n:
        summary = text
    else:
        w=0
        u=len(l[0].split())
        while u <= n:
            summary += " " + l[w]
            if w < len(l)-1:
                w += 1
                u += len(l[w].split())
            else:
                return summary

    return summary