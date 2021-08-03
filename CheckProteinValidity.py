def CheckProteinValidity(protein):
    for i in range(len(protein)):
        if protein[i].upper() not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
            print('Invalid Protein')
            print ("The Protein contains invalid amino acid %s at position %d" %(protein[i] , i) )
            return

    print('Valid Protein')


# Main:
protein = input("Please Enter the Protein Sequence:")
CheckProteinValidity(protein)