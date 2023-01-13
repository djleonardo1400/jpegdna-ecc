#need to run that at beginning of each session
#cd /Users/leonardopanattoni/Downloads/JPEG-DNA-BC-Transcoder-main;
#python3 setupWrapper.py build_ext --inplace
#also remember the subsampling numbers on encoding to be able to decode back

#encode an image
#python -m jpegdna.scripts.jpegdnargb_encode /Users/leonardopanattoni/Downloads/Chamaeleo-master/kodim13.jpg /Users/leonardopanattoni/Downloads/Chamaeleo-master/kodim13.dna


#decode an image
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_PCT_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_PCT_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_PCT_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_PCT_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_PCT_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_PCT_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_PCT_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_PCT_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_PCT_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_PCT_5.png;

python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_5.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/door/rd_ALTDEC_RS8_6.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/rd_ALTDEC_RS8_6.png;


python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_PCT_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_PCT_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_PCT_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_PCT_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_PCT_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_PCT_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_PCT_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_PCT_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_PCT_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_PCT_5.png;

python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_5.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:2:0 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/water/wt_ALTDEC_RS8_6.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/wt_ALTDEC_RS8_6.png;

python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_PCT_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_PCT_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_PCT_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_PCT_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_PCT_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_PCT_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_PCT_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_PCT_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_PCT_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_PCT_5.png;

python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_1.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_1.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_2.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_2.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_3.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_3.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_4.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_4.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_5.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_5.png;
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/parrots_crop/pc_ALTDEC_RS8_6.dna /Users/leonardopanattoni/Downloads/Chamaeleo-master/simulation_results/dec_img/pc_ALTDEC_RS8_6.png;

