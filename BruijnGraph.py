################################################# READ FILE FUNCTIONS #################################################

def readtxtSingleRead (path):
     #read the single reads from text file
     reads=[]
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     for line in file:
         line=line.rstrip() 
         reads.append(line)

     return reads

def readtxtPairedRead (path):
     #read the paired reads from text file
     reads1=[]
     reads2=[]
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     gap=int(line[1])
     for line in file:
         line=line.rstrip() 
         line1=line.split('|') 
         reads1.append(line1[0])
         reads2.append(line1[1])

     return reads1,reads2,gap

def readFastaSingleRead(path):
    #read the single reads from fasta file
     reads=[]
     count=-1
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     for line in file:
         line=line.rstrip()
         if (line[0] == '>'):
            line=file.readline()
            line=line.rstrip()
            reads.append(line)
            count=count+1
         else:
            reads[count]=reads[count]+line 
     file.close()
     return reads

def readFastaPairedRead(path):
    #read the paired reads from fasta file
     reads1=[]
     reads2=[]
     
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     gap=int(line[1])
     file.close()
     
     reads=readFastaSingleRead(path)

     for read in reads:
          splited=read.split('|')
          reads1.append(splited[0])
          reads2.append(splited[1])

     return reads1,reads2,gap

def readFastQSingleRead(path):
    #read the single reads from fasta file
     reads=[]
     count=-1
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     for line in file:
         line= file.readline()
         line=line.rstrip()
         reads.append(line)
         file.readline()
         file.readline()
     file.close()
     return reads

def readFastQPairedRead(path):
    #read the paired reads from fasta file
     reads1=[]
     reads2=[]
     
     file=open(path)
     line = file.readline()
     line=line.split(' ')
     kmer=line[0]
     gap=int(line[1])
     file.close()
     
     reads=readFastQSingleRead(path)

     for read in reads:
          splited=read.split('|')
          reads1.append(splited[0])
          reads2.append(splited[1])

     return reads1,reads2,gap


################################################# SINGLE READ FUNCTIONS #################################################

def prefixSuffix(reads):
    #finds prefix suffix dictionary of single reads
    prefixSuffix={}
    length=len(reads[0])-1
    for i in range (len(reads)):
        prefix=reads[i]
        key=prefix[0:length]
        if key in prefixSuffix:
            prefixSuffix[key].append(prefix[1:])
        else:
            prefixSuffix[prefix[0:length]]=[]
            prefixSuffix[prefix[0:length]].append(prefix[1:])
    return prefixSuffix


def findStart (prefixSuffix):
    #finds start index of prefix suffix dictionary of single reads
    start=''
    for key in prefixSuffix:
        found=True
        for i in prefixSuffix:
            if (key in prefixSuffix[i]):
                found=False
        if (found):
             start=key
             break
    return start
     

def findSequence(prefixSuffix,start):
     #finds the assembled sequence of the single read entered
     sequence=start
     Suf = prefixSuffix[start].pop(0) 
     while(1):
          sequence = sequence + Suf[len(Suf)-1]
          if Suf in prefixSuffix:
               if len(prefixSuffix[Suf])==0: 
                    break
               else:
                   Suf = prefixSuffix[Suf].pop(0)  
          else:
               break     
     return sequence

################################################# PAIRED READ FUNCTIONS ################################################# 

def prefixSuffixPaired(read1,read2):
    #finds prefix suffix of paired reads each in a list of format [[prefix1,prefix2]]
    prefix=[]
    Suffix=[]
    length=len(read1[0])-1
    for i in range (len(read1)):
        prefix1=read1[i]
        prefix2=read2[i]
        key1 = []
        key2 = []
        key1.append(prefix1[0:length])
        key1.append(prefix2[0:length])
        prefix.append(key1)
        key2.append(prefix1[1:])
        key2.append(prefix2[1:])
        Suffix.append(key2)
        
    return prefix,Suffix


def findStartPaired (prefix,Suffix):
     #finds start index of prefix and suffix of paired reads lists as a list [prefix1,prefix2]
     start = []
     for i in range(len(prefix)):
          if (prefix[i] not in Suffix):
               start = prefix[i]
               start_index = i
               break
     return start,start_index
     

def findSequencePaired(prefix,Suffix,start,start_index):
     #finds the sequences of the paired read entered in sequence1 and sequence2
     sequence1=start[0][0]
     sequence2=start[1][0]
     suf = []
     while(1):
          
          start = Suffix[start_index]

          if (start in prefix):
               
               start_index = prefix.index(start)
               start = prefix[start_index]
               sequence1=sequence1+start[0][0]
               sequence2=sequence2+start[1][0]
               #prefix.pop(start_index)
               #Suffix.pop(start_index)
               
          else:
               #termination condition
               #suf=Suffix[start_index]
               sequence1=sequence1+start[0]
               sequence2=sequence2+start[1]
               break
     
   
     return sequence1,sequence2


def findOverlappedSequencePaired(sequence1,sequence2,gap,k):
     #finding the whole assembled sequence using the index calculation
     seq=''
     index=k+gap+1
     print(k)
     print(gap)
     print(index)
     seq=sequence1[:index]+sequence2
     return seq



################################################ RUN TEMPLATES ################################################

####single reads template to run on####
print('####single reads run ####\n')

#1-take the read
""" choose either txt or fatsa read function or fatsq read function """
#reads=readtxtSingleRead('SingleReadsInput.txt')       #in exam just enter path#
#reads=readFastaSingleRead('singleFasta.fasta')          #in exam just enter path#
reads=readFastQSingleRead('SingleReads.fastq')          #in exam just enter path#

#2-find prefixSuffix dictionary and print it
prefixSuffix=prefixSuffix(reads)
"""
print("1- De Bruijn Graph for single read: ")
for i in (prefixSuffix):
    print (i,' : ',prefixSuffix[i])
print('')
"""
#3-find start of the De Bruijn graph
start=findStart(prefixSuffix)
print("2- Start of the De Bruijn graph: ", start)
print('')

#4- find the whole assembled single read sequence
sequence=findSequence(prefixSuffix,start)
print(len(sequence))
print("3- The assembeled single read sequence: ",sequence)
print('')
print('')

"""
pls=0
minus=0
output='TGCCCCTTTGATCGCGGTTCTCGAATCCATGTAAATACAAAGATCTTATGTCCGCCGCGTATAGCGGTCGTAAAAATCTACGAGTTTCGATAACTCCAGGATCAATGCGGAACTATGCCCTTATAATAAGGCCACAATTAGTGCGCGTATTAGTGCGATTCCCATTTGCTCCTTTTCTCAACGACCAACGTAGGCGGGGGATGAGTATGCACACGCCCACCCGCTACACTCGACCCTCTCGGCTCTTTTTGTACCGGGGGCCTATATCTCCTGCACCGCCACCATCGCGTTCTCTCTTATTTTGCTATTATTATTCTTTCCAGAACATATGACATATCAGTGCAAGCTGAATCGCGAAGCGGCACTTAATACGATTTCTTGCGATGTGTCTTCTCGCGGCAATTGCTAGTGCCTGGTAAGTCACCGTGATCGTGTCTATG'
print(len(output))
print(len(sequence))
for i in range (len(output)):
     if (sequence[i]==output[i]):
          pls=pls+1
     else:
          minus+=1

print((pls/len(output))*100)
if (sequence==output):
     print('Be5 saba7 elfol')
"""

####paired reads template to run on####
print('####paired reads run ####\n')

#1-take the read
""" choose either txt or fatsa read function or fatsq read function """
reads1,reads2,gap=readtxtPairedRead('ReadPairsInput.txt')      #in exam just enter path#
#reads1,reads2,gap=readFastaPairedRead('pairedFasta.fasta')      #in exam just enter path#
#reads1,reads2,gap=readFastQPairedRead('pairedFastQ.fastq')      #in exam just enter path#

#2-find prefix and Suffix lists and print it
prefix,suffix=prefixSuffixPaired(reads1,reads2)
"""
print("1- De Bruijn Graph for paired reads: ")
for i in range (len(prefix)):
    print (prefix[i],' : ',suffix[i])
print('')
"""
#3-find start and start index of the De Bruijn graph
start,start_index = findStartPaired(prefix,suffix)
print("2- Start of De Bruijn graph: ", start)
print('')

#4- find the two sequences of paired read sequence
s1,s2=findSequencePaired(prefix,suffix,start,start_index)
print("3- Two sequences of paired reads: ")
print ("Sequence 1: ",s1)
print ("Sequence 2: ",s2)
print('')

#5- find the whole assembled paired read sequence
sequence=findOverlappedSequencePaired(s1,s2,gap,len(reads1[0])-1)
print("4- The assembeled paired read sequence: ",sequence)
print('')
print('')


"""
output='GAAAGGTACAAATACTGGCGACCTCGCTGTTCGACACTTCATCACTGCTCCGGGGCGCTCAGGAGGGACGGTTCCCTGTACCATTGGAAGTCAATAGTCTAAGGTACAAAGAGAAGACCCGACCCGACAGAGGGGGTTCTGCGCCGGGTTTCGAGCTTGTAACCCCCCAGAGAATTAGATCCACCGTCTGTGTGGACAAAGTAGTAAAGCTAGCATACCAAATTGAAATTCGGAGTTTGACTACCAGATCCACGCATACGCTGCACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTAGAAATTCAGAACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGGGGGTAATTCGTAGTTAGGTACAGAAAACTCCCGGACAGAACCGCATATAACCGATGAAGCAAGGGTTCTTCATTTAATACGACCCTAACCGGTATTGCTGCTAGCTTGATTTTCCTAGCAATCTAAACTCTATGTATGAGGCCACTCGGACGCCCGCTAGTGCCGGCAGCTAGCTACTGCCCTTCACCAGGAGCACGCACTATGCCTATCGGGCAATGCTGATCATACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGATCCCTCTGCAGAAAGCGGTGGCGGCGGGTCTAAGCAAGTCCAACGCAATACCAGGAAATCACCGTATCGTTAGCGACCAGTAGGTGATGGTTTGTAAGTTCGGACTACAGGCGGATGTGTCCCCGCCAGTTAAAAGTCGACTTTCTGTTACAACTGCTCCCTACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTCTAATGATCCCCACAGATCGTGTTTCAACGTTGAAGTCTGAATGGGTTCGTGAATATAGCCATCCAACGTGGACAATAAGATGAGCTTTATAGTTTCCGATCCTCATGGCGATCGAATAAGATCTATCCGCTTGTGTGTGTACGAGTCGCCGACTAACCGGTCTTGGGATATATACGTCACAGATTAAGTACTCGTCACGAGCTTGAATGGGAAGATAAGTAGACTCTTGTCGGGCACACACAGAGACTCCGACGCATCGAGATCGCAAACACTGCCTCCAGCCGGGGGATGCTAATCGTCGCGGTCGGTCCGAGCTTTATTCTACATCGTGGTGTTTCCGACCGAGCCATAAGAACAGTGTCCAAGTCACAAGAGGAGCACGCGGTGGAGGTCGTTCGCTATACAATATATTTGCAACTGTGTCTGGCATCACGCGCATTTCTCACACTTCCAAACGTGCTGCATTCTAAATGATTTCATGAATAGATTGTCTACTAGTTCACCCAAGGTATTACAGCACTGGTCATGTGCCGCTCTGGCACGGCTAGTATCAGGGCCGACTGTGTCCTAGGCGGCTGTTTTCGGGAGCCCAAGGGAAGCAATCAATGCGTTGACTGACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGATGACCCTAGGGCGGGCTGTTTGAGTGGGCTATCGGCGACCATTTCGCCCCGCAAGCCCCCGTCACGATACCGAGACCCTGAAGCTCATAAACGCCTATCTTTGTTGCATGAACAACGGGAGTAAGCGAGGCCAGGCCATACGGTTTCGGAGCCGCAGAATAGCCTTTACACGACCTCTACACAACCCAAAGTGAATATCCACGGGGTATTGTTTGTGCTGCTACCATGCGCAGTCAACATCGCCCACCGGCGATGTGTTTCAGATCTGCAGGCCCATCAACCGTTGTGACACCACCCCGGCTTTCAGAAGCAGTATGTCGGACACATTGACCTGTAGCGTTAGTTCTGTACAAGGGACCCTGCTCACTCGAACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTTGGGAATCTAATGCGGTCTGCCATGGGACCCCTAACAACAAGGGACGCCTCCACCTGTCTAGGAGGAAAGACTTTACACACATCTTCTAGTTTCGAGAAGCACCGTAGCCAGTGGACCCTGAGTGGTTACAAACAAATCGCAGTTTAGCGCTTACCGACAAAGGCGGGAGCTTCGTTCACATTAGGATTGAAAGAACTTAAGAGTCTGTAGGCTCGGAGGTCTCTATATATACCATCTAGTCGTCCGGGGCATGATTAACTAAGAGTTGATCTGAGTCGGAACATAATGCCTGATCTGACCCCAATTCACTACGGTCGCACGTTCCGGGAACACCTACCGATCAGTCCGGAACTGTGACCTAAGAAGTCTCAAGCCTTTACGTCAATGTTCCCGGTGAAGGACTGTGTAACGGTCGCCTTCGCGCCCCCCCATAGGCCGGTCCTTCTCGTTGCAGGATAGCTAAGTCCCATATAGAGTTGTTGGTGTACCATTACGCTGATTTTACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTGGTGTGTTCAACTCAGCATACCCGGTTAGTCTGGAGCACTCCCCGTGCCTACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTGCCGAAATCCTTGTCAAGTAGTGGCATCTACTGCCGCGGGGCAGGACTGATGCTGACCCAAGACCACGCTCCTATCAGCCGGTGGCGCATCAGGGTGGGCTATAAGTTATATTCCTACTGTACGGCTGAAGTCAGCTGTAGTCAGGGAGCGGTTCCTGAGCCGGCTGATTCCGCTCGTAATGCGCTATGTAGAAGCATAGTTAGCCTCGCGCTCGTGTGTGGGCAGTCGTATAAGTAGTTTAGCTCCCGATGCGAAGGAGTTGCAAGTACCTACAAACTCGTAACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGTCCGGTTCATATTAACCATGCACCAAGGTTTGACTAAATCAACTCGTGGGAATCCGACGTGACAAAATCCCCAGATATGCCGGGGGTGCACGTGAATACGTCGTAAGTTGAGCGTCCTATGACGGGAACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGCCAAAGTAATACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGAATCCTTGACTGGCCTGCCGAGTGTTATCTCGCTGCTATCCCCCCCCAAGGTAGAAATGGAAGTGGGATCCAGCGCACCAAGGCACTTCACACAGGCATTACCCCAGCACCACGAATTAGCTTGCAGCTAAAGACAGGGTATTTTACGGAGTATATGATCTCTGTGAGGTACCGTATTCACACATCGTGGGATGTCTGCCATGAGCTTTTCCATTAGTATCCGGCGAGTTTTGATCCAAGTTACCAAACAAGGTTGTCCTCCAGGTCCTACGTGCTGAACGGCCAACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGCCGGATCGGCCCTGACTCAAGTAAGGTCTGGTTGCTTGTCACTACATAAAGCCACGGAAGGGTGCGCGGCCCCAAAGCTGCGTCCGGATTCGACTCCCGTTTGCCTGGCTTCTCGACGAATCTAACGTTCTCATTAACCGAAAACCCTGAGCGGCTTAACCTCATTCGTCCCAGAATCAAACCCATCGTGTATCACCGTTGGCCCAGCAGGGAAGACAAGACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGTGTGGCTCCCCAACCGAAGAATAAGATCCCTTCGCCGCCACAGAAGCAACACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGATTTAAAGTCTACCGTGGGGAGCCGGACGAGAACAAGACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGTAGGCGGCTACCTTCTGCCCATATCTCGGAATCCTTAGGGTCTTTAGCTGCTGGCAACACGGGGATGCCTTAGTCGCGGGGGAGCCGTTAGATCGGTTTCAGACTTGCCGACACCGTTCACCGTGGCCGGCCAACCGGCCGGTTCTGTGCTCCACTGAGTTTAGATAGGAATCCATACCTATAGTTTTACGTACACCAACTGGTTAACAAGCCGTCTCCGCGATGACAAACGGTGGGGGCACGAGCTCGAGGTAAGAGGTTGCGATCCGATTACAATGTATGACTACTTATAATGGTCTTACCTTAAATAGGGAACGGGTTTACAGATTACATGTCGGCGAAGACGTTACTGTATTTCGGCCAATGAGCAAATTCCCACCAGGCTCGCTCGGCTTAAATAGAATAGTCAGATTGGCTCTGAATGCTTTGGGCGTGCATTGAGAGCAGCCATATGTAATATTAAATGGCAGTACAAATCATACAGTTCAGAACTGCCGACAGCGCAGGAGTTTAAGGGTATCGAATATTGCGCTATCCGTGAGTGCTCTTAGCGATGGGGGGGCGGACCCTAAGTCTGACCCCCTCTCCTACCTTCTACGGATTACTATTATTGGCACTTGATGAGTAATCATTTCTAGCAAGAGTCTTATAAGGTAAACAATAACTTAGTAAGTGAGTCATGTAGTGTGCTTCCAGGACGAGTCGGCAAACTCTGTAGTCTTATGCTCATGTCTGACCTGCTGTGCCCAAAATTCTCTTCGTAAGGAGGGCTTTATAATGTTATGGGCACGACTTCGCATTGGGTCCACGCCCCAGGACTTCAGCATGTTATTTTGGGTTGCAGGATTTAAGAGAGCCTCATGCGTTGATAAGCCAAAGTGGGGGTATGGTGGGACCTCTCACCATGAGAGTTAAGTTAACTCACCGTGGCTCAAAAAAAGCTGGTTAGAATCTGCGAGTAATACGAGCGGGAAAATCTGGAATAACAGAAGCGACACCCTGACCTACAGTCGTTCAGTACTAGGTTACAAGTGAACCACTCGCGGATATAGTCAGGCGGGGATGTCCCGCGCGTTGATTAGACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGCGAGTTAATTGAAGTTTGCCTAGACACCGCTGAGGCTGGTTCGACATACCCTTAGGGAGGCCAAGCTATATAAAACCAAGATCATTGACCCCCTACGTGATACGTGATTTCAAACTTTACAATCATTAGGGTCGCCAGTGGAGAATCTATAGAATCTTTTCTACAGGCTACAGAGAAGCATTTTTCACAGGACCGCGTGGCGCAAACAATCCGATGGGGACCATCTGTGAACTCCCATACGTGACTATTCTGTGTCACATGAGGGGAGCTAGGGGGATTGAGTGCTCATGTCGGTTGGAGACCATTTTGAGTGCACAAGGGACCCTGCTCACTCGATTGGGAATCTAATGCGGTCTGCCATGGGGCGAAGCATACTTACCTTGATCAACGCAGTGATTATTCATCTGAAGAGGATTGGGATAATACTGCGAACATATTGGAAAATTAACTGATTTATCTTCTGATCGATTCCCACACTCCACGAATTGGGGTGCCATGCTCCCATAGTAGGCCCTAGAGATGCCGATCATTCCGCAGGTGTGCCTAAGTGGACAGTCACTTGGCACTTAGGCCAATAAGTACAACAAAGGGATCAGTGGGCAAATTATCAGCGTACAATTCCCAGATATATAGGCGGCGAGAAAAGCTTCAAAAGACTTAATTTACTAGCCTCCTACAAACTCTAGATGAGGATTGGCTCTTGATGCTAGCGTTTTCATTTTCCATTACAAGACATTAGGCTGATAATTGCAGAGATTGGCGGCGTAGACTGACAGTCGCGATCAATCTGCGTGTTA'
pls=0
minus=0
print(len(output))
print(len(sequence))
for i in range (len(output)):
     if (sequence[i]==output[i]):
          pls=pls+1
     else:
          minus+=1

print((pls/len(output))*100)
if (sequence==output):
     print('Be5 saba7 elfol')

"""

