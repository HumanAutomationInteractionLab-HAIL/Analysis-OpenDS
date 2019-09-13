#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:50:27 2019

@author: weikaikong & zhentaohuang
"""
import math
import matplotlib.pyplot as plt
import numpy as np



def checksection_4lane(list_x,list_z,list_t):

    if (len(list_x) != len(list_z)): 
        return -1

    sections = [0,0,0,0,0,0]    #starts and ends points

    #section 1: traffic light
    for i in range(len(list_z)):
        if (list_z[i] >= 184.0):            #start from z < 184.0
            sections[1] = i
            break
        elif (i == len(list_z) - 1):        #if not find find the point
            sections[1] = -1

    turn_left = True    #is True if it turns left at the first corner
    #section 2: overtaking
    for i in range(sections[1],len(list_z)):
        if (list_z[i] >= 226.478): #go straight
            sections[2] = i
            turn_left = False
            
            for j in range(sections[2],len(list_z)):
                if (list_z[j] >= 958.492):
                    sections[3] = j
                    break
                elif (j == len(list_z) - 1): #if not find find the point
                    sections[3] = -1
                    print('1')
            
            break
        elif (list_x[i] > 15.679):          #turn left at first corner
            sections[2] = i

            for j in range(sections[2],len(list_z)):
                if (list_x[j] >= 751.653):
                    sections[3] = j
                    break
                elif (j == len(list_z) - 1): #if not find find the point
                    sections[3] = -1
            break        

    #section 3: following
    if (turn_left): #turn left at the first corner
        for i in range(sections[3],len(list_z)):
            if (list_z[i] >= 226.478): 
                sections[4] = i
                for j in range(sections[4],len(list_z)):
                    if (list_z[j] >= 958.492):
                        sections[5] = j
                        break
                    elif (j == len(list_z) - 1): #if not find find the point
                        sections[5] = j
                    
                break
            elif (i == len(list_z) - 1): 
                sections[4] = -1
            
    else:   #go straight at the first corner
        for i in range(sections[3],len(list_z)):
            if (list_x[i] >= 15.679):
                sections[4] = i
                for j in range(sections[4],len(list_z)):
                    if(list_x[j] >= 751.653):
                        sections[5] = j
                        break
                    elif (j == len(list_z) - 1):
                        sections[5] = j
                break
            elif (i == len(list_z) - 1): 
                sections[4] = -1                #if not find find the point
                    
    return sections


def checksection_8lane(list_x,list_z,list_t):

    if (len(list_x) != len(list_z)): 
        return -1

    sections = [0,0,0,0,0,0] #starts and ends points

    #section 1: traffic light
    for i in range(len(list_z)):
        if (list_z[i] >= 179.43): #start from z < 184.0
            sections[1] = i
            break
        elif (i == len(list_z) - 1):            #if not find find the point
            sections[1] = -1

    turn_left = True                            #is True if it turns left at the first corner
    #section 2: overtaking
    for i in range(sections[1],len(list_z)):
        if (list_z[i] >= 234.998): #go straight
            sections[2] = i
            turn_left = False
            
            for j in range(sections[2],len(list_z)):
                if (list_z[j] >= 1272.637):
                    sections[3] = j
                    break
                elif (j == len(list_z) - 1): 
                    sections[3] = -1
                
            break
        elif (list_x[i] >= 27.94):  #turn left at first corner
            sections[2] = i

            for j in range(sections[2],len(list_z)):
                if (list_x[j] >= 1064.941):
                    sections[3] = j
                    break
                elif (j == len(list_z) - 1): 
                    sections[3] = -1
            break
    #section 3: following
    if (turn_left): #turn left at the first corner
        for i in range(sections[3],len(list_z)):
            if (list_z[i] >= 234.998): 
                sections[4] = i
                for j in range(sections[4],len(list_z)):
                    if (list_z[j] >= 1272.637):
                        sections[5] = j
                        break
                    elif (j == len(list_z) - 1): 
                        sections[5] = j
                break
            elif (i == len(list_z) - 1): 
                sections[5] = -1

    else:   #go straight at the first corner
        for i in range(sections[3],len(list_z)):
            if (list_x[i] >= 27.94):
                sections[4] = i
                for j in range(sections[4],len(list_z)):
                    if(list_x[j] >= 1064.941):
                        sections[5] = j
                        break
                    elif (j == len(list_z) - 1):
                        sections[5] = j
                break
            elif (i == len(list_z) - 1): 
                sections[5] = -1
                   
    return sections


def plot_map_4lane(list_x,list_z,sections):
    
    if (len(list_x) != len(list_z)):
        return -1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlim=[-800,1700],ylim=[-250,1200])
    plt.scatter(list_z,list_x,marker='.',lineWidth = 0.0001,edgecolor='none')
    ax.plot(list_z,list_x,label='Movement Track')
    ax.plot(np.linspace(184,184,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(226.478,226.478,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(1000.96, 1000.96, 1000), np.linspace(-250, 1200, 1000), color='g')
    ax.plot(np.linspace(958.492,958.492,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(-800,1700,1000),np.linspace(15.679,15.679,1000),color='g')
    ax.plot(np.linspace(-800, 1700, 1000), np.linspace(-26.899, -26.899, 1000), color='g')
    ax.plot(np.linspace(-800, 1700, 1000), np.linspace(794.131, 794.131, 1000), color='g')
    ax.plot(np.linspace(-800,1700,1000),np.linspace(751.653,751.653,1000),color='g')
    plt.title('OpenDS Scene Planform and Movement Track of Vehicle--4 lanes')
    plt.legend()
    plt.show()
            

def plot_map_8lane(list_x,list_z,sections):
    
    if (len(list_x) != len(list_z)): 
        return -1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(xlim=[-800,1700],ylim=[-250,1200])
    plt.scatter(list_z,list_x,marker='.',lineWidth = 0.0001,edgecolor='none')
    ax.plot(list_z,list_x,label='Movement Track')
    ax.plot(np.linspace(179.3,179.3,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(234.998,234.998,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(1272.637,1272.637,1000),np.linspace(-250,1200,1000),color='g')
    ax.plot(np.linspace(1328.205, 1328.205, 1000), np.linspace(-250, 1200, 1000), color='g')
    ax.plot(np.linspace(-800,1700,1000),np.linspace(27.94,27.94,1000),color='g')
    ax.plot(np.linspace(-800, 1700, 1000), np.linspace(-27.628, -27.628, 1000), color='g')
    ax.plot(np.linspace(-800,1700,1000),np.linspace(1064.941,1064.941,1000),color='g')
    ax.plot(np.linspace(-800, 1700, 1000), np.linspace(1120.509, 1120.509, 1000), color='g')
    plt.title('OpenDS Scene Planform and Movement Track of Vehicle--8 lanes')
    plt.legend()
    plt.show()   


def read_data():
    try:
        file=open('C:\\Users\\q4349\\Desktop\\827\\analyzerData\\analyzerData\\p2\\2019_08_12-12_20_14\\carData_track1.txt',"r")
    except FileNotFoundError:         
        print("file is not found")
    else:
        line=file.readline()
        print(line)
        for everyChar in line:
            if (everyChar == '4'):
                lane = 4
                break
            else:
                lane = 8
                
        contents=file.readlines()[4:]      
        print("find Car Data!")
        list_x = [] 
        list_z = []
        list_v = [] #list of speed (km/h)
        list_t = [] #list of time (ms)
        list_distance_ahead = [] #distance ahead(meters)
        for content in contents:
            t = content.split(':')[0]
            x = content.split(':')[1]
            z = content.split(':')[3]
            v = content.split(':')[8]
            distance_ahead = content.split(':')[13]
            list_t.append(int(t))
            list_x.append(float(x))
            list_z.append(float(z))
            list_v.append(float(v))
            list_distance_ahead.append(float(distance_ahead))
        file.close

        return list_x,list_z,list_v,list_t,list_distance_ahead,lane


def save_data(list_x,list_z,list_v,list_t,list_distance_ahead,sections,lane):
    
     
    list_s = [0] #list of distance (meters)
    list_a = [0] #list of acceleration (m/s^2)

    for i in  range(len(list_x) - 1):
        x1 = list_x[i]
        x2 = list_x[i + 1]
        z1 = list_z[i]
        z2 = list_z[i + 1]
        v1 = list_v[i] / 3.6      #convert to m/s
        v2 = list_v[i + 1] /3.6
        t1 = list_t[i] / 100      #convert to seconds
        t2 = list_t[i + 1] / 100  
        s = math.sqrt((x1-x2)*(x1-x2) + (z1-z2)*(z1-z2)) + list_s[i]
        a = abs(v2 - v1) / (t2 - t1)
        list_s.append(s)    #store the distance (m) to list_s
        list_a.append(a)    #store the acceleration (m/s^2) to list_a
    
    with open('section_1.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('Time (ms):Distance (meters): Speed (km/h) : Acceleration (m/s^2): Distance Ahead (meters) \n')
        for i in range(sections[1]):
            month_file.write(str(list_t[i]))
            month_file.write(':')
            month_file.write(str(list_s[i]))
            month_file.write(':')
            month_file.write(str(list_v[i]))
            month_file.write(':')
            month_file.write(str(list_a[i]))
            month_file.write(':')
            month_file.write(str(list_distance_ahead[i]))
            month_file.write('\n')

    with open('position_1.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('%d %s Position(x,z) \n' %(lane,'lane'))
        for i in range(sections[1]):
            month_file.write(str(list_x[i]))
            month_file.write(':')
            month_file.write(str(list_z[i]))
            month_file.write('\n')

    with open('section_2.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('Time (ms): Distance (meters): Speed (km/h) : Acceleration (m/s^2): Distance Ahead (meters) \n')
        for i in range(sections[2],sections[3]):
            month_file.write(str(list_t[i]))
            month_file.write(':')
            month_file.write(str(list_s[i]))
            month_file.write(':')
            month_file.write(str(list_v[i]))
            month_file.write(':')
            month_file.write(str(list_a[i]))
            month_file.write(':')
            month_file.write(str(list_distance_ahead[i]))
            month_file.write('\n')

    with open('position_2.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('%d %s Position(x,z) \n' %(lane,'lane'))
        for i in range(sections[2],sections[3]):
            month_file.write(str(list_x[i]))
            month_file.write(':')
            month_file.write(str(list_z[i]))
            month_file.write('\n')
        

    with open('section_3.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('Time (ms): Distance (meters): Speed (km/h) : Acceleration (m/s^2): Distance Ahead (meters) \n')
        for i in range(sections[4],sections[5]):
            month_file.write(str(list_t[i]))
            month_file.write(':')
            month_file.write(str(list_s[i]))
            month_file.write(':')
            month_file.write(str(list_v[i]))
            month_file.write(':')
            month_file.write(str(list_a[i]))
            month_file.write(':')
            month_file.write(str(list_distance_ahead[i]))
            month_file.write('\n')

    with open('position_3.txt', 'a') as month_file: #store the data into "positions.txt"
        month_file.write('%d %s Position(x,z) \n' %(lane,'lane'))
        for i in range(sections[4],sections[5]):
            month_file.write(str(list_x[i]))
            month_file.write(':')
            month_file.write(str(list_z[i]))
            month_file.write('\n')
        
    return 0

def main():
    list_x,list_z,list_v,list_t,list_distance_ahead,lane = read_data()
    
    
    if (lane == 4):
        sections = checksection_4lane(list_x,list_z,list_t)
        plot_map_4lane(list_x,list_z,sections)
    else:
        sections = checksection_8lane(list_x,list_z,list_t)
        plot_map_8lane(list_x,list_z,sections)
    print(sections)
    save_data(list_x,list_z,list_v,list_t,list_distance_ahead,sections,lane)


main()
