from Bio import SeqIO
import os

#inp = "small_0RS_MESA.fastq"
inter = "small_0RS.tar.gz.dna"
out = "small_0RS_DNA_NOAN"

#fin = open(inp, "r")
#finter = open(inter, "w")
fout = open(out, "w")


#SeqIO.convert(inp,'fastq',inter,'fasta')
#finter.close()



finter = open(inter, "r")

for x in finter:
	if x[0] == '>':
		continue
	else:
		#print(x.strip());
		fout.write(x.strip())
		
fout.close()
# if os.path.exists(inter):
#   os.remove(inter)