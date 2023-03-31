# gbk2ptt
Converts a GenBank file (*.gbk) to an NCBI Protein Table (*.ptt) file

*Note: This repository contains all the code to run on a webserver. If running locally, you only need the GBKtoPTT.pl file.*

### Requirements
* Perl (ActivePerl for Windows may work)
* BioPerl

### How to Run
```bash
perl GBKtoPTT.pl < [yourgbkfile.gbk] > [yourdesiredoutputfile.ptt]
```

### Acknowledgements
GBKtoPTT.pl was written by Torsten Seemann
- https://tseemann.github.io/
- https://github.com/tseemann
