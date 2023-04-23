const styledNames = ["facility", "defense1", "defense2", "defense3", "rails", "partisanRoad"]

const styleFacility = {fillColor:'PaleGreen',color: 'green',weight:0,fillOpacity:0.3, dashArray: '3'};
const styleDefenseLight = {color: 'green',weight:1, dashArray: '5'};
const styleDefenseMedium = {color: 'green',weight:3, dashArray: '1'};
const styleDefenseHeavy = {color: 'green',weight:6};
const styleRails = {color: 'black',weight:5, dashArray: '1'};
const stylePartisanRoad = {color: 'red',weight:3, dashArray: '1'};

function getStyle(name){
   if (name === 'facility'){
        return styleFacility
   }
   if (name === 'rails'){
        return styleRails
   }
   if (name === 'defense1'){
        return styleDefenseLight
   }
   if (name === 'defense2'){
        return styleDefenseMedium
   }
   if (name === 'defense3'){
        return styleDefenseHeavy
   }
   if (name === 'partisanRoad'){
        return stylePartisanRoad
   }
};
