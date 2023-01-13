import textwrap

#converts a single dna string into several oligos of fixed length
#o_length should be the oligo length of the YYC + RS encoded dna
def split_dna(file_in,file_out,o_length):
    fout = open(file_out, "w")
    with open(file_in, "r") as fd:
            x = fd.read()
            xlist = textwrap.wrap(x,o_length)
            for item in xlist:
                fout.write("%s\n" % item)
    fout.close()