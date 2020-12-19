from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import re


def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)
    
def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()

def get_text_similarity(item_one, item_two):
    item_one = item_one.lower()
    item_two = item_two.lower()
    result = get_cosine_sim(*[item_one, item_two])
    sim = result.diagonal(offset=1).item()

    return round(sim, ndigits=2)