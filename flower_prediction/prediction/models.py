from django.db import models
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load the dataset
iris = load_iris()
x, y = iris.data, iris.target

# split the dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
# train a model

model = RandomForestClassifier(n_estimators=100)
model.fit(x_train, y_train)

# savee the model to disk
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)
