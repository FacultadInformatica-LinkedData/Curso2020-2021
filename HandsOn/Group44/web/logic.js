let nombre;

function map() {

    var map = L.map('map').setView([40.4169416,-3.7083759],10);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);

    L.control.scale().addTo(map);

    let pos = 40.4238823;
    for(int i = 0; i<3; i++){
    let prueba = L.marker([pos -3.7122567]).addTo(map); // plaza españa
    prueba.bindPopup("Plaza España <br> <button type=\"button\" onClick=\"loadInfo(\"Plaza España\")\">Informacion</button>");
        pos += 0.0000001;
    }


}

function hola(){
    document.write("helo :D");
}

function loadInfo(){
    var estacion = "Plaza España";
    document.getElementById("nombreEstacion").innerHTML = estacion;
}
