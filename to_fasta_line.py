#takes a file with several oligos (.dna_order) and formats it
#to FASTA, format used when simulating with MESA
def to_fasta_line(file_in,file_out):
    i = 0
    fout = open(file_out, 'w')
    with open(file_in) as file:
        for line in file:
            i += 1
            seq = line.rstrip()
            fast_str = ""
            fast_str += '> oligo ' + str(i) + '\n'
            fast_str += seq
            fast_str += "\n"
            fout.write(fast_str)