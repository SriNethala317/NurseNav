feather.replace();

if ("serviceWorker" in navigator) {
  // register service worker
  navigator.serviceWorker.register("/service-worker.js");
}

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
  document.querySelector('#results').innerHTML = '';
  this.classList.toggle('selected');
  let location = [32.9858304, -96.7511073];
  let tags = Array.from(document.querySelectorAll('.selected')).map(x => x.innerText);
  console.log(tags);
  fetch("/nurses", {
    method: "POST",
    body: JSON.stringify({ location, tags }),
    headers: {
      "Content-Type": "application/json"
    }
  })
  .then(response => response.json())
  .then(result => {
    const fragment = document.createDocumentFragment();
    for (let i = 0; i < result.length; i++) {
      const div = document.createElement('div');
      div.classList.add('result');
      div.innerHTML = `
        <b>Name:</b> ${result[i].name}<br>
        <b>Phone:</b> ${result[i].phone}
        <p>${result[i].description}</p>
        <b>Distance:</b> ${result[i].distance.toFixed(2)}<br>
        <b>Tags:</b> ${result[i].tags}
      `;
      fragment.appendChild(div);
    }
    document.querySelector('#results').appendChild(fragment);
  });
}));
//   fetch("/nurses",{
//     method: 'POST',
//     tags,
//     location
//   }).then(response => response.json())
//     .then(data => console.log(data))
// }))
// .catch(console.error);
