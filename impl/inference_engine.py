#
# base class for inference engines, this should never be instantiated
#

class InferenceEngine():

    # startup variable setup
    def __init__(self):
        raise NotImplementedError("constructor not implemented")

    # build and return the inference engine
    #    also print statistics on building engine
    def buildEngine(self):
        raise NotImplementedError("build engine function not implemented")

    # create a feature vector from the data
    def featuresFromData(self, dl):
        raise NotImplementedError("features from Data not implemented")

    # infer a prediction from a data point
    def inferFromData(self, dl):
        raise NotImplementedError("infer from data function not implemented")

    # cleanup the model
    #    report final statistics on model performance
    def __del__(self):
        raise NotImplementedError("delete inference engine not implemented")
