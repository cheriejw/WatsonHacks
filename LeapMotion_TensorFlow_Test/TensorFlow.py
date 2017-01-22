import tensorflow as tf

import numpy as np
import random
import pandas as pd

TRAINING = "leapMotionTrainingSet.csv"
TEST = "leapMotionTestSet.csv"

dataset = pd.read_csv("finalDataset.csv")
dataset['Direction'] = dataset['Direction'].astype('int')

dfLength = len(dataset)

trainingLength = int(0.8 * dfLength)
testLength = int(0.2 * dfLength)

trainingSetRandomRows = np.random.choice(dataset.index.values, trainingLength)
trainingData = dataset.iloc[trainingSetRandomRows]
trainingData.to_csv(TRAINING, index=False, header=False)

testSetRandomRows = np.random.choice(dataset.index.values, testLength)
testData = dataset.iloc[testSetRandomRows]
testData.to_csv(TEST, index=False, header=False)

trainingSet = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=TRAINING, target_dtype=np.int, features_dtype=np.float32
)

testSet = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename=TEST, target_dtype=np.int, features_dtype=np.float32
)

featureColumns = [tf.contrib.layers.real_valued_column("", dimension=13)]

classifier = tf.contrib.learn.DNNClassifier(
                n_classes=4,
                feature_columns=featureColumns,
                hidden_units=[20, 30, 20]
)

# Fit model
classifier.fit(
                x=trainingSet.data,
                y=trainingSet.target,
                batch_size=128,
                steps=2000)

# Evaluate accuracy
accuracyScore = classifier.evaluate(
                x=testSet.data,
                y=testSet.target)["accuracy"]


# Predict
predictions = classifier.predict(testSet.data)
print testSet.data
# print 'Predictions: ', list(predictions)
# print 'Accuracy: {0:f}'.format(accuracyScore)