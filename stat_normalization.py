import math

SNPLIST=[[]*1 for y in range(22)]
count=[[0]*1 for p in range(101)]
SNPSUM=[[0]*1 for z in range(101)]
MEAN=[[0]*1 for v in range(101)]
DEVST=[[0]*1 for q in range(101)]
DEVST_TEMP=[[0]*1 for _ in range(101)]
for K in range(22):
        infile=open("tarpop_"+str(K+1)+"_withfreq.txt")
        for line in infile:
                line=line.strip()
                line=line.split("\t")
                SNPLIST[K].append(line)
                #SNPBIN[int(line[-1])*100].append(line)
                #print line[-1], int(float(line[-1])*100), SNPSUM[int(float(line[-1])*100)]
                SNPSUM[int(float(line[-1])*100)][0]=SNPSUM[int(float(line[-1])*100)][0]+float(line[10])
		count[int(float(line[-1])*100)][0]=count[int(float(line[-1])*100)][0]+1
for Z in range(len(SNPSUM)):
	if float(count[Z][0])>0:
		MEAN[Z][0]=float(SNPSUM[Z][0])/float(count[Z][0])
#	print SNPSUM[Z][0], count[Z][0], MEAN[Z][0]
for P in range(len(SNPLIST)):
	for z in range(len(SNPLIST[P])):
		DEVST_TEMP[int(float(SNPLIST[P][z][-1])*100)][0]=DEVST_TEMP[int(float(SNPLIST[P][z][-1])*100)][0]+((float(SNPLIST[P][z][10]))-MEAN[int(float(SNPLIST[P][z][-1])*100)][0])**2
for H in range(len(DEVST_TEMP)):
	DEVST[H][0]=math.sqrt(float(DEVST_TEMP[H][0])/(count[H][0]-1))
for M in range(len(SNPLIST)):
        outfile=open("normalized_H12_tarpop_chr"+str(M+1)+".txt","w")
        for m in range(len(SNPLIST[M])):
                if float(SNPLIST[M][m][-1])>=0.0 and float(SNPSUM[int(float(SNPLIST[M][m][-1])*100)][0]) > 0:
#                       print SNPLIST[M][m][-1], SNPLIST[M][m][-3], float(SNPSUM[int(float(SNPLIST[M][m][-1])*100)][0])
                        word=""
                        for element in SNPLIST[M][m]:
                                word=word+element+"\t"
                        word=word+str((float(SNPLIST[M][m][10])-MEAN[int(float(SNPLIST[M][m][-1])*100)][0])/DEVST[int(float(SNPLIST[M][m][-1])*100)][0])
			#print word
			outfile.write(word+"\n")
	outfile.close()
