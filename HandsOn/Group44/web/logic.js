let nombre;

function map() {

    var map = L.map('map').setView([40.4169416,-3.7083759],10);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);

    L.control.scale().addTo(map);

    let pos = 40.4238823;
    var i;


    for(i = 0; i<3; i++){
        let estacion = "Plaza España"; // aqui llamamaos a sparql
        let prueba = L.marker([pos, -3.7122567]).addTo(map);

        prueba.bindPopup(estacion + " <br> <button type=\"button\" onClick=\"loadInfo()\">Informacion</button>");

        pos = pos + 0.01;
    }
}

function loadInfo(){
    document.getElementById("nombreEstacion").innerHTML = "<h2>Ejemplo de estacion</h2>";
    document.getElementById("nombreProvincia").innerHTML = "Ejemplo de provinicia";
    document.getElementById("nombreMunicipio").innerHTML = "Ejemplo de municipio";
    document.getElementById("numero").innerHTML = "Ejemplo de estacion numero";
}

function tmp(){
    alert("Hola macarrones :D");
}
