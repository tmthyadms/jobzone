import joblib
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud,STOPWORDS
from collections import defaultdict
from nltk import ngrams
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import pickle
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import PCA
import warnings
import json

warnings.filterwarnings('ignore')


loaded_model = joblib.load(r'C:\Users\Timothy Adams\Development\jobzone\server\prediction\fraud.sav')
with open(r'C:\Users\Timothy Adams\Development\jobzone\server\prediction\tranforming_model.pkl', 'rb') as f:
    vectorizer, pca = pickle.load(f)

stop=set(stopwords.words("english"))

def fea(text):
    if text=="":
        return 0
    else:
        return 1

def code(string):
    return string.split(",")[0]

def clean(text):
    
    text=text.lower()
    obj=re.compile(r"<.*?>")                     #removing html tags
    text=obj.sub(r" ",text)
    obj=re.compile(r"https://\S+|http://\S+")    #removing url
    text=obj.sub(r" ",text)
    obj=re.compile(r"[^\w\s]")                   #removing punctuations
    text=obj.sub(r" ",text)
    obj=re.compile(r"\d{1,}")                    #removing digits
    text=obj.sub(r" ",text)
    obj=re.compile(r"_+")                        #removing underscore
    text=obj.sub(r" ",text)
    obj=re.compile(r"\s\w\s")                    #removing single character
    text=obj.sub(r" ",text)
    obj=re.compile(r"\s{2,}")                    #removing multiple spaces
    text=obj.sub(r" ",text)
   
    
    stemmer = SnowballStemmer("english")
    text=[stemmer.stem(word) for word in text.split() if word not in stop]
    
    return " ".join(text)

def generate(text,ngram):
    n_grams=ngrams(word_tokenize(text),ngram)
    grams=[" ".join(val) for val in n_grams]
    return grams

def clean_data(user_input):
    data = user_input.copy()
    data.dropna(axis=0)['location'].apply(lambda x: x.split(',')[0])
    text_data=data.select_dtypes(include="object")
    text_data.drop(["location","salaryRange"],axis=1,inplace=True)
    text_col=text_data.columns
    data[text_col]=data[text_col].replace(np.nan,"")
    data["text"]=""
    for col in text_data.columns:
        data["text"]=data["text"]+" "+data[col]
    for col in text_col:
        data[col]=data[col].apply(fea)
    
    data.drop(["salaryRange"],axis=1,inplace=True)
    if "job_id" in data:
        data.drop(["job_id"],axis=1,inplace=True)
    data.dropna(axis=0,inplace=True)
    data["text_len"]=data["text"].str.len()
    drop_col=['title','department', 'description', 'requirements',
        'benefits', 'employmentType', 'requiredExperience',
        'requiredEducation', 'industry', 'function']

    data.drop(drop_col,axis=1,inplace=True)
    data["country"]=data["location"].apply(code)
    data=data[data["country"]=="US"]
    data.drop(columns=["country","location"],axis=1,inplace=True)
    data.reset_index(drop=True,inplace=True)

    stop=set(stopwords.words("english"))
    data["text"]=data["text"].apply(clean)

    return data

def prediction_model(json_input):
    try:
        data = json.loads(json.dumps(json_input))
        data['salaryRange'] = str(data['salaryRange']['min']) +' - '+str(data['salaryRange']['max'])
        input_cleaned = clean_data(pd.DataFrame(data,index=[0]))
        X_test = vectorizer.transform(input_cleaned['text'])
        X_test_pca = pca.transform(X_test.toarray())
        y_pred = loaded_model.predict(X_test_pca)
        return y_pred.sum()
    except Exception as e:
        return 0
