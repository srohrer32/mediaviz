#
# Scikit-learn implementation of the inference engine
#

from impl.inference_engine import InferenceEngine

from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction import DictVectorizer


class ScikitInfer(InferenceEngine):

    def __init__(self, data, labels):
        # save the data
        self.data = data
        self.labels = labels

        # turn into dictionarys to vectorize
        data_dicts = [dict(y.iteritems()) for x, y in self.data.iterrows()]
        self.vectorizer = DictVectorizer()
        self.data = self.vectorizer.fit_transform(data_dicts)


    def buildEngine(self):
        self.cluster = AgglomerativeClustering().fit_predict(self.data.toarray())

        print(self.cluster)
        print(self.cluster.get_params())


    def inferFromData(self, data):
        pass


    def __del__(self):
        pass
