// Código para la animación de mi  texto
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

// inicio el mapa y para las direcciones
function iniciarMap() {
  
  const coord = { lat: -41.4859308, lng: -73.0027962 };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: coord,
  });

  // aquie se esta iniciando el DirectionsService y DirectionsRenderer
  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  // evento para calcular la ruta cuando se presiona en el botón
  document.getElementById("calcularRuta").addEventListener("click", function() {
    const inicio = document.getElementById("inicio").value;
    const destino = document.getElementById("destino").value;
    const cupos = document.getElementById("cupos").value; 
    calcularYMostrarRuta(inicio, destino, cupos);
  });
}

// función para calcular y mostrar la ruta con ayuda del gran chat :)
function calcularYMostrarRuta(inicio, destino, cupos) {
  const request = {
    origin: inicio,
    destination: destino,
    travelMode: 'DRIVING'
  };

  directionsService.route(request, function(result, status) {
    if (status === 'OK') {
      directionsRenderer.setDirections(result);
      guardarRutaEnBaseDeDatos(result.routes[0], inicio, destino, cupos);
    } else {
      alert("No se pudo calcular la ruta: " + status);
    }
  });
}

// función para enviar la ruta al backend
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
          cupos_disponibles: cupos 
      })
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
  })
  .then(data => {
      console.log(data); 
      alert("Ruta guardada exitosamente");
  })
  .catch(error => {
      console.error("Error al guardar la ruta:", error);
  });
}


window.onload = iniciarMap;

let currentSlide = 0;

function moveCarousel(direction) {
    const items = document.querySelectorAll('.carousel-item');
    items[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + direction + items.length) % items.length;
    items[currentSlide].classList.add('active');
    updateCarousel();
}

function updateCarousel() {
    const carouselInner = document.querySelector('.carousel-inner');
    carouselInner.style.transform = `translateX(-${currentSlide * 100}%)`;
}

document.addEventListener('DOMContentLoaded', () => {
    updateCarousel();
});

function cargarRutas() {
  $.ajax({
      url: '/gestionar_rutas',
      method: 'GET',
      success: function(data) {
          var rutaContainer = $('#ruta-container');
          rutaContainer.empty();  

          
          if (Array.isArray(data)) {
              data.forEach(function(ruta) {
                  rutaContainer.append('<div class="ruta-card">' +
                      '<h3>origen: ' + ruta.origen + '</h3>' +  
                      '<p>destino: ' + ruta.destino + '</p>' +  
                      '<p>cupos_disponibles: ' + ruta.cupos_disponibles + '</p>' +  
                      '</div>');
              });
          } else {
              console.error("Los datos devueltos no son un arreglo:", data);
          }
      },
      error: function(xhr) {
          console.error("Error al cargar las rutas:", xhr);
      }
  });
}




window.addEventListener('scroll', function() {
  var footer = document.querySelector('footer');
  var scrollPosition = window.scrollY;

  // Si el scroll es mayor que 100px, muestra el footer
  if (scrollPosition > 100) {
      footer.classList.add('show');
  } else {
      footer.classList.remove('show');
  }
});
