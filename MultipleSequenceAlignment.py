#You should download ClustalW exe first from the following link and specify its path
# http:://www clustal org/download/current/

def MultipleSeqAlign(folderPath , fastaFileName):
    #Prepraing ClustalW module
    import os
    from Bio.Align.Applications import ClustalwCommandline
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=folderPath+fastaFileName+".fasta")
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"

    #Runing Clustalw Command
    clustalw_cline()

    #Applying ClustalW on sequences
    from Bio import AlignIO
    align = AlignIO.read(folderPath+fastaFileName+".aln", "clustal")
    print(align)

    #Printing phylogenetic tree
    from Bio import Phylo
    tree = Phylo.read(folderPath+fastaFileName+".dnd", "newick")
    Phylo.draw_ascii(tree)


# Main:
folderPath = r"C:\\Users\\lulud\\OneDrive\\Desktop\\New folder\\"
fastaFileName = "opuntia"
MultipleSeqAlign(folderPath , fastaFileName)
