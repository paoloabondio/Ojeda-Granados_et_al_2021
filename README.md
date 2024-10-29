# Ojeda-Granados_et_al_2021
Ad hoc Python scripts used in Ojeda-Granados et al. 2021

1) The script H12_calculation.py takes as input FOUR externally provided arguments:
 - input file name
 - window size
 - shift (or step) size
 - population name

as exemplified by the following command line:
python H12_calculation.py space_separated_chromosome_file.txt 200000 50000 TAR.


The input file for this script is a space-separated text file for an entire chromosome, containing as many lines as there are SNPs and FIVE columns with:
- chromosome number
- physical position
- variant ID
- ancestral allele
- derived allele
  
After these five columns, there are 2*N columns (representing the number of chromosome copies in the studied population, that is two chromosome copies for each individual) containing binary indication of phased alleles, where 0 represents the ANCESTRAL state and 1 represents the DERIVED state. This file can be simply obtained by modifying a phased vcf file or the outcome of a SHAPEIT-based phase reconstruction.

The output of this script is a table with 13 columns, that has to be modified by adding a last column of ANCESTRAL allele frequency in order to apply the stat_normalization.py script.

2) The script stat_normalization.py takes as input the modified output obtained at point 1, and computes a 100-frequency-bin based normalization of H12 results (the script can be easily modified to compute normalization of other H statistics from the same file). The output is the same file as the input, with an extra column added to report the normalized score.
