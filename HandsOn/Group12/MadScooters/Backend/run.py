virtualenv env
source env/bin/activate
export FLASK_APP="run.py"
flask run
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
from flask import Flask, request
import json
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD
import rdflib.plugins.sparql as sparql
from flask_cors import CORS


app = Flask("MadScooters")
CORS(app)
# GET /scooters?district=Centro$neighbourhood=Embajadores&company=Acciona
#coger parametros endpoint
@app.route("/scooters")
def scooters():
   s = Scooters()
   page=request.args.get('page')
   district=request.args.get('district')
   neighbourhood=request.args.get('neighborhood')
   company=request.args.get('company')
   lista =s.get_companies_list(district,neighbourhood,company)
   link = s.get_wikidataLink_n(neighbourhood)
   [x,y]=s.get_NB_coordinates(link).split()
   return json.dumps({
     'wikidataDistrict': s.get_wikidataLink_d(district),
     'wikidataNeighbourhood': link,
     'coordNB': [x,y],
     'companies': [{key: value} for key,value in lista.items()]
     },indent=4,separators=(',', ': '))
     
class Scooters:

    def __init__(self):
        self.g = Graph()
        self.g.parse('triples-with-links.nt', format='nt')
        self.companies = [
          'Acciona',
          'Taxify',
          'Koko',
          'Ufo',
          'Rideconga',
          'Flash',
          'Lime',
          'Wind',
          'Bird',
          'RebyRides',
          'Movo',
          'Mygo',
          'JumpUber',
          'SjvConsulting'
        ]

    def get_wikidataLink_d(self, name):
        q = sparql.prepareQuery("""
  		PREFIX owl: <http://www.w3.org/2002/07/owl#> 
  		PREFIX properties: <http://scooters.com/Group12/Properties/> 
  		SELECT DISTINCT ?district ?linkWikidata
		WHERE {
    		?district properties:name_district ?o.
    		?district rdf:type <http://scooters.com/Group12/Classes/District>.
		?district owl:sameAs ?linkWikidata.
    		}""")
        o = Literal(name, datatype=XSD.string)
        qres = self.g.query(q, initBindings={'o': o})
        for row in qres:
          result = row.get(1)
        return result

        

    def get_NB_coordinates(self, link):
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        query_start="""
        SELECT ?coord
        WHERE {
         """
        nb="wd:"+link[30:]
        query_end=""" wdt:P625 ?coord .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
        }"""
        sparql.setQuery(query_start+nb+query_end)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        results_df = pd.io.json.json_normalize(results['results']['bindings'])
        df=results_df.at[0,'coord.value']
        return df[6:-1]

    def get_wikidataLink_n(self, name):
        q = sparql.prepareQuery("""
  		PREFIX owl: <http://www.w3.org/2002/07/owl#> 
  		PREFIX properties: <http://scooters.com/Group12/Properties/> 
	  	SELECT DISTINCT ?neighbourhood ?linkWikidata
		WHERE {
		?neighbourhood properties:name_nb ?o.
		?neighbourhood rdf:type <http://scooters.com/Group12/Classes/Neighbourhood>.
		?neighbourhood owl:sameAs ?linkWikidata.
	    	}""")
        o = Literal(name, datatype=XSD.string)
        qres = self.g.query(q, initBindings={'o': o})
        for row in qres:
          result = row.get(1)
        return result
        

    def spaces(self,s):
      result=''.join(' ' + c if c.isupper() else c for c in s)
      return result[1:len(result)]

    def get_companies_list(
        self,
        district,
        neighbourhood,
        company
        ):
        companies_list = dict()
        query_beginning = """
  			PREFIX owl: <http://www.w3.org/2002/07/owl#> 
  			PREFIX properties: <http://scooters.com/Group12/Properties/> 
  			SELECT DISTINCT ?district ?nb ?Quantity
			  WHERE {
		    	?nb properties:name_nb ?n.
		    	?place properties:hasNeighbourhood ?nb.
		    	?district properties:name_district ?d.
		    	?place properties:hasDistrict ?district.
		    	?place properties:"""
        query_end = ' ?Quantity.}'
        d = Literal(district, datatype=XSD.string)
        n = Literal(neighbourhood, datatype=XSD.string)
        if company in self.companies:
          quantity="quantity"+company
          q = sparql.prepareQuery(query_beginning+quantity+query_end)
          qres = self.g.query(q, initBindings={'d': d, 'n': n})
          company = self.spaces(company)
          for row in qres:
            companies_list[company] = int(str(row.get(2)))
          return companies_list
        else:
          for comp in self.companies:
            quantity="quantity"+comp
            q = sparql.prepareQuery(query_beginning + quantity+ query_end)
            qres = self.g.query(q, initBindings={'n': n, 'd': d})
            comp=self.spaces(comp)
            for row in qres:
              companies_list[comp] = int(str(row.get(2)))
          return companies_list

   

		
		
			
