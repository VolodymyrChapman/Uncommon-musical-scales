# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:33:45 2019
@author: Volodymyr (Vlad) Chapman
Process overview:
    1) import CSV file with all combinations
    2) make each list entry a string to allow each note to be selected 
    individually
    3)use a for loop to generate a txt file for each string(separate scale)
    that can be read and played by sonic Pi
    4) import txt files into sonic Pi and record (somehow) to make midi files
    of each scale
    5) go on a world tour and receive a knighthood 
"""


# Import file with all combinations
import csv
with open('All combinations from A1 to A2 listed.csv', 'r') as combinations:
 reader = csv.reader(combinations)
 scales = list(reader)
 
 #convert to string from list - easier to process indiv. elements
string_scales = ';'.join(map(str, scales))

# print(string_scales.split(';')) # experimenting with splitting the list



