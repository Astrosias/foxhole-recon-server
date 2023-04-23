var iconsFolder = "images/icons/";

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

var geojsonLayerWarapi = new L.GeoJSON.AJAX("warapi.geojson", {
  pointToLayer: function (feature, latlng) {
            return L.marker(latlng, {icon: forgeIcon(feature.properties.name, feature.properties.teamId)});
    },
  onEachFeature: onEachFeature
});


//plTrainPost[0] = L.polyline(latlonPost, {color: 'black', weight: '5'});
//plTrainPost[1] = L.polyline(latlonPost, {color: 'black', weight: '3',  dashArray: '20, 20', dashOffset: '0'});
//plTrainPost[2] = L.polyline(latlonPost, {color: 'white', weight: '3', dashArray: '20, 20', dashOffset: '20'});
//var CPrePostLayer = L.layerGroup(plTrainPost[0], plTrainPost[1], plTrainPost[2]]);
