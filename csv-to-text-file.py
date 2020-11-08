# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:57:12 2020

Converts a csv file to a text file and a text file to a csv file

@author: AAYUSH MISHRA
"""

import csv

# Taking the input of the csv file
name = input('Enter the name of the csv file with extension: ')

# Checking if the file is a csv or txt file
if name[-4:] == '.txt':
    FileName = name[:-4] + '.csv'

    # Reading the text file
    try: 
        textFile = open(name, 'r')

        # Read lines from text file
        totalLines = textFile.readlines()

        # Creating/Opening csv file
        with open(FileName, 'w') as csvfile:

            csv_writer = csv.writer(csvfile)

            for line in totalLines:
                # Write in csv file
                csv_writer.writerow(line.split())
            
        #Close csv file
        csvfile.close()
        
        # Close the text file
        textFile.close()

    except:
        print('Could not open ' + name + ' file')
        exit() 

    print(FileName + ' generated')     

elif name[-4:] == '.csv':
    FileName = name[:-4] + '.txt'

    # Reading the csv file
    try: 
        with open(name, 'r') as csvfile:

            # Creating a csv reader object 
            csvreader = csv.reader(csvfile) 

            # Creating/Opening text file
            textFile = open(FileName, 'w')

            # Adding csv data to text file 
            for row in csvreader:
                for data in row:
                    textFile.write(data + '\t')
                textFile.write('\n')
            
            # Closing the text file
            textFile.close()

        # Closing the csv file
        csvfile.close()

    except:
        print('Could not open ' + name + ' file')
        exit()

    print(FileName + ' generated')

else:
    print('Invalid file type entered')
