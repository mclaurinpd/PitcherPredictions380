'This method should fail miserably to predict who should be in the hall of fame'

import csv
from numpy import arange, array, ones, linalg
import time


def loadCsv(filename):

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', names=['Name', 'WHIP', 'ERA-', 'FIP-'])
        dataset = list(reader)
        for row in reader:
            print(row)
    return dataset


def main():
    hofPitcher = 'HOVSet.csv'
    regularPitchers = 'AllPitcherSet.csv'
    hofset = loadCsv(hofPitcher)
    regularset = loadCsv(regularPitchers)

    print(hofset)
    print(regularset)