from sklearn.metrics import accuracy_score
from sklearn import svm
from Algorithm import Model as model
from sklearn.model_selection import GridSearchCV

def svmModelSobel(X_train, X_test, y_train, y_test):
    clf = svm.SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
    clf.fit(X_train, y_train)
    model.save_Model('svmSobel.sav',clf)
    y_predict = clf.predict(X_test)
    return y_predict

def svmModelImgvec(X_train, X_test, y_train, y_test):
    clf = svm.SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
    clf.fit(X_train, y_train)
    model.save_Model('svmImgvec.sav',clf)
    y_predict = clf.predict(X_test)
    return y_predict

def svmModelParam(data,target):
    parameters= {'kernel':('linear','rbf','poly'),'C':[1,2,3,4,5,6,7,8,9,10]}
    clf = svm.SVC(gamma='scale')
    clff=GridSearchCV(clf,parameters,cv=5,verbose=10)
    print("start")
    clff.fit(data, target)
    print("end")
    print(clff)
    print(clff.best_score_)
    print(clff.best_estimator_)
    #model.save_Model('svm.sav',clf)

    #return accuracy_score(y_test, y_predict)
def svmModelHistogramme(X_train, X_test, y_train, y_test):
    clf = svm.SVC(C=7, cache_size=200, class_weight=None, coef0=0.0,
                  decision_function_shape='ovr', degree=3, gamma='scale', kernel='linear',
                  max_iter=-1, probability=False, random_state=None, shrinking=True,
                  tol=0.001, verbose=False)
    clf.fit(X_train, y_train)
    model.save_Model('svmHisto.sav',clf)
    y_predict = clf.predict(X_test)
    return y_predict
'''
SVC(C=7, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='scale', kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
'''
