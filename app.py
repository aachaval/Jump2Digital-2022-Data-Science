import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,f1_score,classification_report


aire = pd.read_csv('train.csv', header=0, sep=';')

x = aire.drop(['target'], axis='columns')
y = pd.DataFrame(aire.target)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=7)  # 75%-25% proportion

#instantiate RandomForestClassifier()
model = RandomForestClassifier(random_state=7)

#fit the classification
model.fit(x_train, np.ravel(y_train))

#Predict on test
y_pred = model.predict(x_test)

print(classification_report(y_test,y_pred))
print(round(f1_score(y_test, y_pred, average='macro'),2))

aire_predict = pd.read_csv('test.csv', header=0, sep=';')
aire_predict_pred = model.predict(aire_predict)

pd.DataFrame(aire_predict_pred, columns=['predicted']).to_json("predictions.json", orient='columns')
pd.DataFrame(aire_predict_pred, columns=['predicted']).to_csv("predictions.csv", index=False)