// Código existente para la animación de texto
let app = document.getElementById('typewriter');

let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});

typewriter
  .pauseFor(2500)
  .typeString('Somos Rueda Solidaria')
  .pauseFor(200)
  .deleteChars(10)
  .start();



// Función para inicializar el mapa y los servicios de direcciones
function iniciarMap() {
  // Configuración inicial del mapa
  const coord = { lat: -41.4859308, lng: -73.0027962 };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: coord,
  });

  // Crear un marcador inicial en la coordenada especificada
  const marker = new google.maps.Marker({
    position: coord,
    map: map,
  });

  // Inicializar DirectionsService y DirectionsRenderer
  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  // Evento para calcular la ruta cuando se hace clic en el botón
  document.getElementById("calcularRuta").addEventListener("click", function() {
    const inicio = document.getElementById("inicio").value;
    const destino = document.getElementById("destino").value;
    const cupos = document.getElementById("cupos").value; // Obtener el valor de los cupos
    calcularYMostrarRuta(inicio, destino, cupos);
  });
}

// Función para calcular y mostrar la ruta
function calcularYMostrarRuta(inicio, destino, cupos) {
  const request = {
    origin: inicio,
    destination: destino,
    travelMode: 'DRIVING'
  };

  directionsService.route(request, function(result, status) {
    if (status === 'OK') {
      directionsRenderer.setDirections(result);
      // Guardar la ruta en tu base de datos
      guardarRutaEnBaseDeDatos(result.routes[0], inicio, destino, cupos);
    } else {
      alert("No se pudo calcular la ruta: " + status);
    }
  });
}

// Función para enviar la ruta al backend
function guardarRutaEnBaseDeDatos(ruta, inicio, destino, cupos) {
  const puntos = ruta.overview_path.map(punto => ({
      lat: punto.lat(),
      lng: punto.lng()
  }));

  fetch('/guardar_ruta', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
          origen: inicio,
          destino: destino,
          puntos: puntos,
          cupos_disponibles: cupos // Incluir la cantidad de cupos
      })
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
  })
  .then(data => {
      console.log(data); // Agregar esto para ver la respuesta del servidor
      alert("Ruta guardada exitosamente");
  })
  .catch(error => {
      console.error("Error al guardar la ruta:", error);
  });
}

// Asegúrate de llamar a la función iniciarMap cuando cargue la página
window.onload = iniciarMap;
