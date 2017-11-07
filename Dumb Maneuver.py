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
        if (Pitcher.WHIP) > hofMean[0] - hofSTD[0]/4 and Pitcher.WHIP < hofMean[0] + hofSTD[0]/4:
            if Pitcher.FIPminus > hofMean[1]-hofSTD[1]/4 and Pitcher.FIPminus < hofMean[1] + hofSTD [1]/4:
                if Pitcher.ERAminus > hofMean[2]- hofSTD[2]/4 and Pitcher.ERAminus + hofSTD[2]/4:
                    hofResults.append(Pitcher.Name)


def main():
    file = os.getcwd() + "\\HOFSet.txt"
    file2 = os.getcwd() + "\\AllPitcherSet.txt"
    hofPitchers = []
    allPitchers = []
    newHof = []
    loadData(file, hofPitchers)
    loadData(file2, allPitchers)
    hofSTD = []
    hofMean = []
    startTime = time.time()
    hofData(allPitchers, hofSTD, hofMean)
    hofQualify(hofSTD, hofMean, allPitchers, newHof)
    endTime = time.time()
    print(len(allPitchers))
    print(len(newHof))
    print("Your new Hall of Fame pitchers are:")
    print("\n".join(newHof))
    print("And it only took " + "\t{0:.6f}\tseconds".format(endTime - startTime))


main()
