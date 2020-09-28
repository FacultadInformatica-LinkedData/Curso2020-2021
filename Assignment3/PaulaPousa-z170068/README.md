# Assigment 3

1.

```
SELECT DISTINCT ?properties
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?y 

}
```

2.

```
SELECT DISTINCT ?properties
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?y .
 FILTER (?properties != rdf:type)
}
```

3.

```
SELECT DISTINCT ?values
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type)
}
```

4.

```
SELECT DISTINCT ?properties ?values
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type)
}
```

5.

```
SELECT DISTINCT ?properties COUNT(DISTINCT ?values)
WHERE 
{
?x rdf:type <http://dbpedia.org/ontology/Politician> .
?x ?properties ?values .
FILTER (?properties != rdf:type)
}
```