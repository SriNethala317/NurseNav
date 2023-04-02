const map = new mapboxgl.Map({
  container: 'map', // container ID
  style: 'mapbox://styles/mapbox/streets-v12', // style URL
  center: [-96.7511073, 32.9858304], // starting position [lng, lat]
  zoom: 12, // starting zoom
});

map.addControl(
  new mapboxgl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    },
// When active the map will receive updates to the device's location as it changes.
    trackUserLocation: true,
// Draw an arrow next to the location dot to indicate which direction the device is heading.
    showUserHeading: true
  })
);

document.querySelectorAll('.tag').forEach(tag => tag.addEventListener('click', function() {
  this.classList.toggle('selected');
}));
