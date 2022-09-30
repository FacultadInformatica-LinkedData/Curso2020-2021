#!/usr/bin/env python
# coding: utf-8

# **Task 09: Data linking**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/"


# In[2]:


from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"resources/data03.rdf", format="xml")
g2.parse(github_storage+"resources/data04.rdf", format="xml")


# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

# In[3]:


from rdflib.namespace import RDF, OWL
from rdflib.plugins.sparql import prepareQuery

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns1 = Namespace("http://data.three.org#")
ns2 = Namespace("http://data.four.org#")

q1 = prepareQuery('''
  SELECT 
    ?Subject ?FN ?Family
  WHERE { 
    ?Subject rdf:type ns:Person .
    ?Subject vcard:FN ?FN .
    ?Subject vcard:Family ?Family
  }
  ''',
  initNs = { "ns" : ns1, "rdf": RDF, "vcard": VCARD}
)

q2 = prepareQuery('''
  SELECT 
    ?Subject ?FN ?Family
  WHERE { 
    ?Subject rdf:type ns:Person .
    ?Subject vcard:FN ?FN .
    ?Subject vcard:Family ?Family
  }
  ''',
  initNs = { "ns" : ns2, "rdf": RDF, "vcard": VCARD}
)

for s, p, o in g1.query(q1):
    for s1, p1, o1 in g2.query(q2):
        if ((p == p1) and (o == o1)):
            g3.add((s, OWL.sameAs, s1))
            
for s, p, o in g3.triples((None, None, None)):
    print(s, p, o)

