import numpy as np
from sklearn import datasets, svm

iris = datasets.load_iris()
# num_samples = len(iris.data)
# test_set_size = round(.1 * num_samples)
# print test_set_size

iris_X = iris.data
iris_y = iris.target

iris_X_train_class1 = iris_X[iris_y == 1][:-5, :2]
iris_X_train_class2 = iris_X[iris_y == 2][:-5, :2]
iris_X_train = np.concatenate((iris_X_train_class1, iris_X_train_class2), axis=0)

iris_y_train_class1 = iris_y[iris_y == 1][:-5]
iris_y_train_class2 = iris_y[iris_y == 2][:-5]
iris_y_train = np.concatenate((iris_y_train_class1, iris_y_train_class2), axis=0)

iris_X_test_class1 = iris_X[iris_y == 1][-5:, :2]
iris_X_test_class2 = iris_X[iris_y == 2][-5:, :2]
iris_X_test = np.concatenate((iris_X_test_class1, iris_X_test_class2), axis=0)

iris_y_train_class1 = iris_y[iris_y == 1][:-5]
iris_y_train_class2 = iris_y[iris_y == 2][:-5]
iris_y_train = np.concatenate((iris_y_train_class1, iris_y_train_class2), axis=0)

svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)



# print type(iris_y[iris_y == 0])
# print len(iris_y[iris_y == 0])
# print len(iris_y[iris_y == 1])
# print len(iris_y[iris_y == 2])
