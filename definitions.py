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

# from PIL import Image
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def remove_sw(text):
    text1 = text.lower()
    text1 = re.sub('[^a-zA-Z]', ' ' , text1)
    text_tokens = word_tokenize(text1)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    
    for word in tokens_without_sw:
        if word in text.lower():
            continue
        else:
            tokens_without_sw.remove(word)

    return tokens_without_sw

def sentence_vector(sentences,vocabulary):
    sens_vec = []
    for s in sentences:
        s = re.sub('[^a-zA-Z]', ' ' , s)
        sen_vec = []
        for word in vocabulary:
            if word in s.lower():
                sp = s.lower().split()
                r = sp.count(word)
                sen_vec.append(r)
            else:
                sen_vec.append(0)
        sens_vec.append(sen_vec)
    return sens_vec

def sentence_rank(sentences_list, freq_dict):
    rank = {}
    for s in sentences_list:
        for word, fre in freq_dict.items():
            if word in s.lower():
                if s in rank:
                    rank[s] += fre
                else:
                    rank[s] = fre
    return rank

def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element(by=By.XPATH, value = xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_tagname(tagname, driver):
    try:
        driver.find_element(by=By.TAG_NAME, value = tagname)
    except NoSuchElementException:
        return False
    return True
