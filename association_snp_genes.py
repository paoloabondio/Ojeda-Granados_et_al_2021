CHRS=[[]*1 for k in range(22)]
infile=open("Chromosome_list.txt")
infile.readline()
for line in infile:
	line=line.strip()
	line=line.split("\t")
	if line[3] not in ["X", "Y", "MT"]:
		CHRS[int(line[3])-1].append(line)

for J in ["tarpop"]: # "southernclusterpops", "seripop", "tarpop", "centralclusterpops"
	for K in range(1,23):
		outfile1=open("Annotated_H12_"+J+"_chr"+str(K)+".txt","w")
		snplist=[]
		infile1=open("normalized_H12_"+J+"_chr"+str(K)+".txt")
		#snplist=[]
		for line1 in infile1:
			line1=line1.strip()
			line1=line1.split("\t")
			line1[2]=line1[2].split(":")
			variant=int(line1[2][1])
			#print line1[0]
			if float(line1[-2])> 0.0:
				for element in CHRS[K-1]:
					if int(element[1])<=variant<=int(element[2]):
						snplist.append(variant)
						word=str(element[3])+"\t"+str(element[4])+"\t"+str(variant)+"\t"+str(line1[-1])+"\t"+str(element[0])+"\t"+"0"+"\t"+str(element[5])+"\t"+str(element[6])+"\n"
						outfile1.write(word)
		infile1=open("normalized_H12_"+J+"_chr"+str(K)+".txt")
		for line1 in infile1:
                	line1=line1.strip()
                	line1=line1.split("\t")
                	line1[2]=line1[2].split(":")
                        variant=int(line1[2][1])
                	min_dist=50000
                	gene=[]
			for element in CHRS[K-1]:
				if float(line1[-2])>0.0:
					if int(element[1])-50000<=variant<int(element[1]) and variant not in snplist:
						d=int(element[1])-variant
						if d<min_dist:
							min_dist=d
							gene=element
						#word=str(element[3])+"\t"+str(line1[0])+"\t"+str(line1[1])+"\t"+str(element[0])+"\t"+str(int(element[1])-line1[0])+"\n"
						#outfile1.write(word)
					elif int(element[2])<variant<=int(element[2])+50000 and variant not in snplist:
						d=variant-int(element[2])
						if d<min_dist:
                                        		min_dist=d
                                        		gene=element
						#word=str(element[3])+"\t"+str(line1[0])+"\t"+str(line1[1])+"\t"+str(element[0])+"\t"+str(line1[0]-int(element[2]))+"\n"
						#outfile1.write(word)
			if min_dist!=50000:
				word=str(gene[3])+"\t"+str(gene[4])+"\t"+str(line1[1])+"\t"+str(line1[-2])+"\t"+str(gene[0])+"\t"+str(min_dist)+"\t"+str(gene[5])+"\t"+str(gene[6])+"\n"
				#print word
                		outfile1.write(word)
		outfile1.close()
