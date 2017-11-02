import csv
import random
import os
from Pitcher import Pitcher
'''
Authors: Brenton Belanger, David Matrisciano II, and Phillip McLaurin
'''

def loadData(file,list):
	with open(file, 'r') as file:
		for line in file:
			tokens = line.split(',')
			name = tokens[0]
			whip = float(tokens[1])
			era = float(tokens[2])
			fip = float(tokens[3])
			pitcher = Pitcher(name,whip,era,fip)
			list.append(pitcher)

def main():
	file = os.getcwd() + "\\HOFSet.txt"
	allPitchers =[]
	loadData(file,allPitchers)
	for x in allPitchers:
		x.__str__()
		print()

main()