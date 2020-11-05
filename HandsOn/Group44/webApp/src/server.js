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

app.get('/compuesto', function (req, res) {
  let retorno = compuesto(req.query.hora); // Info de Madrid
  res.send(retorno);
});


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


function miniParser(){
  console.log(results);


}

function infoEstacion(estacion){
  console.log("Estacion actual: " + estacion);
  rdfstore.create(function(err, store){
    var rdf = fs.readFileSync('./nuestro.nt').toString();
    store.load('text/turtle', rdf, function(err, resultado){
      if(err)
        console.log(err)

      query = `
        SELECT ?a ?b ?c
        WHERE { 
          ?a ?b ?c
        }
        LIMIT 10
      `;

      store.execute(query, function(success, results){
        miniParser(results);
      });

    });
  });
}

function compuesto(hora){
  console.log(hora)
}
