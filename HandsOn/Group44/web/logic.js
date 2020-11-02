let pos;
let prueba;
let nombre;

var dict = {
    1: "Plaza España",
    2: "Barrio del Pilar",
    3: "Ensanche de Vallecas",
    4: "Retiro",
    5: "Escuelas Aguirre",
    6: "Sanchinarro",
    7: "Urb. Embajada (Barajas)",
    8: "Vallecas",
    9: "Avda. Ramón y Cajal",
    10: "C/ Arturo Soria",
    11: "Casa de Campo",
    12: "Barajas",
    13: "Plaza del Carmen",
    14: "Moratalaz",
    15: "Mendez Alvaro",
    16: "Plaza Castilla",
    17: "Plaza Elíptica",
    18: "Parque Juan Carlos I",
    19: "Plaza Tres Olivos ",
};

function map() {

    var map = L.map('map').setView([40.4169416,-3.7083759],11.2);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);

    L.control.scale().addTo(map);

    // COMIENZO DE TODOS LOS PUNTOS 
    pos = [40.4238823, -3.7122567];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");

    pos = [40.4770471, -3.7035391];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[2] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[2])\">Informacion</button>");

    pos = [40.369559, -3.604265];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[3] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[3])\">Informacion</button>");

    pos = [40.4152606, -3.6844995];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[4] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[4])\">Informacion</button>");

    pos = [40.420158, -3.697726];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[5] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[5])\">Informacion</button>");

    pos = [40.491056, -3.6696];
    prueba = L.marker(pos).addTo(map);
    prueba.bindPopup(dict[6] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[6])\">Informacion</button>");

    //    pos = [40.4563065, -3.632117];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.3868601, -3.6591803];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4514734, -3.6773491];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4400457, -3.6392422];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4193577, -3.7473445];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4769179, -3.5800258];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4192091, -3.7031662];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4079517, -3.6453104];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.3980991, -3.6868138];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4655841, -3.6887449];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.3850336, -3.7187679];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.4607255, -3.6163407];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");
    //
    //    pos = [40.5005477, -3.6897308];
    //    prueba = L.marker(pos).addTo(map);
    //    prueba.bindPopup(dict[1] + " <br> <button type=\"button\" onClick=\"loadInfo(dict[1])\">Informacion</button>");

    // FIN DE TODOS LOS PUNTOS 
}

function loadInfo(param){

    var x = document.getElementById("infoEstacion");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

    document.getElementById("nombreEstacion").innerHTML = `<h2>${param}</h2>`;
    document.getElementById("nombreProvincia").innerHTML = "SPARQL";
    document.getElementById("nombreMunicipio").innerHTML = "SPARQL";
    document.getElementById("numero").innerHTML = "SPARQL";
}

function compuestos(){

    let hora = document.getElementById("start").value;
    document.getElementById("fecha").innerHTML = `<h4>${hora}</h4>`;

    var x = document.getElementById("muestra");
    if (x.style.display === "none") {
        x.style.display = "block";
    }

}
