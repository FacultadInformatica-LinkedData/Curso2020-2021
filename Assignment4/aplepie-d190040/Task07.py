#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# First, with RDFLib

# In[3]:


ns = Namespace("http://somewhere#")

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)


# Now, with SPARQL

# In[4]:


from rdflib.plugins.sparql import prepareQuery


q1 = prepareQuery('''
  SELECT 
    ?Subject
  WHERE { 
    ?Subject rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)


for r in g.query(q1):
  print(r.Subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# First, with RDFLib

# In[5]:


for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)
    
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1, p1, o1 in g.triples((None, RDF.type, s)):
        print(s1)


# Now, with SPARQL

# In[6]:


q2 = prepareQuery('''
  SELECT 
    ?Subject
  WHERE { 
    { ?Subject rdf:type ns:Person }
    UNION
    { ?SubClass rdfs:subClassOf ns:Person . ?Subject rdf:type ?SubClass }
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)


for r in g.query(q2):
  print(r.Subject)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# First, with RDFLib

# In[7]:


for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for s1, p1, o1 in g.triples((s, None, None)):
        print(s1, p1, o1)
        
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1, p1, o1 in g.triples((None, RDF.type, s)):
        for s2, p2, o2 in g.triples((s1, None, None)):
            print(s2, p2, o2)


# Now, with SPARQL

# In[8]:


q4 = prepareQuery('''
  SELECT 
    ?Subject ?Predicate ?Object
  WHERE { 
    { ?Subject rdf:type ns:Person . ?Subject ?Predicate ?Object }
    UNION
    { ?SubClass rdfs:subClassOf ns:Person . ?Subject rdf:type ?SubClass . ?Subject ?Predicate ?Object }
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)


for r in g.query(q4):
  print(r.Subject, r.Predicate, r.Object)


# In[ ]:




