from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

corpus = ['All ','this ']
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).todense()
print( vectorizer.vocabulary_ )
for f in features:
    print( euclidean_distances(features[0], f) )
