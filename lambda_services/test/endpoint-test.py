
import dataiku
from dataiku.apinode.predict.predictor import ClassificationPredictor
import pandas as pd
 
import os
from sklearn.externals import joblib
 
class MyPredictor(ClassificationPredictor):
    """The class for a classification Custom API node predictor"""
 
    def __init__(self, data_folder = None):
        """data_folder is the absolute path to the managed folder storing the data for the model
        (if any)"""
        self.data_folder = dataiku.Folder("test2")
 
    def predict(self, features_df):
 
        #get the location of the managed folder
       # handle = dataiku.Folder("model_web",project_key="PremeraListens")
        path = handle.get_path()
        #load the pickled objects
        vect = joblib.load(os.path.join(path,'model_web.p'))
        clf = joblib.load(os.path.join(path,'vect.p'))
        #score the data
        X = vect.transform(features_df['Comment'])
        predictions = clf.predict(X)
 
        return (predictions)