# TP1 » Introductorio

## RETO I

**_¿Podrías buscar un ejemplo de macromoléculas que almacenen información_**
**_sobre la "identidad" de un organismo dado?_**

Si, las macromoléculas que pueden almacenar información sobre la "identidad"
son los Ácidos nucleicos (AND y ARN).

> Según [Wikipedia » Ácido nucleico](https://es.wikipedia.org/wiki/%C3%81cido_nucleico#Caracter%C3%ADsticas_del_ADN):
>
> Todos los organismos poseen estas biomoléculas que dirigen y controlan la síntesis
> de sus proteínas, proporcionando la información que determina su especificidad y
> características biológicas, ya que contienen las instrucciones necesarias para
> realizar los procesos vitales y son los responsables de todas las funciones
> básicas en el organismo.

## RETO II

**_Proponé una forma de expresar la información contenida en la estructura primaria_**
**_de las proteínas usando tipos de datos de los lenguajes de programación que conocés._**

Dado que la estructura primaria de las proteínas es una cadena de aminoácidos,
podemos representarlas mediante una lista (o _array_) de aminoácidos.

Además, dado que existen 22 tipos de aminoácidos, se pueden representar (en una de sus formas)
mediante una letra que los distingue unívocamente.

Entonces alcanza con generar una lista de _chars_. Y una lista de _chars_
es simplemente un _string_. Con lo cual podemos representar la estructura primaria
de las proteínas como un _string_ de aminoácidos.

## RETO III

**_¿En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?_**

Si no entiendo mal, la estructura terciaria se forma cuando "se conectan"
estructuras secundarias, particularmente _hélices alfa_ con _hojas plegadas_.

Dado este caso, se me ocurre que se podría generar un grafo donde cada nodo
es una estructura secundaria y los vértices del grafo representan las atracciones.

