
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from Algorithm import Model as model
from sklearn.model_selection import GridSearchCV
def ada_boostSobel(X_train, X_test, y_train, y_test):
    clf = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None, learning_rate=1,
          n_estimators=100, random_state=None)
    clf.fit(X_train, y_train)
    model.save_Model('AdaBoostSobel.sav',clf)
    y_predict = clf.predict(X_test)

    #return accuracy_score(y_test, y_predict)
    return y_predict


def ada_boostHistogramme(X_train, X_test, y_train, y_test):
    clf = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=0.1, n_estimators=30, random_state=None)
    clf.fit(X_train, y_train)
    model.save_Model('AdaBoostHisto.sav',clf)
    y_predict = clf.predict(X_test)

    #return accuracy_score(y_test, y_predict)
    return y_predict

def ada_boostImgvec(X_train, X_test, y_train, y_test):
    clf = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1, n_estimators=100, random_state=None)
    clf.fit(X_train, y_train)
    model.save_Model('AdaBoostImgvec.sav',clf)
    y_predict = clf.predict(X_test)

    #return accuracy_score(y_test, y_predict)
    return y_predict

def ada_boostParam(data,target):
    parameters= {'n_estimators':[1,10,20,30,40,50,100],'learning_rate':[0.1,1,2]}
    clf = AdaBoostClassifier()
    clff=GridSearchCV(clf,parameters,cv=5,verbose=10)
    print("start")
    clff.fit(data, target)
    print("end")
    print(clff)
    print(clff.best_score_)
    print(clff.best_estimator_)

'''
algorithm='SAMME.R', base_estimator=None,
          learning_rate=0.1, n_estimators=30, random_state=None
'''
