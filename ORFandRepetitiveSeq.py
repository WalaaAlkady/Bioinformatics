#read file and get ID, sequences and number of sequences 
def read_file () :
    file = open("D:\dna.example.fasta")
    seq={}
    count=0
    iDs = []
    for line in file :
        line = line.rstrip()
        if (line[0]=='>') :
            words=line.split()
            iD = words[0][1:]
            seq[iD]=''
            iDs.append(iD)
            count=count + 1 
        else :
            seq[iD]=seq[iD]+line
    file.close()
    return count , seq , iDs



#calculate minimum and maximum get mninimum and maximum of sequnces
def max_and_min (count,sequences,keys) :
    maxi = []
    mini = []
    length_maxi=[]
    length_mini=[]
    minimum = 1000000
    maximum = 0
    length = count
    for i in range(0,length,1):
        seq = sequences[keys[i]]
        length_of_seq = len(seq)
        if length_of_seq > maximum :
            maximum = length_of_seq
            del maxi[0:]
            del length_maxi[0:]
            maxi.append(keys[i])
            length_maxi.append(length_of_seq)
        elif length_of_seq == maximum :
            maxi.append(keys[i])
            length_maxi.append(length_of_seq)
        if length_of_seq < minimum :
            minimum = length_of_seq
            del mini[0:]
            del length_mini[0:]
            mini.append(keys[i])
            length_mini.append(length_of_seq)
        elif length_of_seq == minimum :
            mini.append(keys[i])
            length_mini.append(length_of_seq)
    return maxi , mini , length_mini , length_maxi


#get open reading frame for sequences at spcific frame
def ORF (iDs,count,dect,frame) :
    ORF_seq=""
    new_seq=[]
    new_dic={}
    set1 = {}
    open_id = []
    bmw=0
    stop_codons=["tga","tag","taa"]
    if frame == 0 :
            var=3
    else :
            var=1
    for x in range (0,count,1) :
        dna=dect[iDs[x]]
        new_seq = []
        if var > 1 :
            frame = 0
        for c in range (0,var,1) :
            if var > 1 :
                frame = frame + 1
                #print (frame)
            else :
                frame = frame
            for i in range((frame-1),len(dna),3) :
                start_codon=dna[i:i+3].lower()
                if start_codon == 'atg' :
                    ORF_seq=start_codon
                    for j in range(i+3,len(dna),3) :
                        stop_codon=dna[j:j +3].lower()
                        ORF_seq+=stop_codon
                        if stop_codon in stop_codons :
                            #new_seq = new_dic[iDs[x]]
                            new_seq.append(ORF_seq)
                            new_dic[iDs[x]]=new_seq
                            open_id.append(iDs[x])
                            set1=set(open_id)
                            open_id = list(set1)
                            #print (new_dic)
                            ORF_seq = ''
                           # bmw=1
                            break
                #if bmw == 1 :
                    #break
    return new_dic , open_id

#get maximum ORF
def max_ORF (dictionary,count,iDs,frame) :
    dic , open_id = ORF(iDs,count,dictionary,frame)
    nmaxi = []
    nlength_maxi=[]
    max_squ= []
    nmaximum = 0
    nseq = []
    nlength = len (open_id)
    for i in range(0,nlength,1):
        nseq = dic[open_id[i]]
        for j in range(0,len(nseq),1) :
            nlength_of_seq = len(nseq[j])
            if nlength_of_seq > nmaximum :
                nmaximum = nlength_of_seq
                del nmaxi[0:]
                del nlength_maxi[0:]
                del max_squ[0:]
                nmaxi.append(open_id[i])
                nlength_maxi.append(nlength_of_seq)
                max_squ.append(nseq[j])
            elif nlength_of_seq == nmaximum :
                nmaxi.append(open_id[i])
                nlength_maxi.append(nlength_of_seq)
                max_squ.append(nseq[j])
                
    return nmaxi , nlength_maxi , max_squ

# return repeatative dictionary
def repeat (var,dic,count,list_ID) :
    seq=""
    list_sequences=[]
    set_sequences={}
    new_list=[]
    x=0
    y=0
    repeat_sequences={}
    for i in range (0,count,1) :
        seq = dic[list_ID[i]]
        for j in range (0,len(seq)-var+1,var) :
                        word = seq[i:i+var]
                        word=word.lower()
                        list_sequences.append(word)
    set_sequences = set(list_sequences)
    new_list = list(set_sequences)
    for i in range (0,len(set_sequences),1) :
        for j in range (0,len(list_sequences),1):
            if new_list[i]== list_sequences[j] :
               x += 1
        repeat_sequences[new_list[i]]= x
        x=0
        y+=1
    return repeat_sequences , y , new_list



maxi=0
var , dicts , listiD = read_file()
z , w , xdict = max_ORF(dicts,var,listiD,3)
seq=" "
maxil =[]

for i in range(0,len(z),1) :
    seq = dicts[z[i]]
    seq = seq.lower()
    g = seq.find(xdict[i]) + 1
dictionary , count , sets =repeat(7,dicts,var,listiD)
for i in range (0,count,1):
    w=dictionary[sets[i]]
    if w > maxi :
        maxi = w
        seq=sets[i]
        del maxil[0:]
        maxil.append(seq)
    elif w == maxi :
        maxil.append(seq)
        
print(maxi)
print(maxil)






