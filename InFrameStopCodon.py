def IsDNAorRNAhasStopCodon(seq , DNAorRNA):
    "This function checks if given sequence has in frame stop codon"
    DNAStopCodons = ['TGA' , 'TAG' , 'TAA']
    RNAStopCodons = ['UGA' , 'UAG' , 'UAA']
    hasStopCodon = False

    if DNAorRNA == '1':
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3].upper()
            if codon in DNAStopCodons:
                hasStopCodon = True
                break
    else:
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3].upper()
            if codon in RNAStopCodons:
                hasStopCodon = True
                break

    return hasStopCodon


# Main:
Sequence = input("Please Enter the Sequence:")
DNAorRNA = input("Enter 1 for DNA and 2 for RNA ")
if IsDNAorRNAhasStopCodon(Sequence , DNAorRNA):
    print('Input Sequence has an in frame stop codon')
else:
    print('Input Sequence has no an in frame stop codon')