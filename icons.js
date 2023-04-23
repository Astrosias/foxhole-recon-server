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
