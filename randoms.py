import random, string, math

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def main():
    #testPitchers = input("How many pitchers do you want? ")
    fileName = input("Please enter a file name: (with .txt at end) ")
    file = open(fileName,'w')
    for i in range(0,1000000):
        names = randomword(10)
        whip = math.ceil(random.normalvariate(1.10,1.50)*100)/100
        fip = random.randint(50,150)
        era = random.randint(50,150)
        pitcher = str(str(names)+","+str(whip)+","+str(era)+","+str(fip))
        print(pitcher)
        file.write(pitcher+"\n")
    file.close()
main()
