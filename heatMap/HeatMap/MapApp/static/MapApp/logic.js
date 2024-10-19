
let map;
let maxIntensity;


async function initMap() {

    const response = await fetch('/data');
    const data = await response.json()

    const heatMapData = parseCSV(data)

  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 39.32000, lng: -111.0937 },
    zoom: 7,
  });

  var heatmap = new google.maps.visualization.HeatmapLayer({
    data: heatMapData,
    opacity: 0.8,
  })
    heatmap.set("maxIntensity", maxIntensity)
    heatmap.setMap(map);
}

function parseCSV(data) {
    const heatmapData = [];
    maxIntensity = data[0][3]
    // Skip the header row and process each row
    for (let i = 1; i < data.length; i++) {

        const lat = parseFloat(data[i][0]);
        const lng = parseFloat(data[i][1]);
        const intensity = parseFloat(data[i][2]);


        // Push the data point to heatmapData array
        heatmapData.push({
            location: new google.maps.LatLng(lat, lng),
            weight: intensity,
        });
    }
    return heatmapData;
}

