import sys

info_tab=[]
variants=[]

infile=open(sys.argv[1])
for line in infile:
	line=line.strip()
	line=line.split(" ")
	info_tab.append(line[:5])
	word=""
	for element in line[5:]:
		if element=="0":
			word=word+line[3]
		else:
			word=word+line[4]
	variants.append(word)
w=int(sys.argv[2])
s=int(sys.argv[3])
print len(variants[0])
c=0
outfile=open(sys.argv[4]+"_"+str(w)+"_"+str(s)+".txt","w")
for K in range(w/2, len(variants)-w/2, s):
	variants_sub=[]
	for n in range(K-w/2, K+w/2):
		variants_sub.append(variants[n])
	haplo_sub=[]
	for m in range(len(variants_sub[0])):
		haplo=""
		for p in range(len(variants_sub)):
			haplo=haplo+variants_sub[p][m]
		haplo_sub.append(haplo)
	#print haplo_sub
	haplo_order=list(set(haplo_sub))
	counter=[]
	for element in haplo_order:
		h=haplo_sub.count(element)
		counter.append(h/float(len(variants[0]))) #attenzione! qui cambia il numero di aplotipi (=2*n.inds)
	#print haplo_order
	#print counter
	H1=0
	for x in range(len(counter)):
		H1=H1+((counter[x])*(counter[x]))
	if len(counter)>1:
		H12=H1+2*(counter[0]*counter[1])
	else:
		H12=H1
	H2=H1-(counter[0]*counter[0])
	H21=H2/H1
	c=c+1
	word1= str(c)+"\t"+str(info_tab[K-w/2][0])+"\t"+str(info_tab[K][1])+"\t"+str(info_tab[K-w/2][2])+"\t"+str(info_tab[K+w/2][2])+"\t"+"H1"+"\t"+str(H1)+"\t"+"H2"+"\t"+str(H2)+"\t"+"H12"+"\t"+str(H12)+"\t"+"H21"+"\t"+str(H21)+"\n"
	outfile.write(word1)
outfile.close()
