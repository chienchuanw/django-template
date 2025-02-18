export async function fetchMapId() {
  const response = await fetch("/apis/map-id/");
  const data = await response.json();
  return data.mapId;
}

export async function initMap() {
  const mapId = await fetchMapId();
  const lat = parseFloat(document.getElementById("map").getAttribute("data-lat"));
  const lng = parseFloat(document.getElementById("map").getAttribute("data-lng"));
  const locationName = document.getElementById("map").getAttribute("data-name");

  const { AdvancedMarkerElement } = google.maps.marker;

  if (isNaN(lat) || isNaN(lng)) {
    console.error("Invalid coordinates, cannot load map.");
    return;
  }
  const { Map } = await google.maps.importLibrary("maps")

  const map = new Map(document.getElementById("map"), {
    center: { lat: lat, lng: lng },
    zoom: 16,
    mapId,
  });

  new AdvancedMarkerElement({
    position: { lat: lat, lng: lng },
    map: map,
    title: locationName,
  });
}

window.initMap = initMap;
