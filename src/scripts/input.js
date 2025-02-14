// maps.js
function initMap() {
  const lat = parseFloat(document.getElementById("map").getAttribute("data-lat"));
  const lng = parseFloat(document.getElementById("map").getAttribute("data-lng"));
  const locationName = document.getElementById("map").getAttribute("data-name");

  if (isNaN(lat) || isNaN(lng)) {
    console.error("Invalid coordinates, cannot load map.");
    return;
  }

  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: lat, lng: lng },
    zoom: 16,
  });

  new google.maps.Marker({
    position: { lat: lat, lng: lng },
    map: map,
    title: locationName,
  });
}
