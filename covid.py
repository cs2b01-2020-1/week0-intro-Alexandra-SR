#genome1
with open("AY274119.txt") as genome1:
  text1 = genome1.read().splitlines()

g1chars=[]
for lines1 in text1:
    for chars1 in lines1:
        g1chars.append(chars1)


#genome2
with open("AY278488.2.txt") as genome2:
  text2 = genome2.read().splitlines()

g2chars=[]
for lines2 in text2:
    for chars2 in lines2:
        g2chars.append(chars2)

#genome3
with open("MN908947.txt") as genome3:
  text3 = genome3.read().splitlines()

g3chars=[]
for lines3 in text3:
    for chars3 in lines3:
        g3chars.append(chars3)


#genome4
with open("MN988668.txt") as genome4:
  text4 = genome4.read().splitlines()

g4chars=[]
for lines4 in text4:
    for chars4 in lines4:
        g4chars.append(chars4)


#genome5
with open("MN988669.txt") as genome5:
  text5 = genome5.read().splitlines()

g5chars=[]
for lines5 in text5:
    for chars5 in lines5:
        g5chars.append(chars5)

genomesdata=[g1chars, g2chars,g3chars,g4chars,g5chars]

def comparegenomes(genome_A, genome_B):
    count=0
    similarity_percentage=0
    min_leng_genome= min(len(genome_A), len(genome_B))
    for char in range(min_leng_genome):
        if genome_A[char]==genome_B[char]:
            count=count+1
    similarity_percentage = round((count/len(genome_A)*100),3)
    return  similarity_percentage

def print_table(genomesdata):
    print("A continuación se muentra una tabla en la que se evalua el porcentaje  de similitud al comparar 5 genomas:")
    print()
    print("\t", end="")

    for y in range(len(genomesdata)):
        print("       Genome", y+1, end = "     ")
        print(end="\t")

    print()

    x=0
    for x in range (len(genomesdata)):
        print("Genome",x+1,  end = "      ")
        print()
        for y in range (len(genomesdata)):
            value= comparegenomes(genomesdata[x],genomesdata[y])
            if x!=y:
                print("           ",value,  end = "     ")
            elif x==y:
                print("              100  ",  end = "   ")
        print()




print_table(genomesdata)
