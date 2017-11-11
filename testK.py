import os
import math
import numpy
import time

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


def Data(hof, med, all):
    hofList = []
    medList = []
    testList = []

    'O(N) for N players in HOF'
    for Pitcher in hof:
        hofList.append([Pitcher.Name,Pitcher.WHIP,Pitcher.ERAminus,Pitcher.FIpminus])
    for Pitcher in med:
        medList.append([Pitcher.Name,Pitcher.WHIP,Pitcher.ERAminus,Pitcher.FIpminus])
    for Pitcher in all:
        testList.append([Pitcher.Name,Pitcher.WHIP,Pitcher.ERAminus,Pitcher.FIpminus])
    return hofList,medList,testList

def nearestNeighbor(hof,med,test):
    distancesHOF = []
    distancesMED = []
    for i in hof:
        distance = getDistance(i.WHIP,i.ERAminus,i.FIPminus,test.WHIP,test.ERAminus,test.FIPminus)
        distancesHOF.append(distance)
    for i in med:
        distance = getDistance(i.WHIP, i.ERAminus, i.FIPminus, test.WHIP, test.ERAminus,
                               test.FIPminus)
        distancesMED.append(distance)
    disHOF = 0

    for i in distancesHOF:
        disHOF += i

    disMED = 0
    for i in distancesMED:
        disMED += i

    avgDisHOF = disHOF/len(hof)
    avgDisMED = disMED/len(med)

    if((avgDisHOF/5.2)>avgDisMED):
        return True
    else:
        return False

def getDistance(x1,y1,z1,x2,y2,z2):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return distance

def main():
    file = os.getcwd() + "/HOFSet.txt"
    file2 = os.getcwd() + "/MediocreSet.txt"
    file3 = os.getcwd() + "/AllPitcherSet.txt"
    file4 = os.getcwd() + "/1000Pitchers.txt"
    file5 = os.getcwd() + "/10000Pitchers.txt"
    file6 = os.getcwd() + "/100000Pitchers.txt"
    file7 = os.getcwd() + "/MillionPitchers.txt"
    hofPitchers = []
    medPitchers = []
    allPitchers = []
    thousandPitchers = []
    tenthouPitchers = []
    hunthouPitchers = []
    millionPitchers = []
    loadData(file, hofPitchers)
    loadData(file2, medPitchers)
    loadData(file3, allPitchers)
    loadData(file4, thousandPitchers)
    loadData(file5, tenthouPitchers)
    loadData(file6, hunthouPitchers)
    loadData(file7, millionPitchers)

    newHOFlist = []
    startTime = time.time()
    for i in allPitchers:
        neighbor = nearestNeighbor(hofPitchers,medPitchers,i)
        if(neighbor == True):
            newHOFlist.append(i.Name)
    endTime = time.time()
    for i in newHOFlist:
        print(i)
    print("Time for All Real Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))

    # newHOFlist = []
    # startTime = time.time()
    # for i in thousandPitchers:
    #     neighbor = nearestNeighbor(hofPitchers,medPitchers,i)
    #     if(neighbor == True):
    #         newHOFlist.append(i.Name)
    # endTime = time.time()
    # print("Time for 1000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    #
    # newHOFlist = []
    # startTime = time.time()
    # for i in tenthouPitchers:
    #     neighbor = nearestNeighbor(hofPitchers,medPitchers,i)
    #     if(neighbor == True):
    #         newHOFlist.append(i.Name)
    # endTime = time.time()
    # print("Time for 10000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    #
    # newHOFlist = []
    # startTime = time.time()
    # for i in hunthouPitchers:
    #     neighbor = nearestNeighbor(hofPitchers,medPitchers,i)
    #     if(neighbor == True):
    #         newHOFlist.append(i.Name)
    # endTime = time.time()
    # print("Time for 100000 Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))
    #
    # newHOFlist = []
    # startTime = time.time()
    # for i in millionPitchers:
    #     neighbor = nearestNeighbor(hofPitchers,medPitchers,i)
    #     if(neighbor == True):
    #         newHOFlist.append(i.Name)
    # endTime = time.time()
    # print("Time for 1 Million Pitchers is " + "\t{0:.6f}\tseconds".format(endTime - startTime))


main()