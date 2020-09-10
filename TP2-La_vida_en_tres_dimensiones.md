# TP1 » La vida en tres dimensiones

**_¿Por qué una célula querría destruir sus propias proteínas?_**

Se pueden haber sintetizado proteínas para un función especifica durante
un período de tiempo y luego de haber cumplido su función ya no son necesarias.

**_¿Qué información nos provee esta página?_**

PDB provee distintas representaciones terciarias de todas las macromoléculas que se pudieron medir.

Particularmente la página de la _ubiquitina_ muestra:

- Clasificación
- Organismo de la proteína
- Fecha de carga de la información
- Autores
- Información del experimento:
  * Método con el cual se obtuvo
  * Resolución
  * Valor de R observado

**_¿Cómo se determinó la estructura de esta proteína?_**

Se utilizó el método de Difracción de Rayos-X.

**_A la izquierda vemos una representación de la estructura de ubiquitina._**
**_¿Qué significan las cintas, las flechas y las regiones angostas?_**

Las cintas, las flechas y las regiones angostas representan cada uno de los aminoácidos
que conforman la proteína.

**_¿Representa esa imagen a la realidad del sistema biológico?_**

No, es un modelo que permite observar distintas características.

**_La estructura 1UBQ fue "refinada a una resolución de 1.8 Angstroms"._**
**_Éste es el error asociado al experimento: mientras mayor es la resolución,_**
**_menor es la certeza al determinar la posición de cada átomo._**
**_¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?_**

El conocer el error en mediciones o experimentos científicos permite analizar
los datos obtenidos con un mejor nivel de certeza. Aunque suene paradójico,
el hecho de conocer el error en la medición permite saber que el dato + el error
brinda información concreta sobre el dato. Por ejemplo, si medimos que una determinada
molécula se encuentra (a nivel espacial) en la coordenada `(1, 2, 2)` con un margen
de error de `(0.1, 0.2, 0.03)` eso nos permite asegurar que la molécula va a estar
(con total seguridad) en algún lugar en el espacio que se forma entre
`(0.9, 1.8, 1.97)` y `(1.1, 2.2, 2.03)`.

**_En la pantalla principal vemos una representación de la estructura de ubiquitina._**
**_¿Qué significan las cintas, las flechas y las regiones angostas?_**

Las cintas, las flechas y las regiones angostas representan cada uno de los aminoácidos
que conforman la proteína.

**_¿Qué diferencias y similitudes notamos respecto de la representación inicial?_**

L3 vista 3D que arranca por defecto (Mol* Javascript) difiere de la de la pantalla
principal es que no tiene la distinción de colores que sí existe en la página de sumario.
En ambos casos las estructura de los amoniácidos son las mismas, solo difieren en
la forma de colorearse.

Por otro lado, la vista 3D permite rotar la estructura en todas las direcciones,
también aumentar o disminuir el zoom. Por defecto esta vista representa moléculas
de agua que no pudieron ser excluídas en la medición. Aunque es posible ocultarlas
desde el panel de configuración.

Además de esta vista por defecto, se puede cambiar la representación para visualizar
los aminoácidos, mostrándose, por ejemplo, con una visualización de "superficie" de la proteína.

**_En el menú de la izquierda hay opciones de distintos tipos de representación_**
**_y formas de colorear la estructura tridimensional._**
**_¿Para qué podría ser útil visualizar lo mismo de distintas maneras?_**

Las distintas formas de representación son útiles según qué sea lo que se está
queriendo analizar.

Por ejemplo, en la visualización de _Surface_ se muestra la proteína como
si fuese una "masa" (o chicle) y permite observar cavidades en donde,
por ejemplo, un fármaco podría acoplarse y generar un cambio a nivel químico.

**_¿Qué información esperaría encontrar como resultado un experimento destinado_**
**_a determinar la estructura terciaria de una molécula biológica?_**

Si el experimento busca determinar la estructura terciaria, es esperable encontrar
la posición en el espacio de los aminoácidos de manera de poder observar
los plegamientos de las proteínas.

**_Podemos explorar el contenido del archivo que acabamos de descargar si lo observamos_**
**_con un editor de texto. Haciendo clic con el botón derecho del mouse sobre el archivo descargado,_**
**_usemos la opción "Abrir con" y seleccionemos el "Bloc de Notas" u otro editor de texto._**
**_¿En qué consiste un archivo PDB?_**

Los archivos PDB, por lo obserable en el ejemplo, son archivos de texto plano con líneas de tamaño fijos.
Además cada línea comienza con un código que permite identificar qué tipo de información se encuentra
en esa línea. Esta forma facilita el parseo de información dado que permite analizar cada línea
con el parser adecuado según se detecta en el código que comienza en cada línea.

Por ejemplo, las primera líneas muestran información del experimiento: nombre, tipo de experimiento,
molécula estudiada, autores del trabajo, método del experimiento, etc...

**_Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM._**
**_¿Qué tipo de información brinda esta sección?_**

Las línea de la sección ATOM muestra la información necesaria acerca de la molécula estudiada.
Por ejemplo, se pueden observar los aminoácidos (con representación de 3 letras), los átomos
asociados a esos aminoácidos, la ubicación espacial del aminoácido, etc...

**_¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión?_**
**_¿Cómo se presenta dicha información y qué significa la representación?_**
**_Desde el punto de vista computacional: ¿de qué tipo de dato se trata esta información?_**

Sí, se puede extraer la información referida a la estructura primera. Estos datos se
encuentran distribuidos en varias líneas ya que están asociados son los puentes de
hidrógeno que forman la estructura secundaria. Pero de todas formas el dato existe y es extraíble.

A nivel computacional se trata de líneas de strings de ancho fijo. Esa estructura es fácilmente
mapeable a una lista o a un diccionario (si se conoce el tipo de dado de cada ancho fijo de cada línea).

**_¿Considera que el formato PDB es útil para presentar los resultados del experimento?_**

En estas primeras aproximaciones a este tipo de información, sí parece ser un formato útil.
Lo más interesante es que está dividido en distintos bloques de información, y cada bloque
tiene, además del identificador del dato, una estructura propia para representar la información.

**_Observamos que la información respeta cierta estructura interna._**
**_¿Cuáles son los beneficios y las limitaciones de imponer una estructura_**
**_para comunicar los resultados de un experimento?_**

Los beneficio es que se genera un estándar de distribución de información de manera
que puede ser accedida universalmente.

Como limitante se podría pensar que se pierde un poco de flexibilidad y es imperioso
ajustarse a lo determinado por el estándar. Podría pasar que determinados experimentos
no encajen del todo bien y haya que hacer ajustes en la representación.

De todas formas, por como se ve el formato con sus identificadores de línea, podrían
generarse nuevos identificadores para nuevos formatos de información.

Lo único que sí puede llegar a ser un limitante es el hecho de que cada línea tiene un
ancho de 80 caracteres, y puede llegar a haber información que entre en ese tamaño.
en ese caso habría que generar un identificador que permita obtener el dato de dos línea consecutivas.

**_Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar_**
**_algunas características de las mismas._**
**_¿Será igual con los ácidos nucléicos?_**

Entiendo que también en los ácidos nucleicos vamos a poder observar estructuras
en el plano y en el espacio.
