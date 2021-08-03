map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


	
def DNAtoRNA(DNA):
	"Convert DNA Sequence To RNA and Return RNA"
	return DNA.replace("T","U")


	
	
def RevComp(DNA):
    "Reverse and Complements DNA sequence and Return The reversed Sequence"
    CompDNA = ""
    
    for ch in DNA:
            if ch =="A":
                    CompDNA+="T"
            elif ch=="T":
                    CompDNA+="A"
            elif ch=="C":
                    CompDNA+="G"
            else:
                    CompDNA+="C"
                    
    return CompDNA[::-1]



def Translation(RNA):
    "Translate RNA to Protein Sequence and return AA"
    protein = ""
    
    #if it is not divided on 3 delete the remaining characters
    while len(RNA) % 3 != 0:
            RNA = RNA[0:len(RNA)-1]
            
    for i in range (0 , len(RNA), 3):
        if map[RNA[i:i+3]] == "STOP":
            protein += "*"

        protein += map[RNA[i:i+3]]

    return protein

def Find(pattern, Seq, start_ind):
    start_Index = 0
    count = 0
    patIndex = 0
    Index = 0
    while start_ind < len(Seq):
        if pattern[patIndex] == Seq[start_ind]:
            if count == 0:
                index = start_ind
            count = count+1
            patIndex = patIndex+1
        else:
            count=0
            patIndex=0

        start_ind = start_ind+1

        if count == len(pattern):
            return index
    return -1

#This function finds the position of DNA that encodes the input protein
def Encoding(DNA,AA):

        EncodeList = []
        RNAforward = DNAtoRNA(DNA)
        RNAreverse = DNAtoRNA(RevComp(DNA))
        for i in range(0,3):
                start_ind = 0
                AAforward = Translation(RNAforward[i:])
                while start_ind < len(AAforward):
                        start_ind = Find(AA , AAforward , start_ind)
                        if start_ind == -1:
                                break
                        else:
                                EncodeList.append(DNA[i+start_ind*3:i+start_ind*3+len(AA)*3])
                                start_ind+=1
                start_ind = 0
                AAreverse = Translation(RNAreverse[i:])
                while start_ind < len(AAreverse):
                        start_ind = Find(AA , AAreverse , start_ind)
                        if start_ind == -1:
                                break
                        else:
                                cstart_ind=len(DNA)-(i+start_ind*3)-3*len(AA)
                                p = DNA[cstart_ind:cstart_ind+len(AA)*3]
                                EncodeList.append(p)
                                start_ind += 1
        return EncodeList


#Main Function Calling
DNA = input("Enter DNA Sequence: ")
AA  = input("Enter Amino Acid Sequence: ")
print(Encoding(DNA , AA))	
   
