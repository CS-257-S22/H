import csv
import sys
import glob
import path
# current directory
directory = path.Path(__file__).abspath()
# setting path to the directory with the feature
sys.path.append(directory.parent.parent)

def mergeFiles(combinedFile, ourPath):
    with open(combinedFile, 'w', encoding = "UTF-8", newline = '') as wFile:
        writer = csv.writer(wFile)

        writer.writerow(['Date', 'Day', 'Month', 'Year', 'Low', 'Open', 'Volume', 'High', 'Close' , 'Ticker Symbol'])
        print("Path folder is called: " + ourPath)
        for fileName in glob.glob(ourPath):
            f = open(fileName, 'r', encoding = "UTF-8")
            with f as rFile:
                spamreader = csv.reader(rFile, delimiter=',')
                print("Reading file: " + fileName)
                next(spamreader)
                for item in spamreader:
                    # trueFileName = fileName.split("testfiles")
                    # print(trueFileName[1])
                    truefileName = fileName[13:-4]
                    dates = item[0].split("-")
                    input = item[0], dates[2], dates[1], dates[0], item[3], item[1], item[5], item[2], item[4], truefileName
                    writer.writerow(input)
            f.close

def deleteColumn(oldfilepath, newfilepath):
    with open(newfilepath, 'w', encoding = "UTF-8", newline = '') as wFile:
        writer = csv.writer(wFile)
        print("Reading file: " + oldfilepath)
        print("Path to new file: " + newfilepath)

        # Adjust this and input line to choose which column to delete
        writer.writerow(['Date', 'Day', 'Month', 'Year', 'Low', 'Open', 'Volume', 'High', 'Close' , 'Ticker Symbol'])

        f = open(oldfilepath, 'r', encoding = "UTF-8")
        with f as rFile:
            spamreader = csv.reader(rFile, delimiter=',')
            next(spamreader)
            for item in spamreader:
                # Adjust this line to choose which column to delete
                input = item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[10]
                writer.writerow(input)
        f.close

        g = open("./Data/NewCombined.csv", 'r', encoding = "UTF-8")

        with g as gFile:
            newspamreader = csv.reader(gFile, delimiter =',')
            next(newspamreader)
            for item in newspamreader:
                writer.writerow(item)
        g.close



if __name__ == '__main__':
    # newfile = "./Data/NewCombined.csv"
    # filepath = "./MoreStocks/*.csv"

    # mergeFiles(newfile, filepath)

    deleteColumn("./Data/Polished/NO_NULL_nasdaq_2010_mid_separate_year_month_day.csv", "./Data/cleanedData.csv")
