def CreateProfile(motif, k):
    count = [[0 for i in range(0, k)] for j in range(4)]
    for i in range(0, k):
        for j in range(0, k):
            if (motif[i][j] == 'a') or (motif[i][j] == 'A'):
                count[0][j] += 1
            elif (motif[i][j] == 'c') or (motif[i][j] == 'C'):
                count[1][j] += 1
            elif (motif[i][j] == 'g') or (motif[i][j] == 'G'):
                count[2][j] += 1
            elif (motif[i][j] == 't') or (motif[i][j] == 'T'):
                count[3][j] += 1
    # print(count)
    for i in range(0, len(motif)):
        count[0][i] += 1
        count[1][i] += 1
        count[2][i] += 1
        count[3][i] += 1
    counter = 0
    for i in range(0, len(count)):
        counter += count[0][i]
        counter += count[1][i]
        counter += count[2][i]
        counter += count[3][i]
        count[0][i] /= counter
        count[1][i] /= counter
        count[2][i] /= counter
        count[3][i] /= counter
        counter = 0
    return (count)


def CalculateKmerProb(profile, deletedseq, k):
    probability = [1 for l in range(0, len(deletedseq) - k + 1)]
    for i in range(0, len(deletedseq) - k + 1):
        subseq = deletedseq[i:i + k]

        for j in range(0, k):
            if (subseq[j] == 'a') or (subseq[j] == 'A'):
                probability[i] *= profile[0][j]
            elif subseq[j] == 'c' or (subseq[j] == 'C'):
                probability[i] *= profile[1][j]
            elif (subseq[j] == 'g') or (subseq[j] == 'G'):
                probability[i] *= profile[2][j]
            elif (subseq[j] == 't') or (subseq[j] == 'T'):
                probability[i] *= profile[3][j]

    index = 0
    maxMotif = probability[0]
    for i in range(1, len(deletedseq) - k + 1):
        if maxMotif < probability[i]:
            maxMotif = probability[i]
            index = i

    return (deletedseq[index:index + k])


def GibbsSampling(DNAList, k_length, n):
    RemovedSequance = ""
    RemovedSequances = []
    finalmotifs = []
    i = 0
    counter = 0
    for i in range(0, n):
        motifList = []
        RemovedSequance = DNAList[0]
        RemovedSequances.append(RemovedSequance)
        del DNAList[0]
        counter += 1
        if i == 0:
            for j in range(0, n - 1):
                start = random.randint(0, len(DNAList[j]) - k_length)
                subseq = DNAList[j]
                motifList.append(subseq[start:start + k_length])
            profile = CreateProfile(motifList, k_length)
            motiff = CalculateKmerProb(profile, RemovedSequance, k_length)
            finalmotifs.append(motiff)
        else:
            motifList = finalmotifs[0:]
            for j in range(0, (n - counter)):
                start = random.randint(0, len(DNAList[j]) - k_length)
                end = start + k_length
                subseq = DNAList[j]
                motifList.append(subseq[start:end])
            profile = CreateProfile(motifList, k_length)
            finalmotifs.append(CalculateKmerProb(profile, RemovedSequance, k_length))
        DNAList.append(RemovedSequance)
    return (finalmotifs)


n = int(input('Sequences Number: '))
print("DNA Sequances: ")
DNAList = []
for i in range(0, n):
    # print(i)
    Dna = input()
    DNAList.append(Dna)
k_length = int(input("Enter the Motif length: "))
motifs = GibbsSampling(DNAList, k_length, n)
print("MOTIFS:")
for i in range(0, len(motifs)):
    print(motifs[i])
