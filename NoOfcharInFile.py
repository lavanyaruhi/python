import os

def counters(file):
    Nwords=0
    Nchars=0
    Nlines=0
    Nspaces=0
    with open(file,'r') as f:
        for line in f:
            line = line.strip(os.linesep)
            wordsList=line.split()
            Nlines += 1
            Nwords=Nwords+len(wordsList)
            Nchars=Nchars+sum(1 for c in line if c not in (os.linesep,' '))
            Nspaces=Nspaces+sum(1 for s in line if s in (os.linesep, ' '))


    print("No.of lines: ",Nlines)
    print("No.of words:",Nwords)
    print("No.of chars:",Nchars)
    print("No. of spaces:",Nspaces)

if __name__=="__main__":
    file="networkPython.txt"
    try:
        counters(file)
    except:
        print("file not existed")





