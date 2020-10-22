# -*- coding: utf-8 -*-
"""
    Hands-On Assignment 5
    SPARQL queries for checking WikiData liking
"""

github_storage = "/home/hxshfx/Descargas/output-with-links.ttl"

"Data loading and graph building"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.plugins.sparql import prepareQuery
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.semanticweb.org/group16/ontologies/air-quality#"), override=False)
g.parse(github_storage, format="nt")

ns = Namespace("http://www.semanticweb.org/group16/ontologies/air-quality#")

# ------------------------------------------

# List all the properties used in our dataset

print("------- Properties:")

q1 = prepareQuery('''
    SELECT DISTINCT
        ?Property
    WHERE {
        ?Subject ?Property ?Object .
    }
    '''
)

for s in g.query(q1):
    print(s.Property.toPython())


# List all the stations included in our dataset

print("------- Stations:")

q2 = prepareQuery('''
    SELECT DISTINCT
        ?StLabel
    WHERE {
        ?St rdf:type ns:Station .
        ?St rdfs:label ?StLabel .
    }
    ''',
    initNs = {"rdf":RDF, "rdfs":RDFS, "ns":ns}
)

for s in g.query(q2):
    print(s.StLabel.toPython())


# List all the magnitudes measured in our dataset's stations

print("------- Magnitude codes:")

q3 = prepareQuery('''
    SELECT DISTINCT
        ?Notation ?LabelEs ?LabelEn ?Code
    WHERE {
        ?Magnitude rdf:type ns:Magnitude .
        ?Magnitude ns:measureNotation ?Notation .
        ?Magnitude ns:measureCode ?Code .
        ?Magnitude rdfs:label ?LabelEn , ?LabelEs .
            FILTER (LANG(?LabelEn) = 'en' && LANG(?LabelEs) = 'es')
    }
    ''',
    initNs = {"rdf":RDF, "rdfs":RDFS, "ns":ns}
)

for s in g.query(q3):
    print(s.Notation.toPython())
    print(s.LabelEs.toPython())
    print(s.LabelEn.toPython())
    print(s.Code.toPython())
    print("--")

# List all the measures linked to an specific station

print("------- Measures in \"Moratalaz\" station")

q4 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?St rdf:type ns:Station .
        ?St rdfs:label "Moratalaz"^^<http://www.w3.org/2001/XMLSchema#string> .
        ?Measure rdf:type ns:Measurement .
        ?Measure ns:measuredAt ?St .
    }
    ''',
    initNs = {"rdf":RDF, "rdfs":RDFS, "ns":ns}
)

for s in g.query(q4):
    print(s.Measure.toPython())

# List all the measures given an specific day

print("------- Measures taken in the day \"2016/4/27\"")

q5 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?Measure rdf:type ns:Measurement .
        ?Measure ns:dateOfMeasure "2016/4/27"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
    }
    ''',
    initNs = {"rdf":RDF, "ns":ns}
)

for s in g.query(q5):
    print(s.Measure.toPython())

# List all the measures given an specific magnitude

print("------- Measures of sulfur dioxide")

q6 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?Measure rdf:type ns:Measurement .
        ?Magnitude rdf:type ns:Magnitude .
        ?Magnitude rdfs:label ?Label .
            FILTER (LANG(?Label) = 'en' && REGEX(?Label, "Sulfur dioxide", "i"))
        ?Magnitude ns:measureCode ?Code .
        ?Measure ns:measureType ?Code .
    }
    ''',
    initNs = {"rdf":RDF, "ns":ns}
)

for s in g.query(q6):
    print(s.Measure.toPython())

# List all the measures in a given district

print("------- Measures taken in \"Barajas\" district")

q7 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?St rdf:type ns:Station .
        ?St ns:inDistrict ?District .
        ?District owl:sameAs <https://www.wikidata.org/wiki/Q807230> .
        ?Measure rdf:type ns:Measurement .
        ?Measure ns:measuredAt ?St .
    }
    ''',
    initNs = {"owl":OWL, "rdf":RDF, "ns":ns}
)

for s in g.query(q7):
    print(s.Measure.toPython())

# List all the measures taken in 2014

print("------- Measures taken in 2014")

q8 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?Measure rdf:type ns:Measurement .
        ?Measure ns:dateOfMeasure ?Date .
            FILTER REGEX (STR(?Date), "^2014", "i") 
    }
    ''',
    initNs = {"rdf":RDF, "ns":ns}
)

for s in g.query(q8):
    print(s.Measure.toPython())

# List the measures given a magnitude and a range value

print("------- Measures of Nitrogen oxides whose value is equal or more than 100")

q9 = prepareQuery('''
    SELECT DISTINCT
        ?Measure
    WHERE {
        ?Measure rdf:type ns:Measurement .
        ?Magnitude rdf:type ns:Magnitude .
        ?Magnitude rdfs:label ?Label .
            FILTER (LANG(?Label) = 'en' && REGEX(?Label, "Nitrogen oxides", "i"))
        ?Magnitude ns:measureCode ?Code .
        ?Measure ns:measureType ?Code .
        ?Measure ns:measureValue ?Value .
            FILTER (?Value >= 100)
    }
    ''',
    initNs = {"rdf":RDF, "ns":ns}
)

for s in g.query(q9):
    print(s.Measure.toPython())