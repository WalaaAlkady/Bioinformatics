#importing Alignment libraries
from Bio import pairwise2
'''
explanation of the two characters in the global and local functions:
-The first character for the mach:
  x: identical characters have score 1, otherwise 0
  m: mach and mismatch scores
  d: dictionary returns the score of any pair
  c: functions returns score

-The second character for the gap penalty:
  x: no gap penalty
  s: tha same penalty for the open and extend gaps
  d: different penalties for the open and extend gaps
  c: functions returns gap penalty
'''
from Bio import SeqIO

def globalAlig (seq1 , seq2):
    "Applying Globa Alignment Using pairwaise2 library from biopython"
    alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)
    print("Global Alignment:")
    print(pairwise2.format_alignment(*alignments[0]))

def localAlig (seq1 , seq2):
    "Applying Globa Alignment Using pairwaise2 library from biopython"
    alignments = pairwise2.align.localxx(seq1.seq, seq2.seq)
    print("Local Alignment:")
    print(pairwise2.format_alignment(*alignments[0]))

def globalAffinGapAlig (seq1 , seq2 , match , mismatch , open , extension):
    "Applying Globa Alignment Using pairwaise2 library from biopython"
    alignments = pairwise2.align.globalms(seq1.seq, seq2.seq, match , mismatch , open , extension)
    print("Global Alignment With Affine Gap Cost:")
    print(pairwise2.format_alignment(*alignments[0]))


# Main:
seq1 = SeqIO.read("C:\\Users\\lulud\\OneDrive\\Desktop\\New folder\\alpha.faa", "fasta")
seq2 = SeqIO.read("C:\\Users\\lulud\\OneDrive\\Desktop\\New folder\\beta.faa", "fasta")
globalAlig(seq1 , seq2)
localAlig(seq1 , seq2)
globalAffinGapAlig(seq1 , seq2, 2 , -1 , -0.5 , -0.1)
