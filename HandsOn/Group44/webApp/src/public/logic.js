let pos;
let prueba;
let nombre;

const url = "http://localhost:9000/sparql"

var dict = { 
  1:{ estacion: "Pza. de España", posicion: [40.4238823, -3.7122567] },
  2:{ estacion: "Barrio del Pilar", posicion: [40.4770471, -3.7035391] },
  3:{ estacion: "Ensanche de Vallecas", posicion: [40.369559, -3.604265] },
  4:{ estacion: "Retiro", posicion: [40.4152606, -3.6844995] },
  5:{ estacion: "Escuelas Aguirre", posicion: [40.420158, -3.697726] },
  6:{ estacion: "Sanchinarro", posicion: [40.491056, -3.6696] },
  7:{ estacion: "Urb. Embajada (Barajas)", posicion: [40.4563065, -3.632117] },
  8:{ estacion: "Vallecas", posicion: [40.3868601, -3.6591803] },
  9:{ estacion: "Avda. Ramón y Cajal", posicion: [40.4514734, -3.6773491] },
  10:{ estacion: "C/ Arturo Soria", posicion: [40.4400457, -3.6392422] },
  11:{ estacion: "Casa de Campo", posicion: [40.4193577, -3.7473445] },
  12:{ estacion: "Barajas", posicion: [40.4769179, -3.5800258] },
  13:{ estacion: "Plaza del Carmen", posicion: [40.4192091, -3.7031662] },
  14:{ estacion: "Moratalaz", posicion: [40.4079517, -3.6453104] },
  15:{ estacion: "Mendez Alvaro", posicion: [40.3980991, -3.6868138] },
  16:{ estacion: "Plaza Castilla", posicion: [40.4655841, -3.6887449] },
  17:{ estacion: "Plaza Elíptica", posicion: [40.3850336, -3.7187679] },
  18:{ estacion: "Parque Juan Carlos I", posicion: [40.4607255, -3.6163407] },
  19:{ estacion: "Plaza Tres Olivos ", posicion: [40.5005477, -3.6897308] }
};

function map() {

  var map = L.map('map').setView([40.4169416,-3.7083759],11.2);

  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
  }).addTo(map);

  L.control.scale().addTo(map);

  // Cargamos todas las posiciones de las estaciones :D
  for(let i = 1; i < 20; i++){
    prueba = L.marker(dict[i]["posicion"]).addTo(map);
    if(dict[i]["estacion"] == "Pza. de España" || dict[i]["estacion"] == "Escuelas Aguirre")
      prueba.bindPopup(dict[i]["estacion"] + ` <br> <button type=\"button\" onClick=\"loadInfo(dict[${i}].estacion)\">Informacion</button>`);
    else
      prueba.bindPopup(dict[i]["estacion"] + ` <br> <button type=\"button\">Estacion no disponible</button>`);
  }
}

function loadInfo(param){

  var x = document.getElementById("infoEstacion");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }

  const Http = new XMLHttpRequest();
  const url=`/infoEstacion?id=${param}`;
  Http.open("GET", url);

  Http.onload = function() {
    let res = JSON.parse(this.responseText);

    document.getElementById("nombreEstacion").innerHTML = `<h2>${param}</h2>`;
    document.getElementById("nombreProvincia").innerHTML = `<a href="${res.provincia}">Madrid</a>`;
    document.getElementById("nombreMunicipio").innerHTML = `<a href="${res.municipio}">Madrid</a>`;
    document.getElementById("numero").innerHTML = res.numero;

  }
  Http.send();
}

function compuestos(){
  
  let hora = document.getElementById("start").value;
  let estacion = document.getElementById("nombreEstacion").value;
  document.getElementById("fecha").innerHTML = `${hora}`;

  const Http = new XMLHttpRequest();
  const url=`/compuesto?hora=${hora}`;
  Http.open("GET", url);

  Http.onload = function() {
    let res = JSON.parse(this.responseText);
    console.log(res);

    var muestra = document.getElementById("cuadrado");
    muestra.innerHTML = "";
    for(let i = 0; i<res.length; i++){

      var p0 = document.createElement("p");
      var bas = document.createTextNode("Muestra " + (i+1) + ":");
      p0.appendChild(bas);

      var createA = document.createElement("a");
      var p1 = document.createElement("p");
      var compuesto = document.createTextNode("- Compuesto: ");
      var url = document.createTextNode(res[i].compuesto);
      createA.setAttribute("href", res[i].compuesto);
      createA.appendChild(url);
      p1.appendChild(compuesto);
      p1.appendChild(createA);

      var p2 = document.createElement("p");
      var tecnica = document.createTextNode("- Tecnica: " + res[i].tecnica);
      p2.appendChild(tecnica);

      var p3 = document.createElement("p");
      var valor = document.createTextNode("- Valor: " + res[i].valor);
      p3.appendChild(valor);

      var p4 = document.createElement("p");
      var valido = document.createTextNode("- Valido: " + res[i].valido);
      p4.appendChild(valido);

      var espacio = document.createElement("br");
      var strong = document.createElement("strong");

      muestra.appendChild(p0);
      muestra.appendChild(p1);
      muestra.appendChild(p2);
      muestra.appendChild(p3);
      muestra.appendChild(p4);
      muestra.appendChild(espacio);
    }
  }

  Http.send();


  var x = document.getElementById("muestra");
    if (x.style.display === "none") {
      x.style.display = "flex";
      x.style.alignItems = "center";
      x.style.justifyContent = "center";
    }

  var y = document.getElementById("titulo");
    if (y.style.display === "none") {
      y.style.display = "flex";
      y.style.alignItems = "center";
      y.style.justifyContent = "center";
      y.style.flexDirection = "column";
      y.style.textAlign = "center";
    }
}


