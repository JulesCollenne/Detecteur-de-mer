import os, os.path
from os import listdir
import math
import numpy as np

import Reader as re         #Util pour les tests internes

from random import randint, seed
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import GaussianNB


def packet_generator(packet_count, dir):
    
    seed()
    
    image_list = [(dir + 'Ailleurs/' + name) for name in os.listdir(dir + 'Ailleurs')]
    target_list = [-1 for t1 in range(len(image_list))]
    
    temporary_list = [(dir + 'Mer/' + name) for name in os.listdir(dir + 'Mer')]
    temp_target_list = [1 for t2 in range(len(image_list))]
    
    image_list += temporary_list
    target_list += temp_target_list
    
    line_count = packet_count
    
    name_packets = [[] for k in range(line_count)]
    target_packets = [[] for t3 in range(line_count)]

    i = 0
    
    while(not(not(image_list))):
        
        random_image_index = randint(0,len(image_list)-1)
    
        name_packets[i%line_count].append(image_list[random_image_index])
        target_packets[i%line_count].append(target_list[random_image_index])
        
        del image_list[random_image_index]
        del target_list[random_image_index]

        i += 1
        
    # for tline in range(len(target_packets)):
    #     target_packets[tline] = np.asarray(target_packets[tline])

    return name_packets, target_packets

    
def cross_Validation_train(data, target, classifier, ratio=0.2):
    
    clf_list = []
    clf_accuracy = []
    packet_count = len(data)
    
    if(packet_count < 2):
        print("Nombre insuffisant de packet")
    elif(ratio < 0 or ratio >=1):
        print("Le ratio doit être compris dans l'intervale [0,1[")
    else:
        test_packet_size = math.ceil(ratio * packet_count)
        train_packet_size = packet_count - test_packet_size

        for pline in range(len(data)):
            
            clf = classifier
            
            train_packet = data[pline][:]                                       #python c'est comme les mercredi matins: C'est bien de la merde! Hein Michel?!
            train_target = target[pline][:]
            test_packet = data[(pline + train_packet_size) % packet_count][:]
            test_target = target[(pline + train_packet_size) % packet_count][:]
            
            index = 1
            
            while(index < train_packet_size):
                for data_img in data[(pline + index) % packet_count]:
                    train_packet.append(data_img)
  
                for target_img in target[(pline + index) % packet_count]:
                    train_target.append(target_img)

                index += 1
            
            index += 1
            
            while(index < packet_count):
                for data_img in data[(pline + index) % packet_count]:
                    test_packet.append(data_img)
 
                for target_img in target[(pline + index) % packet_count]:
                    test_target.append(target_img)

                index += 1
            
            train_packet = np.asarray(train_packet)
            train_target = np.asarray(train_target)
            test_packet = np.asarray(test_packet)
            test_target = np.asarray(test_target)
            
            clf_list.append(clf.fit(train_packet, train_target))
            
            test_result =  clf.predict(test_packet)
            clf_accuracy.append(accuracy_score(test_target, test_result))

    return clf_list, clf_accuracy
    
def cross_predict(clf_list, data):
    
    predicts = [[] for data_img in data]

    for img_index in range(len(data)):
        for clf_index in range(len(clf_list)):
            predicts[clf_index].append(clf_list[clf_index].predict([data[img_index]]))

    return predicts


def cross_boosting(predict_matrix, safety=0.5, clf_coef=-1):
    
    final_predicts = []
    
    if(clf_coef == -1 and predict_matrix[0]):
        clf_coef = [1 for clf_predicts in predict_matrix[0]]
    print("nb d'image : ", len(predict_matrix))
    print("clf_coef : " , clf_coef)
    
    total_coef = 0
    for coef in clf_coef:
        total_coef += coef
    
    print("total_coef : ", total_coef)
    
    for img_predicts in predict_matrix:
        predict_sum = 0 
        
        for clf_index in range(len(img_predicts)):
            predict_sum += img_predicts[clf_index] * clf_coef[clf_index]
        
        if((predict_sum / total_coef) >= safety):
            final_predicts.append(1)
        
        else:
            final_predicts.append(0)
    
    return final_predicts

def namelist_generator(dirpath):
    data_name = []

    for  file in listdir(dirpath):
        name = "" + dirpath + "/" + file
        data_name.append(name)

    # data_name = np.asarray(data_name)

    return data_name

### outils de test

# pcount = 10
# directory = './Data/'

# data_name, targets = packet_generator(pcount,directory)
# data = re.getHistogrammeCross(data_name)
# clfs,accur = cross_Validation_train(data, targets, GaussianNB())

# data_name_test = namelist_generator("./DataTest")
# data_test = re.getHistogramme(data_name_test)

# predicts = cross_predict(clfs, data_test)
# final_predits = cross_boosting(predicts)

# print(data_name_test)
# print(final_predits)



### Proto
# def cross_train(data, target, classifier, ratio=0.2)
    
#     clf_packet = []

#     for pline in range(len(data)):
        
#         clf = classifier
#         clf_packet.append(clf.fit(data[p],target[p]))
