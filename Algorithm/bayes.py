from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score






from Algorithm import Model as model



def Bayes(data, target):
    data_train, data_test, target_train, target_test = train_test_split(data, target, train_size=0.8, test_size=0.2)
    #train
    clf = GaussianNB()
    clf.fit(data_train, target_train)
    model.save_Model('Bayes.sav',clf)
    #predict
    predictions = clf.predict(data_test)
    print(predictions)
    i = 0
    #for  prediction, target in zip( predictions, target):
       # i += 1
        #if prediction != target:
           #print(i, 'has been classified as ', prediction, 'and should be ', target)
        
    #score
    return (accuracy_score(predictions, target_test))

