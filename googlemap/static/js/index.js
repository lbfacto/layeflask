var map = L.map('map').setView([14.6898, -17.4480], 0);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Calculateur de distance sur map SENEGAL By Abdoulaye ba UVS M2 Dig Data',
    minZoom: 1,
    maxZoom: 20
}).addTo(map);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([14.6898, -17.4480]).addTo(map)
    .bindPopup('DAKAR.<br>SENEGAL.')
    .openPopup();
L.marker([14.7841, -16.9395]).addTo(map)
    .bindPopup('Thies.<br>SENEGAL.')
    .openPopup();
L.marker([14.6443, -16.2488]).addTo(map)
    .bindPopup('Diorurbel.<br>SENEGAL.')
    .openPopup();
L.marker([12.5432, -16.2666]).addTo(map)
    .bindPopup('Casamance.<br>SENEGAL.')
    .openPopup();
L.marker([16.013, -16.425]).addTo(map)
    .bindPopup('Saint Louis.<br>SENEGAL.')
    .openPopup();
L.marker([12.5532, -12.1935]).addTo(map)
    .bindPopup('Kedougou.<br>SENEGAL.')
    .openPopup();
//activation gestion des itineraires

L.Routing.control({
    geocoder: L.Control.Geocoder.nominatim(),
    lineOptions: {
        style: [{
                color: '#839c49',
                opacity: 1,
                weight: 7
            }

        ]
    },
    router: new L.Routing.osrmv1({
        language: 'fr',
        profile: 'trafic',
        profile: 'travel'
    })

}).addTo(map)