import os, os.path
import math
import numpy as np
import Reader as re

from random import randint, seed
from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def packet_generator(packet_count, dir):
    
    seed()
    #if os.path.isfile(name)
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
    
    clf_packet = []
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
            train_targets = target[pline][:]
            test_packet = data[(pline + train_packet_size) % packet_count][:]
            test_targets = target[(pline + train_packet_size) % packet_count][:]
            
            index = 1
            
            while(index < train_packet_size):
                for data_img in data[(pline + index) % packet_count]:
                    train_packet.append(data_img)
                #train_packet.append(data[(pline + index) % packet_count])
                for target_img in target[(pline + index) % packet_count]:
                    train_targets.append(target_img)
                #train_targets.append(target[(pline + index) % packet_count])
                index += 1
            
            index += 1
            
            while(index < packet_count):
                for data_img in data[(pline + index) % packet_count]:
                    test_packet.append(data_img)
                # test_packet.append(data[(pline + index) % packet_count])
                for target_img in target[(pline + index) % packet_count]:
                    test_targets.append(target_img)
                # test_targets.append(target[(pline + index) % packet_count])
                index += 1
            
            train_packet = np.asarray(train_packet)
            train_targets = np.asarray(train_targets)
            test_packet = np.asarray(test_packet)
            test_targets = np.asarray(test_targets)
            
            clf_packet.append(clf.fit(train_packet, train_targets))
            
            test_result =  clf.predict(test_packet)
            clf_accuracy.append(accuracy_score(test_targets, test_result))

    return clf_packet, clf_accuracy
    

### outils de test

# pcount = 10
# directory = './Data/'

# data_name, targets = packet_generator(pcount,directory)
# data = re.getHistogrammeCross(data_name)
# clfs,accur = cross_Validation_train(data, targets, GaussianNB())
# print(accur)



### Proto
# def cross_train(data, target, classifier, ratio=0.2)
    
#     clf_packet = []

#     for pline in range(len(data)):
        
#         clf = classifier
#         clf_packet.append(clf.fit(data[p],target[p]))
