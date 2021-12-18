import pandas as pd
from nltk.corpus import stopwords
from textblob import Word

def text_preprocessing(request):
    text = request.POST['info']
    stop = stopwords.words('english')
    data = {'Text': []}
    data['Text'].append(text)
    df = pd.DataFrame(data)
    df['Text'] = df['Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    df['Text'] = df['Text'].str.replace('[^\w\s]', '')
    df['Text'] = df['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    df['Text'] = df['Text'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    return "The Function has Executed"

def easy_function(request):
    return request.POST['info']