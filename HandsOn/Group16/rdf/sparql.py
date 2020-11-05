# -*- coding: utf-8 -*-
"""
    Hands-On Assignment 5
    SPARQL queries for checking WikiData liking
"""

data_storage = "rdf/ntriples/output-with-links.nt" 

"Data loading and graph building"

import pandas as pd
import requests
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.plugins.sparql import prepareQuery
from collections import OrderedDict
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://www.semanticweb.org/group16/ontologies/air-quality#"), override=False)
g.parse(data_storage, format="nt")

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
    ORDER BY asc(?Property)
    '''
)

for s in g.query(q1):
    print(s.Property.toPython())


# List all the stations included in our dataset

print("------- Stations:")

q2 = prepareQuery('''
    SELECT DISTINCT
        ?StLabel ?StCode
    WHERE {
        ?St rdf:type ns:Station .
        ?St rdfs:label ?StLabel .
        ?St ns:stationCode ?StCode .
    }
    ORDER BY asc(?StLabel)
    ''',
    initNs = {"rdf":RDF, "rdfs":RDFS, "ns":ns}
)

for s in g.query(q2):
    print(s.StLabel.toPython())
    print(s.StCode.toPython())


# List all the magnitudes measured in our dataset's stations

print("------- Magnitudes:")

q3 = prepareQuery('''
    SELECT DISTINCT
        ?Notation ?LabelEs ?LabelEn ?Code ?Description
    WHERE {
        ?Magnitude rdf:type ns:Magnitude .
        ?Magnitude rdfs:comment ?Description .
        ?Magnitude ns:measureNotation ?Notation .
        ?Magnitude ns:measureCode ?Code .
        ?Magnitude rdfs:label ?LabelEn , ?LabelEs .
            FILTER (LANG(?LabelEn) = 'en' && LANG(?LabelEs) = 'es')
    }
    ORDER BY xsd:integer(?Code)
    ''',
    initNs = {"rdf":RDF, "rdfs":RDFS, "ns":ns}
)

for s in g.query(q3):
    print(s.Notation.toPython())
    print(s.LabelEs.toPython())
    print(s.LabelEn.toPython())
    print(s.Description.toPython())
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
        ?Measure ns:dateOfMeasure ?Date .
            FILTER REGEX (STR(?Date), "^2016-04-27", "i") 
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
        ?Measure ns:measuredMagnitude ?Magnitude .
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
    ORDER BY asc(?Date)
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
            FILTER (LANG(?Label) = 'en' && REGEX(?Label, "Nitrogen oxide", "i"))
        ?Measure ns:measuredMagnitude ?Magnitude .
        ?Measure ns:measureValue ?Value .
            FILTER (?Value >= 100)
    }
    ''',
    initNs = {"rdf":RDF, "ns":ns}
)

for s in g.query(q9):
    print(s.Measure.toPython())

# List some features extracted from Wikidata datasource

print("------- District features from Wikidata")

url = 'https://query.wikidata.org/sparql'
q10 = """
    SELECT DISTINCT
        ?item ?itemLabel ?population ?area ?image
    WHERE {
        ?item wdt:P31 wd:Q3032114 .
        ?item wdt:P1082 ?population .
        ?item wdt:P2046 ?area .
        ?item wdt:P18 ?image .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """
r = requests.get(url, params = {'format': 'json', 'query': q10})
data = r.json()

districts = []
for item in data['results']['bindings']:
    districts.append(OrderedDict({'districtURI': item['item']['value'],
                                 'districtName': item['itemLabel']['value'],
                                 'population': item['population']['value'],
                                 'area': item['area']['value'],
                                 'image': item['image']['value'],
    }))
df = pd.DataFrame(districts)
df.set_index("districtURI")
df = df.astype({'population': int, 'area': float})
print(df.head())
