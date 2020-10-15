# TP5 » Alineamiento y BLAST

## PARA PENSAR

**_¿Qué tipo de información se puede extraer de la comparación de secuencias?_**
**_¿Cómo esperás que se vea en una comparación?_**

Se puede, en principio, conocer las similitudes y diferencias de nucleótidos
o aminoácidos de las secuencias. Se espera que contengan segmentos en común
pero con otros que difieran.

## PARA PENSAR

**_¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas?_**

Porque en las secuencias de ácidos nucléicos puede pasar que un cambio
en un nucléotido de todas formas siga formando la misma proteína dado que existen
varios codones que forman los mismos aminoácidos.

## RETO I

**_Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema._**
**_Alineá en la tabla interactiva las palabras "BANANA" y "MANZANA"._**
**_¡Tomá nota de tus observaciones y de las conclusiones que se desprendan de estas observaciones!_**

Si alineamos ambas palabras a izquierda se generan pocas similitudes.
Alinear a derecha ambas genera un poco más. En cambio meter un gap en el medio
(`BAN-ANA`) genera mayores coincidencias.

### PREGUNTAS DISPARADORAS

**_¿Existe una única forma de alinearlas?_**

No, existen múltiples formas de alinearlas

**_¿Es alguno de los posibles alineamientos mejor que otro?_**

Si,

```txt
-BANANA
MANZANA
xxxxooo
```

Obtiene tres coincidencias, pero

```txt
BANANA-
MANZANA
xooxxxx
```

Obtiene dos coincidencias. Pero luego,

```txt
BAN-ANA
MANZANA
xooxooo
```

Genera 5 coincidencias.

**_Si así fuera ¿Porqué?_**

Porque según como se ubiquen podemos obtener segmento que coinciden en más letras.

## RETO II

**_En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA"._**
**_Verás que en el margen superior izquierdo aparece un valor de identidad calculado_**
**_para cada alineamiento que intentes._**
**_¡Tomá nota de los valores de identidad observados y de las conclusiones que se_**
**_desprendan de estas observaciones!_**

Alinear ambas a izquierda genera una identidad de `0.6`, lo mismo
que alinear ambas a derecha. Centrarlas genera identidad de `0.0`.
No es posible llegar a una identidad de `1.0` dado que difieren en
la longitud de la cadena.

### PREGUNTAS DISPARADORAS

**_¿Son todos los valores iguales?_**

No, distintos alineamientos generan distintos valores de identidad.

**_¿Qué consideraciones deberían tenerse en cuenta a la hora de realizar el cálculo?_**

Sería interesante, además de alinear para generar mayor identidad,
respetar el significado de "las palabras". No es lo mismo "ANA" que "A-N-A"
porque esos _gaps_ indicarían que estaría faltando información que podría
modificar el sentido de la cadena.

**_¿Se te ocurre, distintas formas de calcularlo?_**

Se podría penalizar el hecho de meter _gaps_ "en el medio".

**_¿Serán todas ellas igualmente válidas en Biología?_**

Probablemente no, habría que analizar qué alineamientos y por ende identidades
tendrían más sentido según, por ejemplo, observaciones pre-existentes.

## RETO III

**_En la siguiente tabla probá distintos alineamientos para las palabras "ANA" y "ANANA"._**
**_Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada_**
**_alineamiento que intentes y un botón para cambiar la penalidad que se le otorga a dicho_**
**_para el cálculo de identidad._**
**_¡Probá varias combinaciones, tomá nota de los valores de identidad observados y_**
**_de las conclusiones que se desprendan de estas observaciones!_**

### PREGUNTAS DISPARADORAS

**_¿Cómo se relacionan los valores de identidad obtenidos con las penalizaciones que se imponen al gap?_**

La penalidad multiplica las disidencias disminuyendo el valor de la identidad geométricamente.
Una identidad de `0.6` y penalidad `1` se convierte en una identidad de `0.4`.
Si la penalidad sube a `2` la identidad baja a `0.2`.

**_¿Qué implicancias crees que tiene una mayor penalización de gaps?_**

A mayor penalidad de disidencias es menor el valor de identidad obtenido, osea
que generar penas más altas conlleva a definir que los _gaps_ son cada vez "más malos".

**_¿Se te ocurre alguna otra forma de penalización que no haya sido tenido en cuenta en este ejemplo?_**

Se me ocurre que podría penalizarse más dos _gaps_ contingüos a dos _gaps_ que estén
separados por una coincidencia.

### PARA PENSAR

**_Entonces, pensando en un alineamiento de ácidos nucleicos_**
**_¿Cuáles te parece que son las implicancias de abrir un gap en el alineamiento?_**

Entiendo que el hecho de tener que "partir" mediante un _gap_ implicaría
o bien que en la secuencia no se pudo observar un aminoácido o bien
que son secuencias muy distintas pero con el _gap_ se "está forzando" a que coincidan.

**_¿Qué implicaría la inserción o deleción de una región de más de un residuo?_**

Puede que esté indicando que esa inserción o deleción se debió a una mutación en la secuencia.

## RETO IV

**_En la siguiente tabla probá distintos alineamientos para las secuencias nucleotídicas._**
**_Podrás ver las traducciones para cada secuencia._**
**_¡Probá varias combinaciones, tomá nota de las observaciones y de las conclusiones que se desprendan de estas!_**

### PARA PENSAR

**_¿Dá lo mismo si el gap que introducís cae en la primera, segunda o tercer posición del codón?_**

No, no es lo mismo en donde se introduce el _gap_ porque, amén de la identidad, cambiar la posición
del _gap_ genera que se pueda o no determinar el aminoácido que se genera a partir del cada codón formado
según el alineamiento.

Por ejemplo, en `TGCGAGG`, alinearlo como `TGC-GAGG-` permite determinar solo el primer aminoácido (`C--`).
Pero alinearlo `TGCGAGG--` permite determinar el primer y segundo aminoácido (`CE-`).

**_¿Cómo ponderarías las observaciones de este ejercicio para evaluar el parecido entre dos secuencias?_**

Determinaría el valor de identidad no solo por las coincidencias de la secuencia sino también por la
cantidad  de aminoácidos que se puedan identificar pero también por la coincidencia de esos aminoácidos.

## RETO V

**_Estuvimos viendo que el alineamiento de secuencias no es trivial y requiere contemplar_**
**_los múltiples caminos posibles, teniendo en cuenta al mismo tiempo la información biológica_**
**_que restringe ese universo de posibilidades._**
**_¡Es momento de llevar entonces estos conceptos a lo concreto!_**

**_Te proponemos pensar los pasos a seguir en un alineamiento de dos secuencias cortas,_**
**_teniendo en cuenta una matriz genérica de scoring (puntuación) que contemple las_**
**_complejidades que estuvimos viendo, es decir que penalice de distinto modo una inserción_**
**_o deleción, una discordancia (mismatch) o una coincidencia (match)._**
**_Escribilos o esquematizalos en un diagrama de flujo._**

```txt
|   |  A |  B |  C  | - |
| A | +1 | -1 | -2  | 0 |
| B | -1 | +1 | -1  | 0 |
| C | -2 | -1 | +1  | 0 |
```

Alinear `ABC` con `AB`.

Caso 1:

```txt
 A B C
 A B -
+1+1+0
```

```txt
 A B C
 A - B
+1+0-1
```

```txt
 A B C
 - A B
+0-1-1
```

### PARA PENSAR

**_¿En qué consiste la programación dinámica? ¿Porqué crees que es útil en este caso?_**

a programación dinámica te permite fundamentalmente recordar cálculos costoso de manera
de no tener que volver a usar tiempo de cómputo cada vez, sino que al encontrar una comparación
que ya fue comparada previamente, se puede volver a utilizar ese valor en vez de tener que volver
a generar todo el procesamiento de cómputo para el cálculo.

Creo que puede ser sobre todo en comparaciones de cadenas locales, ya que al encontrar
otro segmento similar a uno ya calculado, no hace falta volver a generar el scoring sino
que se podría utilizar el scoring previo calculado para otra cadena.

## RETO VI

**_Utilizando la herramienta interactiva desarrollada por el Grupo de Bioinformática de Freiburg_**
**_probá distintos Gap penalties para el ejemplo propuesto y observá lo que ocurre._**
**_Interpretando la recursión, explicá con tus palabras de dónde salen los valores de la matriz_**
**_que se construye. ¡Esquematiza tus conclusiones!_**

Los valores de la matriz salen de calcular 

### PARA PENSAR

**_¿En qué casos serán de utilidad uno u otro tipo de alineamientos?_**
**_¿Qué limitaciones tendrá cada uno?_**
