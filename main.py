from sklearn import linear_model

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

import csv
import numpy as np
# from sklearn.linear_model import LinearRegression
x = []
y = []
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    header = None
    for row in spamreader:
        if header is None:
            header = row
        else :
            # print(' '.join(row))
            data = []
            for i in range(len(header)):
                if header[i] in 'Time' or header[i] in 'signal':
                    pass
                elif header[i] in 'price':
                    y.append(float(row[i]))
                else :
                    data.append(float(row[i]))
            x.append(data)

names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    # SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

s = 20
x_train = x[:]
x_test = x[:]
y_train = y[:]
y_test = y[:]
x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# 1. Set up the model
Ridge = linear_model.Ridge (alpha = .5)
Lasso= linear_model.Lasso(alpha = 0.1)
# # 2. Use fit
Ridge.fit(x_train, y_train)
Lasso.fit(x_train, y_train)

a = Ridge.predict(x_test)
arr = []
for i in a.tolist():
    arr.append([i])
print(arr)
# # 3. Check the score
# print(Ridge.score(x_test, y_test))
# print(Lasso.score(x_test, y_test))

# import matplotlib.pyplot as plt
# plt.plot(range(len(y_test)), y_test, range(len(y_test)), Lasso.predict(x_test), linewidth=2.0)
# plt.show()
# plt.plot(y_test, Lasso.predict(x_test), y_test), linewidth=2.0)


# import matplotlib.pyplot as plt

# for name, clf in zip(names, classifiers):
#     print(name)
#     clf.fit(x_train, y_train)
#     score = clf.score(x_test, y_test)
#     print(score)

#     plt.plot(range(len(y_test)), y_test, range(len(y_test)), clf.predict(x_test), linewidth=2.0)
#     plt.show()
