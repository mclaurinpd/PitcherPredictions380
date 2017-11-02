import csv
import random
'''
Authors: Brenton Belanger, David Matrisciano II, and Phillip McLaurins
'''

def loadCSV(file,list):
	with open(file, 'rb') as csvfile:
	reader = csv.reader(f)
	for row in spamreader:
		tokens = row.split(',')
                name = tokens[0]
		whip = float(tokens[1])
		era = float(tokens[2])
		fip = float(tokens[3])
		pitcher = Pitcher(name,whip,era,fip)
		list.append(pitcher)

def main():
	file = open("AllPitcherSet.csv","r")
        allPitchers =[]
	loadCSV(file,allPitchers)
