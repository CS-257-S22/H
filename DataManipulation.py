import csv
import sys
import glob

# combinedFile = "./Data/Combined_Data.csv"
combinedFile = "./Tests/TestData.csv"

with open(combinedFile, 'w', encoding = "UTF-8", newline = '') as wFile:
    writer = csv.writer(wFile)
    # path = "./Data/nasdaq/csv/*.csv"
    path = "./Data/testfiles/*.csv"

    writer.writerow(['Date', 'Low', 'Open', 'Volume', 'High', 'Close' ,'Adjusted Close', 'Ticker Symbol'])
    print("Path file is called: " + path)
    for fileName in glob.glob(path):
        f = open(fileName, 'r', encoding = "UTF-8")
        with f as rFile:
            spamreader = csv.reader(rFile, delimiter=',')
            print("Reading file: " + fileName)
            next(spamreader)
            for item in spamreader:
                # trueFileName = fileName.split("testfiles")
                # print(trueFileName[1])
                truefileName = fileName[17:-4]
                input = item, truefileName
                writer.writerow(input)

