from flask import Flask, render_template, request, json, redirect, url_for, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g = Graph()
g.namespace_manager.bind('rr', Namespace("http://www.w3.org/ns/r2rml#"), override=False)
g.namespace_manager.bind('rml', Namespace("http://semweb.mmlab.be/ns/rml#"), override=False)
g.namespace_manager.bind('ql', Namespace("http://semweb.mmlab.be/ns/ql#"), override=False)
g.namespace_manager.bind('transit', Namespace("http://vocab.org/transit/terms/"), override=False)
g.namespace_manager.bind('xsd', Namespace("http://www.w3.org/2001/XMLSchema#"), override=False)
g.namespace_manager.bind('wgs84_pos', Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#"), override=False)
g.namespace_manager.bind('', Namespace("http://group11.com/ontology#"), override=False)
g.namespace_manager.bind('rml', Namespace("http://semweb.mmlab.be/ns/rml#"), override=False)
g.namespace_manager.bind('owl', Namespace("http://www.w3.org/2002/07/owl#"), override=False)

ns = Namespace("http://group11.com/ontology#")
ns2 = Namespace("http://group11.com/resource/District/")
owl = Namespace("http://www.w3.org/2002/07/owl#")
g.parse("./rdf/data-with-links-V2.nt", format="nt")


def main():
    district = "Fuencarral-ElPardo"
    _jsonList = []
    query = "select distinct ?Object " \
            " where{ { ?Object <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://group11.com/ontology#MovileRecyclePoint>. " \
            " ?Object ?Property ?Subject. " \
            " ?Subject <http://group11.com/ontology#districtName> " + '"' + district + '".' + "} }"

    q3 = prepareQuery(query)
    for r in g.query(q3):
        tojson = {'id':str(r[0])}
        print(r[0])
        query2 = "select distinct ?Property " \
                 "where { ?m ?Property ?Object .}"
        q4 = prepareQuery(query2)
        for r2 in g.query(q4, initBindings={"m": r[0]}):
            #print(r[0], r2[0])
            query3 = "select distinct ?Object " \
                     "where { ?m ?p ?Object .}"
            q5=prepareQuery(query3)
            for r3 in g.query(q5, initBindings={"m":r[0], "p":r2[0]}):
                propiedad=str(r2[0])
                objeto=str(r3[0])
                #print(r[0], propiedad, objeto)
            if propiedad!="http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
                #print(r[0], propiedad, objeto)
                #poshastag=propiedad.find("#")
                #print(propiedad.replace("http://group11.com/ontology#",""))
                #print(poshastag)
                tojson[propiedad.replace("http://group11.com/ontology#","")]=objeto
        #break
        _jsonList.append(tojson)
    print(json.dumps(_jsonList))
            #print(r[0], r2[0], r2[1])
            #_json.append(json.dumps({"plm": r[0], "propiedad": r2[0], "objeto": r2[1]}))
def test():
    uri=""

if __name__ == '__main__':
    main()
