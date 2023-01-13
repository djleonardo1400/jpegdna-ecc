#ATTENTION: THIS CODE HAS NOT BEEN TESTED BUT SHOULD BE WORKING

from Chamaeleo.utils.pipelines import TranscodePipeline
from Chamaeleo.methods.flowed import YinYangCode
from Chamaeleo.methods.ecc import ReedSolomon
import dna_bin
import comp_errors
import to_fasta_line
import split

coding_scheme = YinYangCode()
error_correction = ReedSolomon(check_size=16)
needed_index = True

binary = True
read_file_path2 = "images/rd.dna"
read_file_path = "images/rd.bin"
dna_path = "simulation_results/door/rd_ENC_PCT_5.dna_order"
fasta_path = "simulation_results/door/rd_ENC_PCT_5.fasta"
MESA_path = "simulation_results/door/rd_MESA_PCT_5.dna"
dna_path2 = "simulation_results/door/rd_MESA_PCT_5.dna_order"
encoded_oligo_length = 200
write_file_path = "simulation_results/door/rd_MESADEC_PCT_5.bin"
write_file_path2 = "simulation_results/door/rd_MESADEC_PCT_5.dna"
percent_change = 0.5


#dna_bin.dna_to_bin(read_file_path2,read_file_path)

#create encoding pipeline + encoding
pipeline = TranscodePipeline(coding_scheme=coding_scheme, error_correction=error_correction, need_logs=True)

encoded_data = pipeline.transcode(direction="t_c", input_path=read_file_path, output_path=dna_path,
                                  segment_length=120, index=needed_index, index_length=16)

#create the fasta file needed to send to MESA
to_fasta_line.to_fasta_line(dna_path,fasta_path)

#PRESS A KEY ONLY AFTER RECIEVED THE MODIFIED SEQUENCES FROM MESA and naming the file correctly
#use simulator.py to collect the modified dna sequence
input("Press Enter to continue to decoding after retrieving the modified sequencey")

#split the dna sequence into the original number of oligos
split.split_dna(MESA_path,dna_path2,encoded_oligo_length)


#create decoding pipeline + decoding with ecc removal
pipeline = TranscodePipeline(coding_scheme=coding_scheme, error_correction=error_correction, need_logs=True)

decoded_data = pipeline.transcode(direction="t_s", input_path=dna_path2, output_path=write_file_path,
                                  index=needed_index, index_length = 16)

#reconverts to dna if done with binary file
if binary == True:
    dna_bin.bin_to_dna(write_file_path,write_file_path2)
    comp_errors.compare_files(read_file_path2,write_file_path2)
else:
    comp_errors.compare_files(read_file_path,write_file_path)