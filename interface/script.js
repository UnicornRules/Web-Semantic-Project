//create the map
var map = L.map('map').setView([48.833, 2.333], 12); //start map obj
var overlayMaps = {};

var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', { //create the layer
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
});
map.addLayer(osmLayer);


//L.marker([48.833, 2.333]).addTo(map).bindPopup("<b>Hello world!</b><br>I am a popup.");//add first marker

//display meteo on map click
var popup = L.popup();
async function onMapClick(e) {
    console.log(e.latlng)
    //get weather
    API_METEO='http://api.openweathermap.org/data/2.5/weather?lat='+e.latlng.lat+'&lon='+e.latlng.lng+'&appid=0c0c9aa8bb23a8054260d263e56fc1cc';
    const responseM = await fetch(API_METEO);
    const dataM = await responseM.json();
    console.log(dataM)
    //get air quality
    API_AIR="https://api.waqi.info/feed/geo:"+e.latlng.lat+";"+e.latlng.lng+"/?token=3ea0f358523452559d46c9d0c715e7908e9d993c"
    const responseA = await fetch(API_AIR);
    const dataA = await responseA.json();
    console.log(dataA)
    const message="<b>"+dataM.name+"</b><br>Temperature : "+((dataM.main.temp-273).toFixed(1))+"°C<br>Weather : "+dataM.weather[0].description+"<br>Air Quality Index : "+dataA.data.aqi
    popup
        .setLatLng(e.latlng)
        .setContent(message)
        .openOn(map);
}

map.on('click', onMapClick);


async function getVelib(){
    console.log("loading velib")
    const API="https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=10000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes";
    const response = await fetch(API);
    const velibJSON = await response.json();
    const listeStations=velibJSON.records;
    
    console.log("displaying velib");
    var velibs=[];
    for (var i = 0;i<listeStations.length;i++){
        var lat = listeStations[i].geometry.coordinates[0];
        var long = listeStations[i].geometry.coordinates[1];
        var name = listeStations[i].fields.name;
        var nbBikeAvail=listeStations[i].fields.mechanical;
        var nbElecAvail=listeStations[i].fields.ebike;
        var nbDockAvail=listeStations[i].fields.numdocksavailable;

        var textPopup="<b>"+name+"</b><br>Available mechanical bikes : "+nbBikeAvail+"<br>Available E-bikes : "+nbElecAvail+"<br>Available parking docks : "+nbDockAvail;
        
        velibs.push(L.marker([long,lat],{icon: goldIcon}).bindPopup(textPopup));
    };
    console.log(velibs);
    var layer_velibs = L.layerGroup(velibs);
    overlayMaps["Velibs"]= await layer_velibs;
}

async function getPythonApi(nomCouche,cleAPI){
    console.log("loading "+nomCouche)
    const APIPython ="http://127.0.0.1:5000/"+cleAPI;
    const response = await fetch(APIPython,{mode: 'cors'});
    const pythonJSON = await response.json();

    console.log("displaying "+nomCouche)
    console.log(pythonJSON)
    var listeCouche=[]
    for (var i = 0;i<pythonJSON.length;i++){
        var lat = pythonJSON[i].Coord[1];
        var long = pythonJSON[i].Coord[0];
        var name = pythonJSON[i].Name;
        var arond=pythonJSON[i].Arrondissements;
        var desc="";        
        var textPopup="<b>"+name+"</b><br>"+arond+"<br>"+desc;
        var iconObj=goldIcon;
        if (cleAPI!="piste"){
            var desc=pythonJSON[i].Description;
        }
        var textPopup="<b>"+name+"</b><br>"+arond+"<br>"+desc;
        var iconObj=goldIcon;
        if(nomCouche=="Fontaines"){
            iconObj=blueIcon;
        }
        if(cleAPI=="parc3"){
            iconObj=greenIcon;
        }
        if(cleAPI=="parc2"){
            iconObj=orangeIcon;
        }
        listeCouche.push(L.marker([long,lat],{icon: iconObj}).bindPopup(textPopup));
    };
    var couche = L.layerGroup(listeCouche);
    overlayMaps[nomCouche] =couche;
}

//ICON
var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });
var goldIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-gold.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });
var redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });
var blueIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });
var orangeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });



async function mainGet(){
    await getVelib();
    await getPythonApi("Fontaines","fontaines");
    await getPythonApi("Evenements","activite");
    await getPythonApi("Parcs hautement ombragé","parc3");
    await getPythonApi("Parcs faiblement ombragé","parc2");
    await getPythonApi("Pistes cyclables","piste");

}
mainGet().then(res=>{
    L.control.layers({},overlayMaps).addTo(map);
    console.log(overlayMaps);
});
    



//.geoJSON(geojsonFeature).addTo(map);


