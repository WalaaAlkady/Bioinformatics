def Fill_Matrix(RNA):
    length = len(RNA)
    Matrix = [[0 for j in range(0 , length)]for i in range(0 , length)]
    num_rows = length - 1
    for iterate in range(0 , length - 1):
        i = 0
        j = iterate+1
        while i < num_rows and j < length:

            energy = 0
            if (RNA[i] == 'A' and RNA[j] == 'U') or (RNA[j] == 'A' and RNA[i] == 'U'):
                energy = 1
            if (RNA[i] == 'G' and RNA[j] == 'C') or (RNA[j] == 'G' and RNA[i] == 'C'):
                energy = 1
            if (RNA[i] == 'G' and RNA[j] == 'U') or (RNA[j] == 'G' and RNA[i] == 'U'):
                energy = 1
            Loop = 0
            for k in range(i+1 , j):
                Loop = max(Loop , Matrix[i][k] + Matrix[k+1][j])
            Matrix[i][j] = max(Loop , Matrix[i+1][j-1] + energy , Matrix[i+1][j] , Matrix[i][j-1])
            i = i + 1
            j = j + 1

        num_rows = num_rows - 1
    return Matrix
class node:
    def __init__(self , indx , List):
        self.indx = indx
        self.List = List
def Traceback(Matrix , length , Rna):
   queue = []
   all = []
   start = node([0 , length -1 ] , [])
   queue.append(start)
   while len(queue) != 0 :
       cur = queue[0]
       del(queue[0])
       i = cur.indx[0]
       j = cur.indx[1]

       List = cur.List
       if i >= j:
            continue
       if Matrix[i][j] == 0:
            all.append(List)

            continue
       if (Matrix[i + 1][j - 1] == Matrix[i][j] - 1) and (
               (Rna[i] == 'C' and Rna[j] == 'G') or
               (Rna[i] == 'A' and Rna[j] == 'U') or
               (Rna[j] == 'C' and Rna[i] == 'G') or
               (Rna[j] == 'A' and Rna[i] == 'U') or
               (Rna[i] == 'G' and Rna[j] == 'U') or
               (Rna[j] == 'U' and Rna[i] == 'G')


       ):
           tmp_List = list(List)
           tmp_List.append([i, j])
           tmp_node = node([i + 1, j - 1], tmp_List)
           queue.append(tmp_node)

       if Matrix[i+1][j] == Matrix[i][j] :
           tmp_List = list(List)
           tmp_node = node([i+1 , j] , tmp_List)
           queue.append(tmp_node)

       if Matrix[i][j-1] == Matrix[i][j]:
           tmp_List = list(List)
           tmp_node = node([i, j-1], tmp_List)
           queue.append(tmp_node)

       if 1:
           for k in range(i+1 , j):
               if Matrix[i][k] + Matrix[k+1][j] == Matrix[i][j]:
                   tmp_List = list(List)
                   tmp_node = node([k+1, j], tmp_List)
                   queue.append(tmp_node)
                   tmp_node = node([i, k], tmp_List)
                   queue.append(tmp_node)

                   break
   MaX_len = 0
   final_ans = []

   for indx in all:

       if MaX_len < len(indx):
           final_ans = indx
           MaX_len = len(indx)
   Str =['.' for i in range(0 , len(Rna))]
   for i in range(0 , len(final_ans)):
       Str[final_ans[i][0]] = '('
       Str[final_ans[i][1]] = ')'
   final_RNA = ''
   for i in Str:
       final_RNA += i
   return final_RNA




Rna = input('Enter RNA Sequence : ')
Matrix = Fill_Matrix(Rna)
RNA_Structure = Traceback(Matrix , len(Rna) , Rna)
print(RNA_Structure)