ann_genes=[]
infile=open("TOTAL_GENES_cluster")
for line in infile:
	line=line.strip()
	ann_genes.append(line)

gene_conversion=[[]*1 for K in range(len(ann_genes))]
ann_stats=[[-1]*1 for K in range(len(ann_genes))]
infile1=open("TOTAL_annotated_cluster.txt")
for line in infile1:
        line=line.strip()
	line=line.split("\t")
	if "e" in line[3]:
		line[3]="0"
	a=ann_genes.index(line[4])
	gene_conversion[a]=line[6]
	if ann_stats[a][0]<abs(float(line[3])):
		ann_stats[a][0]=abs(float(line[3]))

for K in range(len(ann_genes)):
	word="ENTREZID:"+str(gene_conversion[K])
	print word, ann_stats[K][0]

