import numpy as np
import math
from sklearn import datasets, neighbors, linear_model 

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

np.random.seed(0)
indices = np.random.permutation(len(X_digits))

num_samples = len(digits.data)
test_set_size = math.floor(.1 * num_samples)
print "number of samples: ", num_samples
print "test_set_size: " ,test_set_size

digits_X_train = X_digits[indices[:-test_set_size]]
digits_y_train = y_digits[indices[:-test_set_size]]
digits_X_test = X_digits[indices[-test_set_size:]]
digits_y_test = y_digits[indices[-test_set_size:]]

knn = neighbors.KNeighborsClassifier()
knn.fit(digits_X_train, digits_y_train)
print "KNN score: "
print knn.score(digits_X_test, digits_y_test)

logistic = linear_model.LogisticRegression(C=1e5)
logistic.fit(digits_X_train, digits_y_train)
print "Logistic Regression score: "
print logistic.score(digits_X_test, digits_y_test)


# """
# ================================
# Digits Classification Exercise
# ================================

# A tutorial exercise regarding the use of classification techniques on
# the Digits dataset.

# This exercise is used in the :ref:`clf_tut` part of the
# :ref:`supervised_learning_tut` section of the
# :ref:`stat_learn_tut_index`.
# """
# print(__doc__)

# from sklearn import datasets, neighbors, linear_model

# digits = datasets.load_digits()
# X_digits = digits.data
# y_digits = digits.target

# n_samples = len(X_digits)

# X_train = X_digits[:.9 * n_samples]
# y_train = y_digits[:.9 * n_samples]
# X_test = X_digits[.9 * n_samples:]
# y_test = y_digits[.9 * n_samples:]

# knn = neighbors.KNeighborsClassifier()
# logistic = linear_model.LogisticRegression()

# print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
# print('LogisticRegression score: %f'
#       % logistic.fit(X_train, y_train).score(X_test, y_test))