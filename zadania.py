from string import ascii_uppercase
def loaddata(data):
    file=open(data, "r")
    p=list(map(str.strip, file.readlines()))
    return p
def zad1():
    arrays=loaddata("napisy.txt")
    digits=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    counter=0
    for item in arrays:
        for character in item:
            if character in digits:
                 counter+=1
    print(counter)
def zad2():
    arrays=loaddata("napisy.txt")
    k=1
    code=""
    for n, item in enumerate(arrays):
        if n==(k*20)-1:
            code+=item[k-1]
            k+=1
    print(code)
def zad3():
    alphabet=list(ascii_uppercase)
    digits=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    characters=alphabet+digits
    arrays=loaddata("napisy.txt")
    palindroms=""
    for item in arrays:
        firstlist=""
        secondlist=""
        n=len(item)-1
        for i in range(int(len(item)/2)):
            firstlist+=item[i]
        while n>=int(len(item)/2):
            secondlist+=item[n]
            n-=1
        for i in characters:
            if i+firstlist==secondlist+firstlist[-1]:
                palindroms+=firstlist[-1]
            if firstlist+secondlist[-1]==i+secondlist:
                palindroms+=item[25]
        #print(firstlist, secondlist)
    print(palindroms)
def zad4():
    arrays=loaddata("napisy.txt")
    digits=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    pairs=[]
    for item in arrays:
        pair = ""
        for n,character in enumerate(item):
            if character in digits:
                pair+=character
            if len(pair)==2 and int(pair)>=65 and int(pair)<=90:
                pairs.append(int(pair))
                pair=""
            elif len(pair)==2:
                pair=""
    code=""
    n=0
    for i in pairs:
        if i==88:
            n+=1
        else:
            n=0
        if n==3:
            code += chr(i)
            break
        else:
            code+=chr(i)
    print(code)
zad1()
zad2()
zad3()
zad4()