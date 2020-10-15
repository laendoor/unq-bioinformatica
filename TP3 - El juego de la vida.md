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

## RETO III

**_En muchos de los genes codificados en el ADN existe un motivo recurrente ubicado_**
**_antes de la secuencia codificante del gen que direcciona la unión de la_**
**_ARN Polimerasa II, la proteína encargada de copiar el ADN a un ARN mensajero._**
**_Ésta secuencia denominada caja TATA (consistente en una secuencia de nucleótidos 'TATAAA')_**
**_se encuentra presente en lo que se denomina región promotora de diversos genes,_**
**_en organismos de todos los reinos (Smaleand Kadonaga 2003; Lifton  et al. 1978)._**

**_Crea un programa sencillo en algún lenguaje de programación que conozcas que permita_**
**_identificar las regiones promotoras de un gen, en una secuencia dada de ADN,_**
**_considerando que tal región comienza y termina con la caja TATA._**

```py
def genesFromTATA(adnSequence):
  return list(filter(None, adnSequence.split('TATAAA')))
```

## RETO VI

**_Existen numerosas herramientas muy fáciles de usar que te permiten crear videojuegos,_**
**_como por ejemplo PilasEngine y no hay mejor modo de aprender que jugando!_**

**_Diseñá un juego de mesa o un videojuego (hecho con la herramienta que más te guste)_**
**_temático sobre expresión génica, con sus reglas y resúmen. Tené en cuenta que lo vas_**
**_a tener que compartir con la clase. ¡El cielo es límite, a divertirse!_**

[Repo del Juego](https://github.com/unq-bio-dilosaba/rna-proteins-game)
