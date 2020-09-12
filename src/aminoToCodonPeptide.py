import random

# Fuente: https://en.wikipedia.org/wiki/DNA_codon_table
aminoToCodonDict = {
  'A': ['GCA', 'GCC', 'GCG', 'GCT'],               # Ala
  'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], # Arg
  'N': ['AAT', 'AAC'],                             # Asn
  'D': ['GAT', 'GAC'],                             # Asp
  'C': ['TGT', 'TGC'],                             # Cys
  'Q': ['CAA', 'CAG'],                             # Gln
  'E': ['GAA', 'GAG'],                             # Glu
  'G': ['GGT', 'GGC', 'GGA', 'GGG'],               # Gly
  'H': ['CAT', 'CAC'],                             # His
  'I': ['AUU', 'AUC', 'AUA'],                      # Ile
  'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], # Leu
  'K': ['AAA', 'AAG'],                             # Lys
  'M': ['AUG'],                                    # Met
  'F': ['TTT', 'TTC'],                             # Phe
  'P': ['CCT', 'CCC', 'CCA', 'CCG'],               # Pro
  'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], # Ser
  'T': ['ACT', 'ACC', 'ACA', 'ACG'],               # Thr
  'W': ['TGG'],                                    # Trp
  'Y': ['TAT', 'TAC'],                             # Tyr
  'V': ['GTT', 'GTC', 'GTA', 'GTG'],               # Val
}

def aminoToCodon(amino):
  return random.choice(aminoToCodonDict[amino])

def peptideToARN(peptide):
  return ''.join(map(aminoToCodon, peptide))

# Run
arn = peptideToARN('ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA')
print (arn)
