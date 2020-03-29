import boto3
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import json

def cleaning_data(data, symbols = False):
    data = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', '', data) # Remove email
    data = data.replace('\r', '').replace('\n', ' ').replace('  ', ' ')
    data = re.sub(r'Budget: .* Title: ', '', data) # Remove "Budget" 
    data = re.sub(r' Time limit: .*', '', data) # and "Time limit"
    data = re.sub(r'  +', ' ', data) # Remove extra space

    if symbols == False:
        data = re.sub(r"[^a-zA-ZÀ-ÿ]", " ", data.lower()) # Remove symbols and convert to lower case

    return data


def lead_note_to_words(note):
    # nltk.download("stopwords", quiet=True) # We already added the nltk_data folder manually
    stemmer = PorterStemmer()

    data = cleaning_data(note) # Clean the text
    words = data.split() # Split string into words

    words = [w for w in words if w not in stopwords.words('french')] # Remove stopwords
    words = [PorterStemmer().stem(w) for w in words] # stem

    return words


def bow_encoding(words, vocabulary):
    bow = [0] * len(vocabulary) # Start by setting the count for each word in the vocabulary to zero.
    for word in words.split():  # For each word in the string
        if word in vocabulary:  # If the word is one that occurs in the vocabulary, increase its count.
            bow[vocabulary[word]] += 1
    return bow


def lambda_handler(event, context):

    vocab = {'création': 9, 'site': 33, 'web': 36, 'actuel': 0, 'bonjour': 4,
    'chez': 6, 'plu': 28, 'import': 18, 'lign': 23, 'besoin': 3, 'être': 39,
    'sou': 34, 'gestion': 15, 'tout': 35, 'migrat': 25, 'internet': 20,
    'afin': 1, 'fair': 13, 'lien': 22, 'serveur': 31, 'infomaniak': 19,
    'wordpress': 37, 'page': 27, 'pouvoir': 29, 'merci': 24, 'mise': 26,
    'jour': 21, 'base': 2, 'doit': 10, 'fichier': 14, 'si': 32,
    'hébergement': 17, 'domain': 11, 'recherch': 30, 'donné': 12, 'contenu': 8,
    'www': 38, 'ch': 5, 'com': 7, 'http': 16}

    words = lead_note_to_words(event['body'])
    words = ' '.join([str(elem) for elem in words]) 
    bow = bow_encoding(words, vocab)

    # The SageMaker runtime is what allows us to invoke the endpoint that we've created.
    runtime = boto3.Session().client('sagemaker-runtime')

    # Now we use the SageMaker runtime to invoke our endpoint, sending the review we were given
    response = runtime.invoke_endpoint(EndpointName = 'sagemaker-xgboost-2020-03-29-03-10-59-734',
                                       # The name of the endpoint we created
                                       ContentType = 'text/csv',
                                       Body = ','.join([str(val) for val in bow]).encode('utf-8'))

    # The response is an HTTP response whose body contains the result of our inference
    result = response['Body'].read().decode('utf-8')

    return {
        'statusCode' : 200,
        'headers' : { 'Content-Type' : 'text/plain', 'Access-Control-Allow-Origin' : '*' },
        'body' : str(result)
    }