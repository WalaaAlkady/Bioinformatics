f = open("codon.txt")
aaDict={}
for line in f:
      line=line.rstrip() #Remove any trailing characters
      words = line.split(":")
      codon=words[0]
      aa = words[1]
      aaDict[codon]=aa


def reverseComp(dna):
      dna=dna[::-1]
      comp={'A':'T', 'T':'A','G':'C','C':'G'}
      dnalist= list(dna)
      dnalist=[comp[base] for base in dnalist]
      return ''.join(dnalist)

def Translation (dna,frame):
      #Find index of start codon
      index = -1
      for i in range(frame,len(dna),3):
            codon=dna[i:i+3]
            if codon == "ATG":
                  index = i
                  break
            
      if index == -1:
            print("No start codon")
      else:
            proteinlist=[]
            for i in range(index,len(dna),3):
                  codon=dna[i:i+3]
                  if len(codon)<3:
                        break
                  aa=aaDict[codon]
                  if aa == "Stop":
                        break
                  proteinlist.append(aa)
            protein = ''.join(proteinlist)
            print(protein)
            
      
#Main
dna = input ("Please enter dna sequence")
for i in range(3):
      Translation(dna,i)
      Translation(reverseComp(dna),i)






      
      
