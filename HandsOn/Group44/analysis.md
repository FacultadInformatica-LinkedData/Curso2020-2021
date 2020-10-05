# Hands-on assignment 2  

## Analyse Data Set  

Our data set has the following data:  

- "Provincia" with value 28  
- "Municipio" with value 79  
- "Estacion" with values between (4 - 61)  
- "Magnitud" with values between (1 - 45) Magnitude is the gas that is beeing tested (CO2, S02, NOX)  
- "Punto\_Muestreo" with String values, last 2 digits of the String tell us the method for testing the gas (Fluorescencia ultravioleta, Quimioluminiscencia)  
- "Ano" with value 2020  
- "Mes" with value between (1-8)  
- "D01...D31" with value between (0-400) this is the data each day has measure.
- "V01...V31" with values (V - N) V means valid data and N means NO valid data.  

## Analyse Licensing of the Data Source  

- **Who is the publisher and the rightsholder?**  
The publisher and rightsholder of the data is the City of Madrid.  

- **What is the licence?**  
The license is ``CC0 1.0 Universal Public Domain Dedication`` and more specific information writen by the City of Madrid can be found in [Use Condition](https://datos.madrid.es/egob/catalogo/aviso-legal)  

- **Which will be the license to be used for the generated dataset?**  
We will use the same licence ``CC0 1.0 Universal Public Domain Dedication`` [Link](https://creativecommons.org/publicdomain/zero/1.0/deed.en)

## Define Resource Naming Strategy  
* Base URI: http://www.semanticweb.org/group44/ontologies/2020/9/untitled-ontology-4 

* You can check the content of the onlogy in the `ontology/madridAirQuality.ttl`


## Develop Ontology  
