## Background
Air quality classification
The Paris Agreement is an international treaty on climate change that was adopted by 196 Parties at COP21 in Paris. Its goal is to limit global warming to well below 2, preferably 1.5 degrees Celsius, compared to pre-industrial levels.
To reach this long-term temperature goal, countries aim to peak greenhouse gas emissions as soon as possible to achieve a climate-neutral planet by mid-century.
That is why the European Union is allocating large amounts of resources to the development of new technologies that allow the improvement of the fight against pollution. One of these is a new type of sensor based on laser technology that allows air quality to be detected based on different sensors.


## Problem
The objective is to carry out a predictive model that allows to know the type of air quality based on the measurements of the sensors.
0 corresponds to Good air quality
1 corresponds to Moderate air quality
2 corresponds to Dangerous air quality
We face a multiclass classification problem.


## Analysis
We have 8 features, all numerical, corresponding to the parameters measured by the different sensors. The training dataset has 2100 records and the test dataset 900. The distribution between the 3 labels is balanced: 33% of the records for each label. The features are standardized. 


## Solution
I have trained a ramdom forest model. To do so, I have reserved 25% of the train dataset to measure the model performance.


## Results
The result for the final f1_score for the ramdom forest model is 89%.
The model is used to predict the label for the test dataset. The result is in the csv-file predictions.csv and the json-file predictions.json


## License
To resolve the problem, i used the technical package:

*pycharm
python
pandas
scikit-learn
matplotlib
seaborn*
