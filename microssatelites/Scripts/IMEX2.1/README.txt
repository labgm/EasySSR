IMEx: Imperfect Microsatellite Extractor README, Last Updated April 2017.
Version: 2.1
Authors: Suresh B. Mudunuri (sureshverma@gmail.com) and H.A.Nagarajaram (nagarajaram@gmail.com)

Imperfect Microsatellite Extractor (IMEx) is a tool for extracting perfect,imperfect as well as 
compound Microsatelites or Simple Sequence Repeats (SSR's) or Short Tandem Repeats (STR's) 
from genome sequences.  

IMEx 2.1 / G-IMEx IMPROVEMENTS FROM EARLIER VERSION
-------------------------

* Works in latest Linux OS Versions
* Graphical and non-graphical user interfaces added
* Compound SSR Extraction module added
* 4 levels of SSR and cSSR Standardization added
* Statistics and Summary of SSR and cSSRs in Output
* Extracting a particular size SSRs and cSSRs(Mono, di, tri...)
* More user-friendly and better interface
* Robust
* Ability to run IMEx in batch mode
* Better output display
* Improved navigation in HTML output files
* No need of Perl s/w 

To learn more about the program, please see:
http://www.cdfd.org.in/imex

Running the program is done by a simple command:

./imex (non-graphical mode)
./gimex (graphical mode)

The program will inturn asks for inputs from the user such as input sequence file (fasta file), 
parameters and other.

For your convenience, a genome file of E.coli (NC_000913.fna) and its corresponding protein table file (NC_000913.ptt) are included.

This file describes the installation and usage of the IMEx program for the detection of microsatellite repeats. 
Please send comments, suggestions or bug reports to the authors.

IMEx INSTALLATION
-------------------------

1. Download the latest version of IMEx zip file and unpack it.

#unzip IMEx2.1
#cd IMEX2.1

2. Make sure the following softwares and programming environments are installed in your
system.

   a)gcc version (3.4 or above)
   b)Web-browser software (Firefox,IE,opera etc)
   c)Java (for using graphical user interface)(version 1.6 or above)

INSTRUCTIONS TO RUN Non-Graphical IMEx
---------------------------------------

Syntax of using IMEx over command line:

./imex


To run the program in batch mode:

 ./imex_batch <filename> <mismatches allowed in 6 types> <imperfection % of 6 types> <repeat numbers of 6 types> <flanking sequence length> <align_flag> <text_flag> <coding_flag> <compound_flag> <standardization level> <repsize_flag> [coding_file]

* coding_file is an optional argument for checking whether a microsatellite falls in coding/region or not. If you are not using coding argument, please make sure that coding_flag is set to 0.

Example: ./imex_batch NC_000913.fna 1 1 1 2 2 3 10 10 10 10 10 10 10 5 4 3 2 2 10 1 1 0 10 3 0

Explaination of arguments:

<filename>  
          Name / path of the file Eg: sample.txt, /home/suresh/atrophin.fasta, NC_000913.fna etc

<mismatches allowed in 6 types>
          Number of mismatches allowed in each repeat type. The repeat number range can be 0-n where n is the size of the repeat. Eg. 1 1 1 2 2 3 means only one mismatch is allowed per pattern for mono, di and trinucleotide repeats and two mismatches for tetra and penta and 3 mismatches for hexa repeats. 
 
<imperfection % of 6 types> 
          Imperfection percentages allowed in each repeat type. The imperfection % can be between 0-50 where 0 is for finding perfect repeats (without mismatches). Eg. 10 10 10 10 10 15 means 10% of imperfection is allowed for mono, di, tri, tetra and penta repeats and 15 % imperfection for hexa repeats.

<repeat numbers of 6 types>
          Number of repeat units in each repeat type. The minimum repeat number of any repeat is 2. Eg. 15 10 7 5 3 2 means the program picks up mono repeats which are repeated atleast 15 times, di-nucleotide repeats which are repeated atleast 10 times, tri, tetra, penta, hexa repeats which are repeated atleast 7, 5, 3, 2 times respectively.

<flanking sequence length> 
          The number of nucleotides before and after the repeat tract. The flanking sequence is displayed along with the alignments generated.Eg. 10 means a flanking sequence of length 10 nucleotides is displayed.

<align_flag> 
          To indicate whether alignments should be generated or not. Eg. 1 indicates that alignments should be generated where as 0 indicates no generation of alignments.

<text_flag>
          To indicate whether text format of output should be generated or not. Eg. 1 indicates that output should also be generated in text format also where as 0 indicates output should be generated in HTML format only.

<coding_flag>
          To indicate whether text format of output should be generated or not. Eg. 1 indicates that output should also be generated in text format also where as 0 indicates output should be generated in HTML format only.

<compound_flag>
          To indicate whether Compound Microsatellites (cSSRs) should be extracted or not. Eg. -1 indicates cSSR extraction not required where as number 0-50 indicates the min. distance between any two SSRs to be considered as a cSSR.

<standardization level>
          To indicate the standardization level for extracting SSR and cSSR occurrence statistics. Eg. 0 indicates 'NO Standardization', 1 indicates 'Level 1 Standardization', 2 indicates 'Level 2 Standardization', 3 indicates 'Full / Complete Standardization',.
          * For detailed information about standardization levels, please look in glossary @ http://www.cdfd.org.in/imex

<repsize_flag>
          To indicate a particular repeat size (1-6) when you dont want to extract all size repeats . Eg. 0 indicates all sizes where as 1 indicates extracting only mono, 2 for di, 3 for tri etc .

[coding_file]
          Name / path of the protein table file (ptt file) Eg: sample.ptt, /home/suresh/atrophin.ptt, NC_000913.ptt etc
	  Should be supplied if the coding flag is set to 1. Used for getting info whether the repeat falls in coding region or non-coding region. 
          To get ptt files for your genome sequence, please download them from NCBI.

Eg../imex_batch NC_000913.fna 1 1 1 2 2 3 10 10 10 10 10 10 10 5 4 3 2 2 10 1 1 1 -1 2 0 NC_000913.ptt

*PTT files are available for all bacterial genomes, fungus and many other organisms and can be downloaded from NCBI ftp website. If you want coding info, please make sure that the code flag is turned to 1 along with giving the xxx.ptt file as argument.

The current version is for use on Linux system only.

If any errors or bugs or suggestions, please do mail to the authors


-IMEx Development Team 
