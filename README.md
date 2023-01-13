<p float="left">
<img src="./images/logos.png" width="350">
</p>

# Error correction on JPEG transcoding for DNA based storage
## Master Semester Project - École Polytechnique Fédérale de Lausanne, Microengineering section
### By Leonardo Panattoni - Supervisors: Prof. Dr. Touradj Ebrahimi and Davi Lazzarotto

The goal of this project is, firstly, to study the relevant state of the art in DNA storage and coding. The next point is to integrate an existing JPEG to DNA image transcoder with a DNA synthesis, storage and sequencing simulator and analyse the performance of that framework. As final objective, error correcting codes are implemented to attenuate or cancel the effect of the simulated errors. <br> <br>

Note: the error simulator ([MESA](https://mesa.mosla.de)) has stopped working when developping this code so an alternative simpler selfmade script, *random_change.py*, has been created. The following code has been tested with this alternative instead.

## Installation
To install the required packages and set up the transcoder you need to have *pip* and *homebrew* installed.  Python 3.10.6 was used. For Apple Silicon chips, it is needed to run the terminal using Rosetta because the installation will not work otherwise.

#### First, we install all required packages:
To install them, use the following command at the root of the repository’s folder:
```
pip install -r requirements.txt
```

#### Then, we set up the JPEG_DNA_Transcoder:
To install it, use the following command under the */JPEG-DNA-BC-Transcoder-main directory*:
```
python setup.py install
```
#### Then we set up the Python wrapper for the *ibjpeg* C library:
```
brew install libjpeg
```
Please update the include and lib paths in *setupWrapper.py* such that they point to your installation. 
```python
libjpeg_include_dir = "path/to/libjpeg/build/include"
libjpeg_lib_dir = "path/to/libjpeg/build/lib"
```
Tip: Run the following command in order to find the path to *libjpeg*:
```
brew info libjpeg
```

Finally, to compile the extension for use in the project’s root directory, run the following in the
root of the */Jpeg_DNA_Transcoder* directory: 
```
python setupWrapper.py build_ext −−inplace
```
This last command needs to be done each time we close the terminal.

Now, we can install the code to retrieve the modified sequences from MESA. To do so, code from Romain Graux master thesis was used. Be careful, this code does not work on Apple silicon chips (even using Rosetta). The code was slightly edited to make it work on a Windows computer, so you can simply go in the right folder from this project’s repository, which is simulator. For Intel based Mac users, it is better to download the original [*utils.py*](https://github.com/romaingrx/dna-pcc-master-thesis/blob/master/compression/dna/codec/utils.py) file from R. Graux and overwrite it over the delivered version. Now, go to *config/simulator/post/nosim.yaml* and edit the *key:* parameter with your personal MESA API key. If you are not using Windows, also replace the "\\\\" with "/" in *config/simulator/default.yaml*.
<br><br>

Now all the packages are installed and the code is ready to be run.

## Example on how to run the code
First, we need to use the transcoder to have our dna sequence. To do so, run:
```
python -m jpegdna.scripts.jpegdnargb_encode $IMG_PATH.jpg $DNA_OUT_PATH.dna
```
with the wanted directory for the image to encode and .dna file. Also remember the subsampling coefficients printed, they will be used in the decoding. Let us assume 4:4:4 was printed in this case. <br> <br>

Now, we can directly open the *enc_dec.py* file and edit the following lines as wanted
```
coding_scheme = YinYangCode()
error_correction = ReedSolomon(check_size=16)
needed_index = True

binary = True
read_file_path2 = "image.dna"
read_file_path = "image.bin"
dna_path = "encoded_dna.dna_order"
dna_path2 = "altered_dna.dna_order"
write_file_path = "decoded_dna.bin"
write_file_path2 = "decoded_dna.dna"
percent_change = 0.5
```
We can for example set check_size = 16 and edit all the files path to correspond to our
needs. We can also change the percent_change value of course.<br>

Once all this is done, simply run:
```
python enc_dec.py 
```
the code will do everything on its own. When it is done, it will print how many errors are still present after decoding. <br><br>

Now, the last task is to use the transcoder again to decode the dna sequence that as been outputted from the previous code (write_file_path2). To do so, in the transcoder code directory, run:
```
python -m jpegdna.scripts.jpegdnargb_decode 4:4:4 $DNA_PATH.dna $DEC_IMG.png
```
Here 4:4:4 is the subsampling coefficients that were given in the image encoding but this has to be changed accordingly to what is given in the image encoding. <br> <br>

Now that we have our png, we have gone through the whole pipeline and if now errors remained from the error correction step, we should get the same image as what was initially inputted.

## Credits:
The JPEG DNA transcoder software is a work of L. Secilmis and can be found on his [github](https://github.com/lukasec/JPEG-DNA-BC-Transcoder). Check its LICENSE.md document in the root of this project for additional infos. 
<br>
Code in */simulator* originally comes from R. Graux from his master project. It can be found on his [github](https://github.com/romaingrx/dna-pcc-master-thesis/tree/master/compression/dna/codec).<br>
Chamaeleo code can be found [here](https://github.com/ntpz870817/Chamaeleo)