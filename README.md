# EasySSR: an User-Friendly web application for large-scale batch microsatellite prediction and samples comparison
## Introduction
### Microsatellites
Microsatellites, also known as Simple Sequence Repeats (SSRs) or Short Tandem Repeats (STRs), are polymorphic DNA regions with tandem repetitions of a nucleotide motif ranging 1 - 6 bp, also called mononucleotide, di-, tri-, tetra-, penta- and hexanucleotide repeats (Pinheiro 2022). They can be categorized into perfect, imperfect and compound, and are found in both coding and non-coding regions in eukaryotes, prokaryotes and viruses (Mudunuri 2007, Beier 2017). The SSRs have various clinical implications and a broad range of applications in many fields, such as conservation and evolutionary studies, comparative genomics, molecular biology, biotechnology, oncology, and forensics (Laskar 2022, Pinheiro 2022).

## How to use the web server: Quick Input Tutorial

### Input
Write a ProjectName, a email, input your fasta files. Optional: input your genbank files (must have the same name as correspondent fasta files).
Use the default parameters. Click in Upload. 
![image](https://user-images.githubusercontent.com/101668229/228958608-d12e8ebb-fb25-4b63-8334-b6449bb9fabd.png)
### Execution
Go have coffee while watching some tik toks while waiting for your results.
![image](https://user-images.githubusercontent.com/101668229/228959832-49d9da2b-bf73-4040-8c41-31aca8df7312.png)
### Outputs 

Done! 
- Feel free to click on [download report folder] button to download the IMEX outputs for every genome analyzed, as also the fasta, gbk and ptt used.
- Feel free to interact with the charts, or download them in the format PNG or JPEG.
- Feel free to analyze the tables or downwload them in csv, excel or pdf format.
- Feel free to save the webpage by right-click+save as: Webpage, Complete (*. htm;*html) 
![image](https://user-images.githubusercontent.com/101668229/228960135-5e3a4b98-c687-4724-ad0a-faa44d60469e.png)
![image](https://user-images.githubusercontent.com/101668229/228961192-a507d3fc-94fc-494c-980e-36d2de5c6b89.png)
![image](https://user-images.githubusercontent.com/101668229/228961277-e187e122-15d0-4fa4-9b64-733f2af105c5.png)
![image](https://user-images.githubusercontent.com/101668229/228961334-fc940c09-234a-42f6-88c7-cef5d7c62259.png)
![image](https://user-images.githubusercontent.com/101668229/228961381-9bbd58b9-ba1c-466a-9859-4f1d95bc3b7b.png)


## How to use the web server: Detailed Input tutorial
### User Information
![image](https://user-images.githubusercontent.com/101668229/228953850-6a008dee-f7df-4184-a8ec-e5f5e0235260.png)
Input:
- ProjectName: It can be any word, might be your name, or a project name (e.g. test1) 
- Email: Write a valid email you have acess. Don't worry, easySSR won't send spam or any marketing for you.

E.g: someone with 'Alves' project name and who has an email (email@gmail.com)
![image](https://user-images.githubusercontent.com/101668229/228958251-5de0794e-8215-4c4b-a2cb-8c23a79b212b.png)


### Input files

![image](https://user-images.githubusercontent.com/101668229/228955252-8f236ac2-3477-4b39-856c-ce5ad17e05ef.png)

- In input files, you should upload your fasta files by clicking in the "choose files" button. 
- EasySSR accepts as fasta input files with the filename extensions: ( '.fasta' | '.fna' | '.fa' | '.ffn' )
- You can select as many fasta files you want, with no limit size. 
- Also don't forget to rename your files to have less than 35 characters. 
  - Use intuitive names, because the input name will be the names to appear in the output graphs and tables.
- EasySSR works with draft genomes and complete genomes.
- EasySSR can run with multifasta files, but it will identify each fasta file as a unique genome. 

If you choose to analyze coding/non coding regions, a genbank annotation file will be solicited.

- EasySSR accepts as genbank input files with the filename extensions:  ('.gbk', '.gb', '.gbff)
- Empty genbank files or formats that are not the ones accepted will result in error.


### Default Parameters
The default parameters are based on Pinheiro (2022): 
  - Repeat Number: 1-12, 2-6, 3-4, 4-3, 5-3, and 6-3
  - Imperfection % (p%): 1-10%, 2-10%, 3-10%, 4-10%, 5-10%, 6-10%
  - Mismatch in Pattern: 1-1; 2-1; 3-1; 4-2; 5-2; 6-2
  - Maximum distance for compound SSR: 100 bp;
  - Standardization Level: Level 3; 
  - Flanking Sequences: 15 bp; 
  - Extract all SSR types, 
  - Generate Alignment and Text Output: Yes.

If a user desires to run the default parameters but change something, they should use the custom parameters as done in the following figure.
![image](https://user-images.githubusercontent.com/101668229/228964065-60918c6b-191a-40ee-8eb5-e729e2110a0e.png)

### Custom parameters 

- A) Imperfection Limit/Repeat Unit (mismatches allowed):
  - Imperfection Limit of a repeat size (mono, di, tri, tetra, penta, hexa) is the number of point mutations (substitutions and indels) that can be allowed in a repeat unit (e.g. a trinucleotide [ATC]) so that it can be considered as a match. For example, 2 words ATCATC and ATCATG can be considered as matching repeat units if the imperfection limit (mismatches allowed) for tetranucleotide repeats is set as 1 or more. 

- B) Imperfection Percentage

  - Imperfection percentage of a microsatellite repeat tract is the percentage of mismatches in the entire repeat tract. Imperfection Percentage can be calculated as follows: Imperfection = (No. of imperfections in entire tract / Total No. of Bases in tract) * 100)

- C) Minimum Repeat Number

  - Minimum Repeat Number of a repeat tract is the number of repeat units in a tract so that it can be considered as a valid microsatellite tract. For example, if Mininum Repeat Number for mono is set to 15, means that only the mononucleotide repeat tracts that contain at least 15 nucleotides (total lenght) will be considered as a valid tract. Tracts with less than 15 won't be considered.

- D) Size of Flanking Sequences

  - The program will also extract the sequence located adjacent to each SSR identified in both left and right sides. Flanking regions are important mainly because knowing their sequences enables researchers to isolate the SSR using polymerase chain reaction, or PCR, amplification.

- E) Generate Alignment

  - Alignment will help identifing imperfections.
- F) Generate Text output

  - Imex has their outputs in TXT and HTML. On "Yes" to generate both and off to generate HTML only (Not Adviseable, if off fastSSR might not work.

- G) Identify Coding Regions

  - Do you wish to Identify Coding/No Coding Regions?

- H) dMAX Compound SSR

  - dMAX : Maximum distance between SSRs allowed to consider as a cSSR dMAX is the maximum distance (threshold) between any two SSRs to become a potential Compound SSR. IMEx considers 2 or more SSRs as a single compound SSR if the distance between any two SSRs is less than or equal to the dMAX value set by the user. (-1=Do not extract compound SSR; 0-100 dMAX)


- I) Standardization Level
- 
  - The Microsatellites and Compound Microsatellites in IMEx are standardized according to the following Levels. Higher the standardization, more sensitivity and different patterns will be considered the same SSR. In L0 (level 0) standardization each pattern is unique. In L1 it is considered the circular permutation of the nucleotides in the repeat. In L2, more patterns become equivalent due to its reverse complementation followed by circular permutation. Furthermore, at L3 level in addition to all the SSRs at level 2, more motifs are considered equivalent because of complementation and circular permutation. In the full standardization mode, plenty SSR are considered equivalent as a consequence of motif reversal followed by its circular permutation. (0=N, 1=lvl 1, 2= lvl 2, 3=lvl 3, F = full)")

- J) SSR types to extract

  - 0=Todos, 1=Only mono, 2=Only di ... 6= Only hexa. Advanced users can also search for specific SSR motifs or patterns.

## How to run in Misa-mode
- Put all Mismatches and imperfection parameters to 0, as the following figure.
- ![image](https://user-images.githubusercontent.com/101668229/228966132-8ff74600-ec6d-4ee2-88a1-2c5dce758d06.png)


# FAQ
## Input file not working
### Problems with fasta file

Please verify:
-  If your fasta file is not empty or corrupted
-  If the name of your file has less than 35 characters
-  If your fasta file extension is one of the following: ( '.fasta' | '.fna' | '.fa' | '.ffn' ). EasySSR does not accept: ( '.faa' | '.frn') and other fasta extensions that are not of nucleotides.

### Problems with genbank file

In case you selected the analysis of coding/non coding regions, might have problems with genbank file 
please verify:

-  If your fasta file is not empty or corrupted
-  If the name of your file has less than 35 characters
-  If every genbank annotation file have the same name as the corresponding fasta file. (e.g.: [genome.fasta, genome.gbk] <- correct. [genome.fasta, mygenome.gbk] <- wrong] 
-  If your genbank file extension is one of the following: ('.gbk', '.gb', '.gbff). EasySSR does not accept: ( '.gff'|'.gff3' ) files. 

## Output: Issues with graphs
### Graph for Imperfect SSR empty: 
 - Please check if you used the imperfection parameters with more than 0%. Using 0% in the parameters for imperfect and/or mismatches would result in a analyzis that extracts only perfect SSR, thus not having any imperfect SSR to be shown in the graph. 
### Graph for coding/non coding showing all as non coding:
 - Please verify if you selected the option to analyze coding/non coding. If you didn't select, the alghorithm considers by default all as non coding.
 - Please verify your genbank annotation file. The file might be empty, corrupted or not be in the proper genbank format.  
### Graphs for top 10 SSR comparison empty:
- Please verify your genbank file

## EasySSR is stuck in Step1, Step2 or Step3.
The time of execution depends on the size, complexity and amount of genomes queued, as also on the computational disponibility of the server where the data is processed. It is normal to take seconds, minutes or hours depending on the input. We recommend to perform a test with EasySSR using a a single genome (faster execution) to check if the tool is working properly. If the tools is working properly, it's adviseable to wait until the analysis is done or until an error message appears. Updating your page will stop your processing, and you would have to restart from data upload.
