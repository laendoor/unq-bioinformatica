# TP5 » Alineamiento y BLAST

## RETO I

**_Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema._**
**_Alineá en la tabla interactiva las palabras "BANANA" y "MANZANA"._**
**_¡Tomá nota de tus observaciones y de las conclusiones que se desprendan de estas observaciones!_**

**_PREGUNTAS DISPARADORAS:_**
**_¿Existe una única forma de alinearlas?_**

No, existen múltiples formas de alinearlas

**_¿Es alguno de los posibles alineamientos mejor que otro?_**

Si,

```txt
-BANANA
MANZANA
    xxx
```

Obtiene tres coincidencias, pero

```txt
BANANA-
MANZANA
 xx
```

Obtiene dos coincidencias. Pero luego,

```txt
BAN-ANA
MANZANA
 xx xxx
```

Genera 5 coincidencias.

**_Si así fuera ¿Porqué?_**

Porque según como se ubiquen podemos obtener segmento que coinciden en más letras.