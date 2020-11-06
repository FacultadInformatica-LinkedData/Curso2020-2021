from flask import Flask, render_template, request
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from rdflib import Graph, Namespace, Literal, RDF
from rdflib.plugins.sparql import prepareQuery
import folium
import sys
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)
def return_distance(latitude_user,longitude_user,coords):
    '''This function return the distance between
    two streets in kilometers'''
    coord_user = (latitude_user, longitude_user)
    return geodesic(coord_user, coords).kilometers


'''Function for looking for the streets and their latitudes and longitudes '''
@app.route('/Distance', methods=["POST"])
def sparql_search():
    street = request.form.get("street")
    postalCode = request.form.get("postalCode")

    #We have to separate the latitude and the longitude
    if street:
        latitude = str(street).split(',')[0]
        longitude = str(street).split(',')[1]
    else:
        geolocator = Nominatim(user_agent="Geoparking")
        location_user = geolocator.geocode({"postalcode":postalCode})
        latitude, longitude = location_user.latitude, location_user.longitude

    actual_dist = -1
    parking = ''
    totalslots= -1
    addressid= ''
    schedule= ''
    province = ''
    city = ''
    district = ''
    neighborhood = ''
    wikistreet = ''
    wikiprovince = ''
    wikicity = ''
    wikidistrict = ''
    wikineighborhood = ''
    image = ''
    g = Graph()
    github_storage = "https://raw.githubusercontent.com/adrix1341/Curso2020-2021/master/HandsOn/Group02/rdf/output" \
                     "-with-links.nt "
    g.parse(github_storage, format="nt")

    findparking = Namespace("http://findyourparking.es/lcc/ontology/Parking#")
    owl = Namespace("http://www.w3.org/2002/07/owl#")
    wikidata = Namespace("http://www.wikidata.org/prop/direct/")

    q1 = prepareQuery('''
                     SELECT DISTINCT ?x ?parkname ?y ?street ?lat ?lon ?totalslots ?addressid ?schedule ?wikistreet ?province ?city ?district ?neighborhood ?wikiprovince ?wikicity ?wikidistrict ?wikineighborhood
                     WHERE {
                      ?x rdf:type findparking:Parking.
                      ?x findparking:hasName ?parkname.
                      ?x findparking:hasTotalSlots ?totalslots.
                      ?x findparking:hasSchedule ?schedule.
                      ?y rdf:type findparking:Address.
                      ?x findparking:hasProvince ?p.
                      ?x findparking:hasCity ?c.
                      ?x findparking:hasDistrict ?d.
                      ?x findparking:hasNeighborhood ?n.
                      ?p findparking:hasProvince ?province.
                      ?p owl:sameAs ?wikiprovince.
                      ?c owl:sameAs ?wikicity.
                      ?d owl:sameAs ?wikidistrict.
                      ?n owl:sameAs ?wikineighborhood.
                      ?c findparking:hasCity ?city.
                      ?d findparking:hasDistrict ?district.
                      ?n findparking:hasNeighborhood ?neighborhood.
                      ?x findparking:hasAddress ?y.
                      ?y findparking:hasAddressId ?addressid.
                      ?y findparking:hasStreet ?street.
                      ?y owl:sameAs ?wikistreet. 
                      ?x findparking:hasLatitude ?lat.
                      ?x findparking:hasLongitude ?lon
                     }
                     ORDER BY ASC(?street)
                     ''',
                      initNs={"findparking": findparking, "rdf": RDF, "owl": owl, "wikidata": wikidata}
                      )

    for st in g.query(q1):

        parkini,streeti,latitudi,longitudi,totalsloti,addressidi,scheduli = st.parkname, st.street, st.lat, st.lon, st.totalslots, st.addressid, st.schedule
        wikistreeti, wikiprovinci, wikiciti, wikidistricti, wikineighborhoodi = st.wikistreet, st.wikiprovince, st.wikicity, st.wikidistrict, st.wikineighborhood
        provinci, citi, districti, neighborhoodi = st.province, st.city, st.district, st.neighborhood
        coordlist = [latitudi, longitudi]

        if street:
            km = return_distance(latitude,longitude, tuple(coordlist))
        else:
            auxList = [location_user.latitude, location_user.longitude]
            km= geodesic(tuple(auxList), tuple(coordlist)).kilometers

        if actual_dist == -1:
            actual_dist = km
            parking = parkini
            park_street = streeti
            totalslots=totalsloti
            addressid=addressidi
            schedule=scheduli
            province=provinci
            city=citi
            district=districti
            neighborhood=neighborhoodi
            wikistreet=wikistreeti
            wikiprovince=wikiprovinci
            wikicity=wikiciti
            wikidistrict=wikidistricti
            wikineighborhood=wikineighborhoodi
            pk_lat = latitudi
            pk_long = longitudi
        elif km < actual_dist:
            actual_dist = km
            parking = parkini
            park_street = streeti
            totalslots = totalsloti
            addressid = addressidi
            schedule=scheduli
            province = provinci
            city = citi
            district = districti
            neighborhood = neighborhoodi
            wikistreet = wikistreeti
            wikiprovince = wikiprovinci
            wikicity = wikiciti
            wikidistrict = wikidistricti
            wikineighborhood = wikineighborhoodi
            pk_lat = latitudi
            pk_long = longitudi

    wd=Namespace("https://www.wikidata.org/wiki#")

    wiki1 = wikistreet.split('Q')[1]
    wiki1 = 'Q' + wiki1
    query2 = str('''
                         PREFIX wikidata: <http://www.wikidata.org/prop/direct/>
                         SELECT DISTINCT ?image
                         WHERE {
                          wd:'''+ wiki1 + ''' wikidata:P18 ?image
                          
                         }
                         ''')


    endpoint_url = "https://query.wikidata.org/sparql"
    def get_results(endpoint_url, query2):
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query2)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    results = get_results(endpoint_url, query2)
    imaget = ''
    for result in results["results"]["bindings"]:
        imaget = str(result)
    # Splitting the object to obtain only the link
    imaget = imaget.split('h')[1] + 'h' + imaget.split('h')[2]
    imaget = 'h' + imaget   #Inserting the h for http://
    imaget = imaget.split("'")[0]

    map = folium.Map(
        location = [pk_lat, pk_long],
        zoom_start = 12
    )
    folium.Marker(
        location=[pk_lat, pk_long],
        popup=("Your nearest parking is: " + '<b>' +parking +'</b>'+", at "+str(actual_dist)+" km from your current position." + '<br>' + '<b>Parking Info:</b>' + '<br>' + "  -Address: " + ' <a href=' + wikistreet + '>' + addressid + '</a>' + '<br>'
               + "  -Province: " + '<a href=' + wikiprovince + '>' + province + '</a><br>' + "  -City: " + ' <a href=' + wikicity + '>' + city + '</a>' + '<br>'
               + "  -District: " + ' <a href=' + wikidistrict + '>' + district + '</a>' + '<br>'
               + "  -Neighborhood: " + ' <a href=' + wikineighborhood + '>' + neighborhood + '</a>' + '<br>' +
               "  -TotalSlots: " + totalslots + '<br>' + "  -Schedule: " + schedule + '<br>' +'<style>img{width: 100%;height: auto;}</style>' + '<img src=' + imaget + ' alt="Image of the parking street"' + '></img'),
        tooltip="Click here for more info.",
        icon=folium.Icon(color='red', icon='star')
    ).add_to(map)
    folium.Marker(
        location=[latitude, longitude],
        popup="<b>You are here.</b>",
        tooltip="Click Here!"
    ).add_to(map)

    return map._repr_html_()



@app.route('/Ontology')
def ontology():
    g = Graph()
    github_storage = "https://raw.githubusercontent.com/adrix1341/Curso2020-2021/master/HandsOn/Group02/ontology/ontology_updated.ttl"
    g.parse(github_storage, format="ttl")
    ss = []
    pp = []
    oo = []
    for s, p, o in g:
        ss.append(s)
        pp.append(p)
        oo.append(o)
    return render_template("ontology.html", ss=ss,pp=pp,oo=oo)
@app.route('/Streets')
def show_dataset():
    g = Graph()
    github_storage = "https://raw.githubusercontent.com/adrix1341/Curso2020-2021/master/HandsOn/Group02/rdf/output" \
                     "-with-links.nt "
    g.parse(github_storage, format="ttl")
    findparking = Namespace("http://findyourparking.es/lcc/ontology/Parking#")
    qp = prepareQuery('''
          SELECT DISTINCT  ?streets ?parkingname ?totalslots
          WHERE { 
           ?x rdf:type findparking:Parking.
           ?x findparking:hasName ?parkingname.
           ?x findparking:hasTotalSlots ?totalslots.
           ?y rdf:type findparking:Address.
           ?x findparking:hasAddress ?y.
           ?y findparking:hasAddressId ?streets
          }
          ORDER BY ASC(?streets)
          ''',
                      initNs={"findparking": findparking, "rdf": RDF}
                      )
    parkings = []
    streets = []
    totalslots =[]
    for r in g.query(qp):
        parkings.append(r.parkingname)
        streets.append(r.streets)
        totalslots.append(r.totalslots)
    return render_template("streets.html", streets=streets)



@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
