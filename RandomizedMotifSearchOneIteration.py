f=open("motifs.txt")
x=open("pr.txt","w")
motifs=[]
for i in range(4):
      motifs.append(f.readline().rstrip())
      
A=[]
C=[]
G=[]
T=[]


ac=0
cc=0
gc=0
tc=0
      
for i in range (3):
      for j in range(len(motifs)):
            if motifs[j][i]=='A':
                  ac+=1
            elif motifs[j][i]=='C':
                  cc+=1
            elif motifs[j][i]=='G':
                  gc+=1
            elif motifs[j][i]=='T':
                  tc+=1
      A.append(ac/4.0)
      C.append(cc/4.0)
      G.append(gc/4.0)
      T.append(tc/4.0)
      ac=0
      cc=0
      gc=0
      tc=0

print ("A :",A)
print("C:",C)
print("G:",G)
print("T :",T)

A = [str(i) for i in A]
x.write(' '.join(A)+"\n")
C = [str(i) for i in C]
x.write(' '.join(C)+"\n")
G = [str(i) for i in G]
x.write(' '.join(G)+"\n")
T = [str(i) for i in T]
x.write(' '.join(T)+"\n")
x.close()

f=open("pr.txt")
dic={}
l=f.readline().rstrip().split()
l = [float(i) for i in l]
dic["A"]=l
l=f.readline().rstrip().split()
l = [float(i) for i in l]
dic["C"]=l
l=f.readline().rstrip().split()
l = [float(i) for i in l]
dic["G"]=l
l=f.readline().rstrip().split()
l = [float(i) for i in l]
dic["T"]=l

seqs=[]
x = open("seqs.txt")
for i in range (4): #seqs
      maxV=-1
      maxd=[]
      seq= x.readline().rstrip()
      for j in range (len(seq)-3+1):#one seq threes
            d=seq[j:j+3]
            ans=1
            for k in range(len(d)):
                  ans=ans*dic[d[k]][k]
            if ans>maxV:
                  maxV=ans
                  maxd=[]
                  maxd.append(d)
            if ans == maxV and d not in maxd:
                  maxd.append(d)
      print(maxd)
      
            


      
