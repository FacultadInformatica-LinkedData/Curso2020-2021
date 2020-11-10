
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('select');
  M.FormSelect.init(elems);
});

$('#district').on('change', (e) => {
  $('#neighborhood').val('');
  if(camposCorrect($(e.target).val()) === 1) {
        M.toast({html: 'The district doesn\'t exist'})
        return;
  };
  const container = $('#list-neighborhood');
  container.empty();
  neighborhoods[$(e.target).val()].sort().forEach((neighborhood) => {
    container.append(`<option value="${neighborhood}">${neighborhood}</option>`)
  })
})

$('#neighborhood').on('change', (e) => {
  const neighborhood = $(e.target).val();
  if(neighborhood === '') return;
  console.log(neighborhood);
  const districts = Object.keys(neighborhoods);
  let selectDistrict;
  for(let i = 0; i < districts.length; i++) {
    if(neighborhoods[districts[i]].includes(neighborhood)){
      selectDistrict = districts[i];
      return;
    }
  }
  console.log(selectDistrict)
  if(selectDistrict) {
    $('#district').val(selectDistrict);
  } else {
    M.toast({html: 'The neighborhood doesn\'t exist'})
  }
})

$('#filtrar').submit((e) => {
  e.preventDefault();
  const district = $('#district').val();
  const neighborhood = $('#neighborhood').val();
  const company = $('#company').val();
  const correct = camposCorrect(district, neighborhood, company);
  console.log(correct)
  if(correct === 1) {
    M.toast({html: 'The district doesn\'t exist'})
    return;
  }
  if(correct === 2) {
    M.toast({html: 'The neighborhood doesn\'t exist'})
    return;
  }
  if(correct === 3) {
    M.toast({html: 'The company doesn\'t exist'})
    return;
  }
  console.log(district)
  console.log(neighborhood)
  console.log(company)
  fetch(`http://127.0.0.1:5000/scooters?district=${district}&neighborhood=${neighborhood}&company=${company}`, {
        method: 'GET',
        headers: {
              'Access-Control-Allow-Origin': '*',
        } 
  })
    .then((response) => {
      console.log(response)
      return response.json()
    })
    .then((data) => {
      console.log(data);
      // TODO: poner dos botones al link de wikidata: district y neighborhood (abrir una nueva pestaña)
      const container = $('.card-datos .card-content');
      container.empty();
      container.append(`<a href="${data.wikidataDistrict}" target="_blank" class="waves-effect waves-teal btn pink-primary">Wikidata District</a>`)
      container.append(`<a href="${data.wikidataNeighbourhood}" target="_blank" class="waves-effect waves-teal btn pink-primary">Wikidata neighbourhood</a>`)
      renderTable(data.companies, container);
      changeGoogleMap(data.coordNB[1], data.coordNB[0], 16);
    })
})

$('.clear').click(() => {
  $('#filtrar').trigger("reset");
  changeGoogleMap();
  $('.card-datos .card-content').empty();
});

const neighborhoods = {
  'Arganzuela': ['Imperial', 'Las Acacias', 'La Chopera', 'Legazpi', 'Las Delicias', 'Palos de Moguer', 'Atocha'],
  'Carabanchel': ['Comillas', 'Opañel', 'San Isidro', 'Vista Alegre', 'Puerta Bonita', 'Buenavista', 'Abrantes'],
  'Barajas': ['Corralejos', 'Timón', 'Casco Histórico de Barajas', 'Aeropuerto', 'Alameda de Osuna'],
  'Centro': ['Palacio', 'Embajadores', 'Cortes', 'Justicia', 'Universidad', 'Sol'],
  'Chamartín': ['El Viso', 'Prosperidad', 'Ciudad Jardín', 'Hispanoamérica', 'Nueva España', 'Castilla'],
  'Chamberí': ['Gaztambide', 'Arapiles', 'Trafalgar', 'Almagro', 'Ríos Rosas', 'Vallehermoso'],
  'Ciudad Lineal': ['Ventas', 'Pueblo Nuevo', 'Quintana', 'Concepción', 'San Pascual', 'San Juan Bautista', 'Colina', 'Atalaya', 'Costillares'],
  'Hortaleza': ['Palomas', 'La Piovera', 'Canillas', 'Pinar del Rey', 'Apóstol Santiago', 'Valdefuentes'],
  'Fuencarral-El Pardo': ['El Pardo', 'Fuentelarreina', 'Peñagrande', 'El Pilar', 'La Paz', 'Valverde', 'Mirasierr', 'El Goloso'],
  'Moncloa-Aravaca': ['Casa de Campo', 'Argüelles', 'Ciudad Universitaria', 'Valdezarza', 'Valdemarín', 'El Plantío', 'Aravaca'],
  'Moratalaz': ['Pavones', 'Horcajo', 'Marroquina', 'Media Legua', 'Fontarrón', 'Vinateros'],
  'Latina': ['Los Cármenes', 'Barrio de Puerta del Ángel', 'Lucero', 'Aluche', 'Campamento', 'Cuatro Vientos', 'Las Águilas'],
  'Puente de Vallecas': ['Entrevías', 'San Diego', 'Palomeras Bajas', 'Palomeras Sureste', 'Portazgo', 'Numancia'],
  'Retiro': ['Pacífico', 'Adelfas', 'Estrella', 'Ibiza', 'Jerónimos', 'Niño Jesús',],
  'Salamanca': ['Recoletos', 'Goya', 'Fuente del Berro', 'La Guindalera', 'Lista', 'Castellana'],
  'San Blas': ['Salvador', 'Canillejas', 'Rejas', 'Rosas', 'Arcos', 'Amposta', '
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('select');
  M.FormSelect.init(elems);
});

$('#district').on('change', (e) => {
  $('#neighborhood').val('');
  if(camposCorrect($(e.target).val()) === 1) {
        M.toast({html: 'The district doesn\'t exist'})
        return;
  };
  const container = $('#list-neighborhood');
  container.empty();
  neighborhoods[$(e.target).val()].sort().forEach((neighborhood) => {
    container.append(`<option value="${neighborhood}">${neighborhood}</option>`)
  })
})

$('#neighborhood').on('change', (e) => {
  const neighborhood = $(e.target).val();
  if(neighborhood === '') return;
  console.log(neighborhood);
  const districts = Object.keys(neighborhoods);
  let selectDistrict;
  for(let i = 0; i < districts.length; i++) {
    if(neighborhoods[districts[i]].includes(neighborhood)){
      selectDistrict = districts[i];
      return;
    }
  }
  console.log(selectDistrict)
  if(selectDistrict) {
    $('#district').val(selectDistrict);
  } else {
    M.toast({html: 'The neighborhood doesn\'t exist'})
  }
})

$('#filtrar').submit((e) => {
  e.preventDefault();
  const district = $('#district').val();
  const neighborhood = $('#neighborhood').val();
  const company = $('#company').val();
  const correct = camposCorrect(district, neighborhood, company);
  console.log(correct)
  if(correct === 1) {
    M.toast({html: 'The district doesn\'t exist'})
    return;
  }
  if(correct === 2) {
    M.toast({html: 'The neighborhood doesn\'t exist'})
    return;
  }
  if(correct === 3) {
    M.toast({html: 'The company doesn\'t exist'})
    return;
  }
  console.log(district)
  console.log(neighborhood)
  console.log(company)
  fetch(`http://127.0.0.1:5000/scooters?district=${district}&neighborhood=${neighborhood}&company=${company}`, {
        method: 'GET',
        headers: {
              'Access-Control-Allow-Origin': '*',
        } 
  })
    .then((response) => {
      console.log(response)
      return response.json()
    })
    .then((data) => {
      console.log(data);
      // TODO: poner dos botones al link de wikidata: district y neighborhood (abrir una nueva pestaña)
      const container = $('.card-datos .card-content');
      container.empty();
      container.append(`<a href="${data.wikidataDistrict}" target="_blank" class="waves-effect waves-teal btn pink-primary">Wikidata District</a>`)
      container.append(`<a href="${data.wikidataNeighbourhood}" target="_blank" class="waves-effect waves-teal btn pink-primary">Wikidata neighbourhood</a>`)
      renderTable(data.companies, container);
      changeGoogleMap(data.coordNB[1], data.coordNB[0], 16);
    })
})

$('.clear').click(() => {
  $('#filtrar').trigger("reset");
  changeGoogleMap();
  $('.card-datos .card-content').empty();
});

const neighborhoods = {
  'Arganzuela': ['Imperial', 'Las Acacias', 'La Chopera', 'Legazpi', 'Las Delicias', 'Palos de Moguer', 'Atocha'],
  'Carabanchel': ['Comillas', 'Opañel', 'San Isidro', 'Vista Alegre', 'Puerta Bonita', 'Buenavista', 'Abrantes'],
  'Barajas': ['Corralejos', 'Timón', 'Casco Histórico de Barajas', 'Aeropuerto', 'Alameda de Osuna'],
  'Centro': ['Palacio', 'Embajadores', 'Cortes', 'Justicia', 'Universidad', 'Sol'],
  'Chamartín': ['El Viso', 'Prosperidad', 'Ciudad Jardín', 'Hispanoamérica', 'Nueva España', 'Castilla'],
  'Chamberí': ['Gaztambide', 'Arapiles', 'Trafalgar', 'Almagro', 'Ríos Rosas', 'Vallehermoso'],
  'Ciudad Lineal': ['Ventas', 'Pueblo Nuevo', 'Quintana', 'Concepción', 'San Pascual', 'San Juan Bautista', 'Colina', 'Atalaya', 'Costillares'],
  'Hortaleza': ['Palomas', 'La Piovera', 'Canillas', 'Pinar del Rey', 'Apóstol Santiago', 'Valdefuentes'],
  'Fuencarral-El Pardo': ['El Pardo', 'Fuentelarreina', 'Peñagrande', 'El Pilar', 'La Paz', 'Valverde', 'Mirasierr', 'El Goloso'],
  'Moncloa-Aravaca': ['Casa de Campo', 'Argüelles', 'Ciudad Universitaria', 'Valdezarza', 'Valdemarín', 'El Plantío', 'Aravaca'],
  'Moratalaz': ['Pavones', 'Horcajo', 'Marroquina', 'Media Legua', 'Fontarrón', 'Vinateros'],
  'Latina': ['Los Cármenes', 'Barrio de Puerta del Ángel', 'Lucero', 'Aluche', 'Campamento', 'Cuatro Vientos', 'Las Águilas'],
  'Puente de Vallecas': ['Entrevías', 'San Diego', 'Palomeras Bajas', 'Palomeras Sureste', 'Portazgo', 'Numancia'],
  'Retiro': ['Pacífico', 'Adelfas', 'Estrella', 'Ibiza', 'Jerónimos', 'Niño Jesús',],
  'Salamanca': ['Recoletos', 'Goya', 'Fuente del Berro', 'La Guindalera', 'Lista', 'Castellana'],
  'San Blas': ['Salvador', 'Canillejas', 'Rejas', 'Rosas', 'Arcos', 'Amposta', 'Hellin', 'Simancas'],
  'Tetuán': ['Bellas Vistas', 'Cuatro Caminos', 'Castillejos', 'Almenara', 'Valdeacederas', 'Berruguete'],
  'Usera': ['Orcasitas', 'Orcasur', 'San Fermín', 'Almendrales', 'Moscardó', 'El Zofío', 'Pradolongo'],
  'Vicálvaro': ['Casco Histórico de Vicálvaro', 'Ambroz'],
  'Villaverde': ['Villaverde Alto, Casco Histórico de Villaverde', 'San Cristóbal', 'Butarque', 'Los Rosales', 'Los Ángeles'],
  'Villa de Vallecas': ['Casco Histórico de Vallecas', 'Santa Eugenia'],
}

function renderTable(companies, container) {
  const table = document.createElement('table');
  const thead = document.createElement('thead');
  const tbody = document.createElement('tbody');
  const tr = document.createElement('tr');
  const th1 = document.createElement('th');
  const th2 = document.createElement('th');
  th1.innerText = 'Company';
  th2.innerText = 'Scooters';
  tr.appendChild(th1);
  tr.appendChild(th2);
  thead.appendChild(tr);
  table.appendChild(thead)
  companies.forEach((company) => {
    const tr = document.createElement('tr');
    const td1 = document.createElement('td');
    const td2 = document.createElement('td');
    td1.innerText = Object.keys(company)[0]
    td2.innerText = Object.values(company)[0]
    tr.appendChild(td1);
    tr.appendChild(td2);
    tbody.appendChild(tr);
  });
  table.appendChild(tbody)
  container.append(table);
}

function camposCorrect(district, neighborhood, company) {
  if(!Object.keys(neighborhoods).includes(district)) return 1;
  if(!Object.values(neighborhoods).flat().includes(neighborhood)) return 2;
  if(!['All', 'Acciona', 'Taxify', 'Koko', 'Ufo', 'Rideconga', 'Flash', 'Lime', 'Wind', 'Bird', 'RebyRides', 'Movo', 'Mygo', 'JumpUber', 'SjvConsulting'].includes(company)) return 3;
  return 0; 
}

function changeGoogleMap(y = 40.5281307, x = -3.7000000, zoom = 11) {
  console.log(x, y, zoom)
  document.getElementById('gmap_canvas').src = `https://maps.google.com/?ll=${y},${x}&z=${zoom}&t=m&output=embed`
}