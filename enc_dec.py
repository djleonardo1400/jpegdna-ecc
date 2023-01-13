from Chamaeleo.utils.pipelines import TranscodePipeline
from Chamaeleo.methods.flowed import YinYangCode
from Chamaeleo.methods.ecc import ReedSolomon
import dna_bin
import random_change
import comp_errors

coding_scheme = YinYangCode()
error_correction = ReedSolomon(check_size=64)
needed_index = True

binary = True
read_file_path2 = "images/rd.dna"
read_file_path = "images/rd.bin"
dna_path = "simulation_results/door/rd_ENC_PCT_5.dna_order"
dna_path2 = "simulation_results/door/rd_ALT_PCT_5.dna_order"
write_file_path = "simulation_results/door/rd_ALTDEC_PCT_5.bin"
write_file_path2 = "simulation_results/door/rd_ALTDEC_PCT_5.dna"
percent_change = 0.5
dna_bin.dna_to_bin(read_file_path2,read_file_path)

#create encoding pipeline + encoding
pipeline = TranscodePipeline(coding_scheme=coding_scheme, error_correction=error_correction, need_logs=True)

encoded_data = pipeline.transcode(direction="t_c", input_path=read_file_path, output_path=dna_path,
                                  segment_length=120, index=needed_index, index_length=16)


#apply alteration of nucleotides
random_change.random_change(dna_path,dna_path2,percent_change)


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