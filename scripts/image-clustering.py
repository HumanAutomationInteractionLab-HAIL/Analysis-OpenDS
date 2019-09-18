# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:50:27 2019

@author: Zhentao Huang
"""

import time
import os
import shutil


#convert unix timestamp to real world time
def convert_format(path_A):
    A_list = os.listdir(path_A)
    for A_str in A_list:

        A_str_s = A_str[:-8]
        A_str_ms = A_str[-7:-4]

        time_unix = time.strptime(str(A_str_s), '%Y-%m-%d-%H-%M-%S')
        time_t = time.mktime(time_unix)
        #print(str(time_t))
        filename = str(int(time_t)) + A_str_ms
        os.rename(path_A + '/' + A_str, path_A + '/' + filename +'.jpg')

#sort files of different sections
def sort_files(path_A, path_B, a1_time, a2_time, a3_time, a4_time, a5_time, a6_time):

    for i in range(1,4):
        os.mkdir(path_B + '/a' + str(i))
    A_list = os.listdir(path_A)

    for A_str in A_list:
        A_str_front = A_str[:-4]
        if ((int(A_str_front) > int(a1_time)) & (int(A_str_front) <= int(a2_time))):
            shutil.move(path_A + '/' + A_str, path_B + '/'+ 'a1'+ '/' + A_str)
        elif ((int(A_str_front) > int(a3_time)) & (int(A_str_front) <= int(a4_time))):
            shutil.move(path_A + '/' + A_str, path_B + '/'+ 'a2' + '/' + A_str)
        elif ((int(A_str_front) > int(a5_time)) & (int(A_str_front) <= int(a6_time))):
            shutil.move(path_A + '/' + A_str, path_B + '/' + 'a3' + '/' + A_str)
        #shutil.move(path_A + '/' + A_str, path_B + '/' + A_str)

#read txt files and acquires a1-a4 times
def read_txt_files(path_C):
    try:
        file=open(path_C + '/' + 'section_1.txt',"r")
    except FileNotFoundError:
        print("file is not found")
    else:
        contents = file.readlines()[1:]
        list_time = []
        for content in contents:
            t = content.split(':')[0]
            list_time.append(t)
        a1_time = list_time[0]
        a2_time = list_time[-1]
        file.close()
        
    try:
        file=open(path_C + '/' + 'section_2.txt',"r")
    except FileNotFoundError:
        print("file is not found")
    else:
        contents = file.readlines()[1:]
        list_time = []
        for content in contents:
            t = content.split(':')[0]
            list_time.append(t)
        a3_time = list_time[0]
        a4_time = list_time[-1]
        file.close()

    try:
        file=open(path_C + '/' + 'section_3.txt',"r")
    except FileNotFoundError:
        print("file is not found")
    else:
        contents = file.readlines()[1:]
        list_time = []
        for content in contents:
            t = content.split(':')[0]
            list_time.append(t)
        a5_time = list_time[0]
        a6_time = list_time[-1]
        file.close()


    return a1_time, a2_time, a3_time, a4_time, a5_time, a6_time

def main():
    path_A = "E:/facecapture - copy/08-18-17-37-03" #path of images
    path_B = "E:/facecapture-sorted/p36-1/s4"    #path of sorted images
    path_C = "E:/Data/p36-1/s4" #path of section txt files
    #a1_time = "1549076560202"
    #a2_time = "1549076560300"
    #a3_time = "1549076560400"
    #a4_time = "1549076560404"


    a1_time, a2_time, a3_time, a4_time, a5_time, a6_time = read_txt_files(path_C)
    convert_format(path_A)
    sort_files(path_A,path_B,a1_time,a2_time,a3_time,a4_time,a5_time,a6_time)
    print(a1_time,a2_time,a3_time,a4_time,a5_time,a6_time)



main()