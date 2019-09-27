#
# Scikit-learn implementation of the inference engine
#

from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction import DictVectorizer

from impl.inference_engine import InferenceEngine


class ScikitInfer(InferenceEngine):

    # create SKL object out of it
    def __vectorize(self):
        # turn into dictionaries to vectorized
        data_dicts = [dict(y.iteritems()) for x, y in self.data.iterrows()]

        self.vectorizer = DictVectorizer()
        self.data = self.vectorizer.fit_transform(data_dicts)
        print(self.vectorizer.get_feature_names())

    def __init__(self, data, labels):
        # save the data
        self.data = data
        self.labels = labels

    def buildEngine(self):
        self.cluster = AgglomerativeClustering()
        self.cluster = self.cluster.fit_predict(self.data.toarray())

        print(self.cluster.get_params())

    def inferFromData(self, data):
        return data

    def __del__(self):
        pass
