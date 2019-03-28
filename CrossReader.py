import os, os.path
import math

from random import randint, seed

dir = './Data/'



def packet_generator(packet_count, dir):
    
    seed()
    #if os.path.isfile(name)
    image_list = [(dir + 'Ailleur/' + name) for name in os.listdir(dir + 'Ailleurs')]
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
    
    return name_packets, target_packets

#pcount = 10
#directory = './Data/'

#print(packet_generator(pcount,dir))
