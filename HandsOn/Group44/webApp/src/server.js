const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch')
const request = require('request')
const fs = require('fs')

const rdfstore = require('rdfstore');

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
  let retorno = infoEstacion(req.query.id); // Info de Madrid
  res.send(retorno);
});

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

function infoEstacion(estacion){
  console.log("Estacion actual: " + estacion);
  rdfstore.create(function(err, store){
    var rdf = fs.readFileSync('./nuestro.nt').toString();
    store.load('text/turtle', rdf, function(err, resultado){
      if(err)
        console.log(err)

      store.execute(
        "PREFIX aqm: <http://www.semanticweb.org/group44/ontologies/2020/9/madridAirQuality/>\r\n" +
        "SELECT ?station WHERE {\r\n"+
          "\t\t ?station aqm: ?s ?p ?o\r\n"+
        "} LIMIT 10\r\n"
        , function(success, results){
        console.log(success, results);
      });

    });
  });
}
