var iconsFolder = "images/icons/";
const styledNames = ["facility", "defense1", "defense2", "defense3", "rails", "partisanRoad"];
const styleFacility = {fillColor:'PaleGreen',color: 'green',weight:0,fillOpacity:0.3, dashArray: '3'};
const styleDefenseLight = {color: 'green',weight:1, dashArray: '5'};
const styleDefenseMedium = {color: 'green',weight:3, dashArray: '2'};
const styleDefenseHeavy = {color: 'green',weight:6};
const styleRails = {color: 'black',weight:5, dashArray: '6'};
const stylePartisanRoad = {color: 'red',weight:3, dashArray: '1'};
const styleObs = {color: 'green',weight:0, fillColor: 'green'};

const translation = {"obs": "Watchtower"};


function forgeIcon(name, teamId) {
    var iconPath = iconsFolder + "MapIcon" + name;
    if (teamId == "COLONIALS" ) {
        iconPath = iconPath + "Colonial.png";
    }
    else if (teamId == "WARDENS" ) {
        iconPath = iconPath + "Warden.png";
    }
    else if (teamId == "NONE" ) {
        iconPath = iconPath + ".png";
    }
    else {
        iconPath = iconPath + ".png";
        console.log("Incorrect teamId: " + teamId)
    }
    return L.icon({iconUrl: iconPath, iconSize: [20, 20]});
}

function onEachFeature(feature, layer) {
  layer.bindPopup(feature.properties.name);
}
function onEachFeatureRecon(feature, layer) {
  layer.bindPopup(feature.properties.popup);
  if (!(feature.properties.shape.includes("obs"))){
    layer.setStyle(getStyle(feature.properties.shape));
  }

//  console.log("style set");
//  console.log(layer);
//  console.log(feature);
//  if (feature.properties.shape === 'obsBunkerT3Colonial'){
//    var coords = L.latLng(feature.geometry.coordinates[0], feature.geometry.coordinates[1]);
//      console.log(coords);
//     var circle_tmp = L.circle(coords, {weight:0, radius:ratio*180});
//     circle_tmp.addTo(map);
//  }
//  else if (feature.properties.shape === 'obsBunkerT2Colonial'){
//      var coords = L.latLng(feature.geometry.coordinates[0], feature.geometry.coordinates[1]);
//           console.log(coords);
//     var circle_tmp = L.circle(coords, {weight:0, radius:ratio*120});
//     circle_tmp.addTo(map);
//  }
//  else if (feature.properties.shape === 'obsBunkerT1Colonial'){
//      var coords = L.latLng(feature.geometry.coordinates[0], feature.geometry.coordinates[1]);
//      console.log(coords);
//     var circle_tmp = L.circle(coords, {weight:0, radius:ratio*80});
//     console.log(circle_tmp);
//     circle_tmp.addTo(map);
//  }
  console.log("done");
}

function extractFeatures(name){
    var teamid = "NONE";
    if (name.includes("Colonial")){
    teamId = "COLONIALS";
    name = name.replace("Colonial", "");
    }
    else if (name.includes("Warden")){
    teamid = "WARDENS";
    name = name.replace("Warden", "");
    }

    name = name.replace(/obs.*/, "Watchtower");
    return [name, teamid];
}

function getStyle(name){
   if (name === 'facilityColonial'){
        return styleFacility
   }
   else if (name === 'rails'){
        return styleRails
   }
   else if (name === 'defense1Colonial'){
        return styleDefenseLight
   }
   else if (name === 'defense2Colonial'){
        return styleDefenseMedium
   }
   else if (name === 'defense3Colonial'){
        return styleDefenseHeavy
   }
   else if (name === 'partisanRoad'){
        return stylePartisanRoad
   }
   else if (name === 'obs'){
        return styleFacility
   }
};

const getCircularReplacer = () => {
  const seen = new WeakSet();
  return (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) {
        return;
      }
      seen.add(value);
    }
    return value;
  };
};
function export2txt(originalData, name) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(originalData, getCircularReplacer())], {
    type: "text/plain"
  }));
  a.setAttribute("download", name);
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

var geojsonLayerWarapi = new L.GeoJSON.AJAX("warapi.geojson", {
  pointToLayer: function (feature, latlng) {
            return L.marker(latlng, {icon: forgeIcon(feature.properties.name, feature.properties.teamId)});
    },
  onEachFeature: onEachFeature
});

var geojsonLayerRecon = new L.GeoJSON.AJAX("recon.geojson", {
  pointToLayer: function (feature, latlng) {
        var shape = extractFeatures(feature.properties.shape)[0];
        var teamid = extractFeatures(feature.properties.shape)[1];
        console.log(feature.properties.shape);
        if (feature.properties.shape === 'obsBunkerT3Colonial'){
            var circle_tmp = L.circle(latlng, {weight:0, radius:ratio*180, fillColor: 'green', fillOpacity:0.15});
        }
        else if (feature.properties.shape === 'obsBunkerT2Colonial'){
            var circle_tmp = L.circle(latlng, {weight:0, radius:ratio*120, fillColor: 'green', fillOpacity:0.15});
        }
        else if (feature.properties.shape === 'obsBunkerT1Colonial'){
            console.log("T1");
            var circle_tmp = L.circle(latlng, {weight:0, radius:ratio*80, fillColor: 'green', fillOpacity:0.15});
            console.log(circle_tmp);
        }
        var marker = L.marker(latlng, {icon: forgeIcon(shape, teamId)});
        console.log(circle_tmp);
        if (typeof circle_tmp !== 'undefined') {
            console.log("B");
            return L.layerGroup([marker, circle_tmp]);
//            return circle_tmp;
        }
        else {
            return marker;
        }
    },
  onEachFeature: onEachFeatureRecon
});

function sendJson(jsonData, mode){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/tmp_json/" + mode, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        value: jsonData
    }));
}

//plTrainPost[0] = L.polyline(latlonPost, {color: 'black', weight: '5'});
//plTrainPost[1] = L.polyline(latlonPost, {color: 'black', weight: '3',  dashArray: '20, 20', dashOffset: '0'});
//plTrainPost[2] = L.polyline(latlonPost, {color: 'white', weight: '3', dashArray: '20, 20', dashOffset: '20'});
//var CPrePostLayer = L.layerGroup(plTrainPost[0], plTrainPost[1], plTrainPost[2]]);
