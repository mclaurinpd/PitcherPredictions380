'This method is a brute-force method that checks the data for each pitcher within'
'one Standard Deviation of the Hall of Fame, then tries to predict if the pitcher is HOF worthy'

import csv
import sys
import os
import numpy
import time

'''
Authors: Brenton Belanger, David Matrisciano II, and Phillip McLaurin
'''


class Pitcher:
    Name = ""
    WHIP = 0.0
    ERAminus = 0.0
    FIPminus = 0.0

    def __init__(self, name, whip, ERAminus, FIPminus):
        self.Name = name
        self.WHIP = whip
        self.ERAminus = ERAminus
        self.FIPminus = FIPminus

    def __str__(self):
        print('Name: ', self.Name)
        print('WHIP: ', self.WHIP)
        print('ERA-: ', self.ERAminus)
        print('FIP-: ', self.FIPminus)


def loadData(file, list):
    with open(file, 'r') as file:
        for line in file:
            tokens = line.split(',')
            name = tokens[0]
            whip = float(tokens[1])
            era = float(tokens[2])
            fip = float(tokens[3])
            pitcher = Pitcher(name, whip, era, fip)
            list.append(pitcher)


def hofData(dataset, std, mean):
    whipList = []
    fipList = []
    eraList = []

    'O(N) for N players in HOF'
    for Pitcher in dataset:
        whipList.append(Pitcher.WHIP)
        fipList.append(Pitcher.FIPminus)
        eraList.append(Pitcher.ERAminus)

    whipSTD = numpy.std(whipList)
    whipMean = numpy.mean(whipList)
    fipSTD = numpy.std(fipList)
    fipMean = numpy.mean(fipList)
    eraSTD = numpy.std(eraList)
    eraMean = numpy.mean(eraList)
    std.extend([whipSTD, fipSTD, eraSTD])
    mean.extend([whipMean, fipMean, eraMean])

def hofQualify(hofSTD, hofMean, allPitchers, hofResults):
    'Used 1/4 std deviation for top of the elite players'
    for Pitcher in allPitchers:
        if Pitcher.WHIP >= hofMean[0] - hofSTD[0] and Pitcher.WHIP <= hofMean[0] + hofSTD[0]:
            if Pitcher.FIPminus >= hofMean[1]-hofSTD[1] and Pitcher.FIPminus <= hofMean[1] + hofSTD [1]:
                if Pitcher.ERAminus >= hofMean[2]- hofSTD[2] and Pitcher.ERAminus <= hofMean[2] + hofSTD[2]:
                    hofResults.append(Pitcher.Name)


def main():
    file1 = os.getcwd() + "/HOFSet.txt"
    file2 = os.getcwd() + "/1000Pitchers.txt"
    file3 = os.getcwd() + "/10000Pitchers.txt"
    file4 = os.getcwd() + "/100000Pitchers.txt"
    file5 = os.getcwd() + "/MillionPitchers.txt"
    file6 = os.getcwd() + "/AllPitcherSet.txt"
    hofPitchers = []
    thousandPitchers = []
    tenthouPitchers = []
    hunthouPitchers = []
    millionPitchers = []
    AllPitchers = []
    newHof = []
    loadData(file1, hofPitchers)
    loadData(file2, thousandPitchers)
    loadData(file3, tenthouPitchers)
    loadData(file4, hunthouPitchers)
    loadData(file5, millionPitchers)
    loadData(file6, AllPitchers)
    hofSTD = []
    hofMean = []
    hofData(hofPitchers, hofSTD, hofMean)
    startTime = time.time()
    hofQualify(hofSTD, hofMean, AllPitchers, newHof)
    endTime = time.time()
    print("Time for All Real Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    for i in newHof:
        print(i)
    newHof = []
    startTime = time.time()
    hofQualify(hofSTD, hofMean, thousandPitchers, newHof)
    endTime = time.time()
    print("Time for 1000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    for i in newHof:
        print(i)
    newHof = []
    startTime = time.time()
    hofQualify(hofSTD, hofMean, tenthouPitchers, newHof)
    endTime = time.time()
    print("Time for 10000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    for i in newHof:
        print(i)
    newHof = []
    startTime = time.time()
    hofQualify(hofSTD, hofMean, hunthouPitchers, newHof)
    endTime = time.time()
    print("Time for 100000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    for i in newHof:
        print(i)
    newHof = []
    startTime = time.time()
    hofQualify(hofSTD, hofMean, millionPitchers, newHof)
    endTime = time.time()
    print("Time for 1 Million Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    for i in newHof:
        print(i)

main()