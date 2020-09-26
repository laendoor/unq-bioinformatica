# TP4 » ¿En qué se parecen una gallina y una mosca?

## Tabla Citocromo C

| Secuencia      | Nombre taxonómico        | Nombre común          |
|----------------|--------------------------|-----------------------|
| NP_061820.1    | Homo sapiens             | Humano                |
| NP_001072946.1 | Gallus gallus            | Gallo                 |
| NP_001065289.1 | Pan troglodytes          | Chimpancé común       |
| NP_001157486.1 | Equus caballus           | Caballo               |
| NP_001183974.1 | Canis lupus familiaris   | Perro                 |
| AEP27192.1     | Gorilla gorilla          | Gorila occidental     |
| XP_024245566.1 | Oncorhynchus tshawytscha | Salmón real           |
| NP_001086101.1 | Xenopus laevis           | Rana de uñas africana |
| NP_477164.1    | Drosophila melanogaster  | Mosca de la fruta     |

**_¿Cuán sencillo será alinear dos o más secuencias a mano?_**
**_¿Cuánto influirán el número de secuencias a alinear, su longitud, y la similitud entre ellas?_**

A partir de las secuencias en formato FAST no es que sea complicado en sí
sino que es sumamente tedioso. Las secuencias son muy largas e ir alineándolas
para encontrar la mejor coincidencia puede requerir probar un número
muy grande de combinaciones.

Por supuesto que mientras sean más parecidas es más sencillo, dado que
si difieren mucho quizás haya que ir agregando _gaps_ cuando un aminoácido
no esté en la misma columna en la otra secuencia.

**_¿Son parecidos los citocromos c de humano y gallo?_**

Tienen cierta similitud dado que coinciden en un 90% de aminoácidos alineados.

**_¿Qué teorías subyacen a este análisis?_**

Se supone que esto se da porque el humano y el gallo comparten algún ancestro en común.

**_¿Cómo nos ayuda la evolución a explicar sus similitudes y diferencias?_**

Supongo que conocer las familias evolutivas debe tener un correlato con los porcentajes
de similitudes y diferencias entre las proteínas de las distintas especies.

**_Podemos elegir verlo en colores (Show Color). ¿Qué indican los colores?_**

Los colores indican las propiedades físico-químicas de un sub-segmento.
Cuando coinciden los colores es porque ese sub-segmento de aminoácidos
tienen similitudes, aunque no coincidan exactamente los mismos aminoácidos en ese segmento.

**_¿Qué indican el guión (-), los dos puntos (:) y el asterisco (*)?_**

Los guiones (-) indican que en esa columna, ese aminoácido falta en esa posición
con respecto a la misma posición en la otra proteína.

El asterisco (*) indica que en ese segmento hay un porcentaje total de coincidencia.

Los dos puntos (:) parecieran indicar que hay una diferencia en el aminoácido
con respecto a la cadena de referencia.

**_A simple vista, ¿se conserva la secuencia del citocromo c en los organismos?_**

Pareciera que se conserva en un porcentaje relativamente alto, pero se encuentran diferencias.

**_¿Creeríamos que todos los organismos se asemejan por igual al resto, o se pueden identificar grupos de mayor similitud? Si es así, ¿tienen sentido?_**

Pareciera que existen grupos de mayor similitud. Tiene sentido dado que pareciera
ser de especies que están más cerca en el árbol evolutivo, como ser el _homo sapiens_
y el _Pan troglodytes_, que son especies que "están cerca" en la evolución.

**_¿Qué evidencias nos aportaría este análisis, a la luz de la evolución?_**

Justamente podría ayudarnos a conocer cuan "cerca" o "lejos" están dos especies.
O sea, si comparten altos porcentajes de proteínas se podría suponer que son especies
que están cerca evolutivamente.

**_A juzgar por los organismos participantes, ¿cuáles creería que deberían estar más_**
**_agrupados en el árbol filogenético?_**

Uno esperaría que el Homo sapiens (Humano) esté agrupado con el Pan troglodytes (Chimpancé)
y el Gorilla gorilla (Gorilla).

Además es de esperar también que Oncorhynchus tshawytscha (Salmón) esté
agrupado con el Xenopus laevis (Rana) por ser anfibios.

**_Observemos el árbol filogenético. ¿Concuerda con lo esperado?_**
**_¿De qué organismos son los citocromos c más parecidos? ¿Cómo se explica?_**

Sí, concuera. Se puede notar el agrupamiento de Humano-Chimpacé-Gorilla
como también el de Salmón-Rana, aunque en este último se suma el
Gallus gallus (Gallo), lo cual en principio no resulta muy intuitivo.

De todas formas esto se explica porque el citocromos c es una proteína
que se encarga de la respiración celular, y tiene sentido que sea una proteína
que no haya variado tanto entre especies.
