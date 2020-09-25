# Assignment3

1. Get all the properties that can be applied to instances of the Politician class (<http://dbpedia.org/ontology/Politician> or its equivalent in Wikidata).

```
SELECT DISTINCT ?properties
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values
}
```

2. Get all the properties, except for rdf:type, that are applied to instances of the Politician class

```
SELECT DISTINCT ?properties
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type) .
}
```

3. Which different values exist for the properties, except for rdf:type, of the instances of the Politician class?

```
SELECT DISTINCT ?values
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type) .
}
```

4. For each of these properties, except for rdf:type, which different values do they take in those instances?

```
SELECT DISTINCT ?properties ?values
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type)
}
```

5. For each of the properties, except for rdf:type, how many distinct values do they take?
```
SELECT DISTINCT ?properties count(DISTINCT ?values)
WHERE 
{
 ?x rdf:type <http://dbpedia.org/ontology/Politician> .
 ?x ?properties ?values .
 FILTER (?properties != rdf:type)
}
```