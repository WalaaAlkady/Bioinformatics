# Importing the libraries

#data hunding libraries
import numpy as np
import pandas as pd

#feature selection libraries
from sklearn.feature_selection import SelectKBest, mutual_info_classif , f_classif

#training & testing libraries
from sklearn.model_selection import train_test_split , cross_val_score
#https://scikit-learn.org/stable/modules/cross_validation.html

#classifiers libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

#performance libraries
from sklearn.metrics import confusion_matrix

#preprocessing libraries (if more than two classes)
from sklearn.preprocessing import LabelEncoder , LabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

#...............................................................................

#Importing the dataset:

#accession and Location (CSV file)
dataset = pd.read_csv('D:\Iris.csv')
x = dataset.iloc[:,1:5].values #features
y = dataset.iloc[:,5].values #class label

dataset = pd.read_csv('D:\Cancer.csv')
x = dataset.iloc[:,1:10].values #features
y = dataset.iloc[:,10].values #class label

#...............................................................................

#Converting Label (Multiple classes):
BL = LabelBinarizer()
biny = BL.fit_transform(y)

y_label = LabelEncoder()
numy = y_label.fit_transform(y)

#...............................................................................

#Training & Testing:
#normal labels
X_train , X_test , Y_train , Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#numerical labels
Xn_train , Xn_test , Yn_train , Yn_test = train_test_split(x, numy, test_size=0.2, random_state=0)

#binary labels
Xb_train , Xb_test , Yb_train , Yb_test = train_test_split(x, biny, test_size=0.2, random_state=0)

#...............................................................................

#Feature Selection:

#Info Gain:
fs = SelectKBest(score_func= mutual_info_classif, k=4)

# ANOVA feature selection for numeric input and categorical output
fs = SelectKBest(score_func= f_classif, k=)

#apply feature selection
fs = fs.fit(X_train, Y_train)
X_train_fs = fs.transform(X_train)
X_test_fs = fs.transform(X_test)

#...............................................................................

#Classification

#Logistic Regression:
LR = OneVsRestClassifier(LogisticRegression(random_state=0)) #for binary label

LR = LogisticRegression(random_state=0)

#training & testing method
#muliple classes or binary
L = LR.fit(X_train,Y_train)
acc_lr = L.score(X_test, Y_test) *100

#binary classification
LR.fit(X_train,Y_train)
Pred = LR.predict(X_test)
cm_LR = confusion_matrix(Y_test,Pred)
TN, FP, FN, TP = cm_LR.ravel()

#Accuracy
acc_LR = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_LR = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_LR = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_LR = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(LR, x, y, cv=10)
acc_LR_cross = scores.mean() * 100

#...............................................................................

#KNN Classifier:
KNN = KNeighborsClassifier(n_neighbors=3,metric='minkowski',p=1)

#training & testing method
#muliple classes or binary
k = KNN.fit(X_train,Y_train)
acc_knn = k.score(X_test, Y_test) *100

#binary classification
KNN.fit(X_train,Y_train)
Pred = KNN.predict(X_test)
cm_KNN = confusion_matrix(Y_test,Pred) 

TN, FP, FN, TP = cm_KNN.ravel()

#Accuracy
acc_KNN = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_KNN = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_KNN = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_KNN = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(KNN, x, y, cv=10)
acc_KNN_cross = scores.mean() * 100

#...............................................................................

##SVM:
svm = SVC(kernel='poly',random_state=0)
"""
rbf 
linear 
sigmoid
polynomial
"""

#training & testing method
#muliple classes or binary
S = svm.fit(X_train,Y_train)
acc_svm = S.score(X_test, Y_test) *100

#binary classification
svm.fit(X_train,Y_train)
Pred = svm.predict(X_test)
cm_svm = confusion_matrix(Y_test,Pred) 
TN, FP, FN, TP = cm_svm.ravel()

#Accuracy
acc_SVM = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_SVM = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_SVM = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_SVM = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(svm, x, y, cv=10)
acc_SVM_cross = scores.mean() * 100

#...............................................................................

#NB:
NB = GaussianNB()

#training & testing method
#muliple classes or binary
N = NB.fit(X_train,Y_train)
acc_nb = N.score(X_test, Y_test) *100

#binary classification
NB.fit(X_train,Y_train)
Pred = NB.predict(X_test)
cm_NB = confusion_matrix(Y_test,Pred) 
TN, FP, FN, TP = cm_NB.ravel()

#Accuracy
acc_NB = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_NB = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_NB = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_NB = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(NB, x, y, cv=10)
acc_NB_cross = scores.mean() * 100

#...............................................................................

#DT:
DT = DecisionTreeClassifier(random_state=0,criterion="entropy")

#training & testing method
#muliple classes or binary
D = DT.fit(X_train,Y_train)
acc_dt = D.score(X_test, Y_test) *100

#binary classification
DT.fit(X_train,Y_train)
Pred = DT.predict(X_test)
cm_DT = confusion_matrix(Y_test,Pred) 
TN, FP, FN, TP = cm_DT.ravel()

#Accuracy
acc_DT = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_DT = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_DT = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_DT = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(DT, x, y, cv=10)
acc_DT_cross = scores.mean() * 100

#...............................................................................

#RF:
RF = RandomForestClassifier(n_estimators=20,random_state=0,criterion="entropy")

#training & testing method
#muliple classes or binary
rf = RF.fit(X_train,Y_train)
acc_rf = rf.score(X_test, Y_test) *100

#binary classification
RF.fit(X_train,Y_train)
Pred = RF.predict(X_test)
cm_RF = confusion_matrix(Y_test,Pred) 
TN, FP, FN, TP = cm_RF.ravel()

#Accuracy
acc_RF = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_RF = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_RF = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_RF = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(RF, x, y, cv=10)
acc_RF_cross = scores.mean() * 100

#...............................................................................

#ANN:
NN = MLPClassifier(solver='lbfgs', alpha=0.0001, hidden_layer_sizes=(5, 2), random_state=0)
"""
lbfgs
sgd
adam
"""
#training & testing method
#muliple classes or binary
nn = NN.fit(X_train,Y_train)
acc_nn = nn.score(X_test, Y_test) *100

#binary classification
NN.fit(X_train,Y_train)
Pred = NN.predict(X_test)
cm_NN = confusion_matrix(Y_test,Pred) 
TN, FP, FN, TP = cm_NN.ravel()

#Accuracy
acc_NN = (TP+TN)/(TP+TN+FP+FN) * 100
# Sensitivity, hit rate, recall, or true positive rate
Sens_NN = TP/(TP+FN) *100
# Specificity or true negative rate
Spec_NN = TN/(TN+FP) *100
# Precision or positive predictive value
Prec_NN = TP/(TP+FP) *100

#cross validation method:
scores = cross_val_score(NN, x, y, cv=10)
acc_NN_cross = scores.mean() * 100