#!/usr/bin/env python
# coding: utf-8

# **Task 08: Completing missing data**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/"


# In[2]:


from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"resources/data01.rdf", format="xml")
g2.parse(github_storage+"resources/data02.rdf", format="xml")


# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# In[3]:


ns = Namespace("http://data.org#")

for s, p, o in g1.triples((None, None, ns.Person)):
    print(s)


# In[4]:


for s, p, o in (g1 + g2).triples((None, None, ns.Person)):
    for s1, p1, o1 in (g1 + g2).triples((s, None, None)):
        print(s1, p1, o1)

