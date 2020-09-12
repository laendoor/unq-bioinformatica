# TP3 » El juego de la vida

## RETO I

**_Enumerá las diferencias que existen entre una célula procariota y eucariota._**

* Células Eucariotas
  - Son considerablemente más grandes que las Procariotas
  - Poseen un Núcleo bien definido
  - Tienen cromosomas lineales
  - El núcleo está rodeado por una membrana
  - El proceso de transcripción y traducción del ADN ocurre de manera separada
  - Tienen un sistema de endomembrana y otras organelas (lisosomas, peroxisomas, mitocondrias, cloroplastos, vacuolas)
  - Pueden reproducirse tanto de manera sexual como asexual
  - Generan división por mitosis
  - Tienen complejos proteicos (tubulina, actina)
  - Tienen un citoesqueleto
* Células Procariotas
  - Son mucho más pequeñas que las Eucariotas
  - No poseen un núcleo definido
  - Tienen cromosomas circulares
  - Hay ausencia de membrana que defina el espacio y la organización
  - Los procesos de transcripción y traducción ocurren de manera simultánea
  - Solo permiten reproducción asexual
  - Generan división por fisión binaria

## RETO II

**_Dado el código genético como se muestra en la tabla_**
**_Crea un programa sencillo en algún lenguaje de programación que conozcas que imprima una cadena_**
**_de ARN codificante para el siguiente péptido (cadena corta de aminoácidos)_**

> Sec1: 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

```py
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
```
