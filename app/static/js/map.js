// create neighborhood dropdown
let neighborhoodList = ['Albany Park', 'Archer Heights', 'Armour Square', 'Ashburn', 'Auburn Gresham', 'Austin', 'Avalon Park', 'Avondale', 'Belmont Cragin', 'Beverly', 'Bridgeport', 'Brighton Park', 'Burnside', 'Calumet Heights', 'Chatham', 'Chicago Lawn', 'Clearing', 'Douglas', 'Dunning', 'East Garfield Park', 'East Side', 'Edgewater', 'Edison Park', 'Englewood', 'Forest Glen', 'Fuller Park', 'Gage Park', 'Garfield Ridge', 'Grand Boulevard', 'Greater Grand Crossing', 'Hegewisch', 'Hermosa', 'Humboldt Park', 'Hyde Park', 'Irving Park', 'Jefferson Park', 'Kenwood', 'Lakeview', 'Lincoln Park', 'Lincoln Square', 'Little Village', 'Logan Square', 'Loop', 'Lower West Side', 'McKinley Park', 'Montclare', 'Morgan Park', 'Mount Greenwood', 'Near North Side', 'Near South Side', 'Near West Side', 'New City', 'North Center', 'North Lawndale', 'North Park', 'Norwood Park', "O'Hare", 'Oakland', 'Portage Park', 'Pullman', 'Riverdale', 'Rogers Park', 'Roseland', 'South Chicago', 'South Deering', 'South Lawndale', 'South Shore', 'The Loop', 'Uptown', 'Washington Heights', 'Washington Park', 'West Elsdon', 'West Englewood', 'West Garfield Park', 'West Lawn', 'West Pullman', 'West Ridge', 'West Town', 'Woodlawn'];
let dropdown = d3.select("#neighborhoodDropdown");
dropdown.attr("class","dd")
for (let i = 0; i < neighborhoodList.length; i++){
    dropdown.append("option").text(neighborhoodList[i]).attr("value",neighborhoodList[i])
};

// create zipcode dropdown
let zipcodeList =     ['60601', '60602', '60603', '60604', '60605', '60606', '60607', '60608', '60609', '60610', '60611',
       '60612', '60613', '60614', '60615', '60616', '60617', '60618', '60619', '60620', '60621', '60622', '60623',
       '60624', '60625', '60626', '60628', '60629', '60630', '60631', '60632', '60633', '60634', '60636', '60637',
       '60638', '60639', '60640', '60641', '60642', '60643', '60644', '60645', '60646', '60647', '60649', '60651',
       '60652', '60653', '60654', '60655', '60656', '60657', '60659', '60660', '60661', '60666', '60707', '60827'];
let dropdown2 = d3.select("#zipDropdown");
dropdown2.attr("class","dd")
for (let i = 0; i < zipcodeList.length; i++){
    dropdown2.append("option").text(zipcodeList[i]).attr("value",i)
};


let failLayer = new L.LayerGroup();
let riskLayer = new L.LayerGroup();

let overlayMaps = {
    'Top 10 Fail': failLayer,
    'Top 10 Risk': riskLayer
};

let map = L.map('map', {
    center: [41.8781, -87.6298],
    zoom: 13,
    layers:[failLayer, riskLayer]
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.control.layers(null, overlayMaps, {collapsed: false}).addTo(map);

onNeighborChange(failLayer, riskLayer)

// map chanes on future dropdown changes
let neighborhoodDropdown = d3.select('#neighborhoodDropdown');
neighborhoodDropdown.on('change', function() { onNeighborChange(failLayer, riskLayer) }, )




function onNeighborChange(failLayer, riskLayer, nbhd="Albany Park") {

    let neighborhoodDropdown = d3.select('#neighborhoodDropdown');
    let selectedNeighborhood = neighborhoodDropdown.property("value");
   
    if(selectedNeighborhood == ''){
        selectedNeighborhood = nbhd;
    }

    // Clear existing markers
    if(failLayer){
    failLayer.clearLayers();
    }

    if(riskLayer){
    riskLayer.clearLayers();
    }
    console.log(selectedNeighborhood)
    d3.csv("./static/data/modified_food_inspections.csv")
        .then(markers => {
            let neighborhoodMarkers = markers.filter(i => i.Neighborhood == selectedNeighborhood)
            console.log(neighborhoodMarkers)
            neighborhoodMarkers.forEach(marker => {
                let lat = parseFloat(marker.Latitude);
                let lon = parseFloat(marker.Longitude);
                let name = marker['DBA Name'];
                let address = marker.Address;
                let total_fail = marker["Total Fail"];
                let total_risk = marker["Total Risk"];
                let top_fail = marker['Top 10 Fail']
                let top_risk = marker['Top 10 Risk']
                // console.log(top_fail)

                if (top_fail == 'True') {
                    L.circleMarker([lat, lon], {
                        color: 'rgba(255,0,0,0.8)',
                        radius: 8
                        })
                        .bindPopup(`
                            <strong>${name}</strong><br>
                            Address: ${address}<br>
                            Total Fail: ${total_fail}<br>
                            Total Risk: ${total_risk}
                        `)
                        .addTo(failLayer);
                }

                if (top_risk == 'True') {
                    console.log('it ran')
                    L.circleMarker([lat, lon], {
                        color: 'rgba(0,0,255,0.8)',
                        radius: 8
                        })
                        .bindPopup(`
                            <strong>${name}</strong><br>
                            Address: ${address}<br>
                            Total Fail: ${total_fail}<br>
                            Total Risk: ${total_risk}
                        `)
                        .addTo(riskLayer);
                }
                map.setView(new L.LatLng(lat, lon), 14);
            });
            
        });

};

let legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {
    let div = L.DomUtil.create('div', 'legend');
    div.innerHTML += '<i class="fail"></i> Fail<br>';
    div.innerHTML += '<i class="risk"></i> Risk';
    return div;
};

legend.addTo(map);

function removeDuplicates(arr) {
    return arr.filter((item, index) => arr.indexOf(item) === index);}