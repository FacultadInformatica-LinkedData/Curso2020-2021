const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch')
const request = require('request')
const fs = require('fs')

const rdfstore = require('rdfstore');
var estacionAtual;

const app = express();

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:true}));

app.get('/', function (req, res) {
  res.render('index', {isISBN: null, book: null, error: null})
});

app.listen(3000, function () {
  console.log('The best web ever is running on port 3000!');
});

app.get('/infoEstacion', function (req, res) {
  estacionActual = req.query.id;
  infoEstacion(req.query.id, function(retorno){
    res.send(retorno);
  });
});

app.get('/compuesto', function (req, res) {
  compuesto(req.query.hora, function(retorno){
    res.send(retorno);
  });
});


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


function miniParser(res){
  let leJason = {
    numero: res[0].stationId.value.charAt(res[0].stationId.value.length - 1),
    municipio: res[0].MunicipalityWiki.value,
    provincia: res[0].ProvinceWiki.value,
  }

  return leJason;
}

function infoEstacion(estacion, callback){
  let res;
  rdfstore.create(function(err, store){
    var rdf = fs.readFileSync('./nuestro.nt').toString();
    store.load('text/turtle', rdf, function(err, resultado){
      if(err)
        console.log(err)
      query = `
        PREFIX swo: <http://www.semanticweb.org/group44/ontologies/madridAirQuality#>
        PREFIX dbp: <http://dbpedia.org/ontology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT ?stationId ?MunicipalityWiki ?ProvinceWiki
        WHERE { 
          ?stationId swo:stationPlace "${estacion}"^^xsd:string .
          ?Municipality swo:containStation ?stationId .
          ?Municipality owl:sameAs ?MunicipalityWiki .
          ?Municipality swo:isPartOf ?Province .
          ?Province owl:sameAs ?ProvinceWiki .
        }
        LIMIT 10
      `;
      store.execute(query, function(success, results){
        res = miniParser(results);
        return callback(res);
      });
    });
  });
}

function theOtherMiniParser(res){

  let leJason = [];

  for(let i = 0; i<res.length; i++){
    leJason.push({
      compuesto: res[i].Compound.value,
      valor: res[i].Value.value,
      tecnica: res[i].Technique.value,
      valido: res[i].Valid.value,
    })
  }

  return leJason;
}

function compuesto(hora, callback){

  let fecha = hora.split("-");
  fecha[1] = fecha[1].replace("0", "");

  fecha = `${fecha[0]}-${fecha[1]}-${fecha[2]}`

  let res;
  rdfstore.create(function(err, store){
    var rdf = fs.readFileSync('./nuestro.nt').toString();
    store.load('text/turtle', rdf, function(err, resultado){
      if(err)
        console.log(err)
      query = `
        PREFIX swo: <http://www.semanticweb.org/group44/ontologies/madridAirQuality#>
        PREFIX dbp: <http://dbpedia.org/ontology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT ?Compound ?Value ?Technique ?Valid
        WHERE { 
          ?stationId swo:stationPlace "${estacionActual}"^^xsd:string .
          ?stationId swo:takeMeasure ?Measure .
          ?Measure xsd:date "${fecha}"^^xsd:date .
          ?Measure swo:measuredCompound ?Compound .
          ?Measure swo:measuredValue ?Value .
          ?Measure swo:measuringTechnique ?Technique .
          ?Measure swo:isValid ?Valid .
        }
      `;
      store.execute(query, function(success, results){
        res = theOtherMiniParser(results);
        return callback(res);
      });
    });
  });
}
