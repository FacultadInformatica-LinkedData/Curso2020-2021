# Analysis over the Data Source

## Analyse Data Set
Analizando el dataset seleccionado en formato CSV de los diferentes puestos de bicicletas eléctricas en la ciudad de Madrid podemos observar algunas peculiaridades: 
* Aparición de varios puestos de bicicletas en una misma calle y prácticamente en las mismas coordinadas considerandolos como una ampliación del puesto inicial.
* Podemos observar también que algunos puestos comparten id categorizándose como ampliaciones (p.Ej: 025a y 025b).
* En cuanto a irregularidades en el dataset, podemos observar que el formato de campos como "Fecha de Alta" no son muy relevantes o representativos ya que se componen de un número de 5 cifras (p.Ej:41813).
* Analizando el campo "Gis_x" en un principio pensamos que se trataba de las coordenadas del puesto pero con la presencia de un campo explícito para la longitud y latitud finalmente concluimos que se trata de la localización del puesto basado en el Geographic Information System.
* El número de plazas de cada puesto está representado mediante números en un campo de texto en vez de valores numéricos puros.
* El campo "Tipo de Reserva" no es demasiado significativo ya que todas las reservas se hacen a través de BiciMAD.
* El campo "Dirección" mezcla el contenido de la Calle donde se encuentra el puesto con el número de plazas de este.
* Como es de esperar, las latitudes y longitudes son muy similares ya que todos los puestos de bicicletasse encuentran en la ciudad de Madrid.

## Analyse Licensing of the Data Source
### Who is the publisher and the rightsholder?
El dataset ha sido publicado por el Ayuntamiento de Madrid y agrupado en el sector de Transporte.
### What is the licence?
Los datos contenidos en este dataset publicado en "datos.madrid.es" están sujetos bajo los términos de la licencia Creative Commons-Attribution(CC-BY 4.0) que permite:
*copiar, distribuir y divulgar públicamente.
*servir de base para obras derivadas como resultado de su análisis o estudio.
*ser utilizadas con fines comerciales o no comerciales, siempre que este uso no constituya una actividad administrativa pública.
*modificar, transformar y adaptar.
*se deba mencionar la autoría de la Comunidad de Madrid.

A su vez, los datos también están sujetos a la Ley 37/2007 que habla sobre la reutilización de la información contenida en los conjuntos de datos sometida a las siguientes condiciones:
*que el contenido de la información no sea alterado.
*que no se desnaturalice el sentido de la información.
*que se mencione la fuente.
*que se mencione la fecha de la última actualización.
### Which will be the license to be used for the generated dataset?
La licencia de los datos que se generarán a partir de este dataset será del mismo carácter que la presente en los datos originales (CC-BY 4.0) con la modificación de que la autoría de los integrantes del grupo no será necesaria incluirla si se lleva a cabo su reutilización.
## Resource Naming Strategy
Términos: Latitud, Longitud, Número de plazas, Calle, Barrio, Distrito, Fecha de alta.
URI form: http://semantic.web.es/group05/ontology/BiciMAD/
Content negotiation: JSON
### Examples of resource URI's
Puesto en concreto: http://semantic.web.es/group05/ontology/BiciMAD/estacion/2
Calle: http://semantic.web.es/group05/ontology/BiciMAD/estacion/2/calle
Numero de Plazas: http://semantic.web.es/group05/ontology/BiciMAD/estacion/2/puestos
### Structure of the Ontology
Clases: Estación, Calle, Barrio, Distrito, Coordenadas.
Properties: numeroCalle, numeroEstacion, puestos, tieneDistrito, tieneBarrio, tieneCiudad, tieneCoordenadas, latitud, longitud.
Datatypes: xsd:Integer, xsd:String.