import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def main():
    fileName = input("Please enter a file name: (with .txt at end) ")
    file = open(fileName,'w')
    for i in range(0,10000):
        names = randomword(10)
        whip = int((random.normalvariate(1.35,.15) * 100) + 0.5) / 100.0
        if(whip<=1.2):
            fip = random.randint(50,75)
            era = random.randint(50,75)
        elif(1.2<=whip<1.4):
            fip = random.randint(75,125)
            era = random.randint(75,125)
        else:
            fip = random.randint(125,150)
            era = random.randint(125,150)
        pitcher = str(str(names)+","+str(whip)+","+str(era)+","+str(fip))
        print(pitcher)
        file.write(pitcher+"\n")
    file.close()
main()
