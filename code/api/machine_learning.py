import pandas as pd
import matplotlib.pylab as plt
import sklearn
import keras

import datetime
import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def train_random_forest(X_train, y_train, type="classifier", param_grid=None):
    if type == "classifier":
        rf = RandomForestClassifier(random_state=7)
    else:
        rf = RandomForestRegressor(random_state=7)

    if param_grid != None:
        grid = GridSearchCV(rf, param_grid, n_jobs=-1).fit(X_train, y_train)

    return grid


def get_random_forest_model(data,labels,type="classifier"):
    param_grid={
        'max_features': np.unique(np.round(np.linspace(0.3, 0.99, 9), 1)),
        'n_estimators': np.arange(100, 1100, 100)
    }
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25, random_state=42)
    model = train_random_forest(X_train, y_train, type=type, param_grid=param_grid)
    return model

def get_random_forest_predict(model,X_test):
    return model.predict(X_test)