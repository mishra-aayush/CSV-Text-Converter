import csv

# Taking the input of the csv file
name = input('Enter the name of the csv file with extension: ')

# Naming text file
textFileName = name[:-4] + '.txt'

# Reading the csv file
try: 
    with open(name, 'r') as csvfile:

        # Creating a csv reader object 
        csvreader = csv.reader(csvfile) 

        # Creating/Opening text file
        textFile = open(textFileName, 'w')

        # Adding csv data to text file 
        for row in csvreader:
            for data in row:
                textFile.write(data + '\t\t\t')
            textFile.write('\n')
        textFile.close()

    # Closing the csv file
    csvfile.close()

except:
    print('Could not open ' + name + ' file')
    exit()

print(textFileName + ' generated')