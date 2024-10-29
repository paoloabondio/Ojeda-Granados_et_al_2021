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
