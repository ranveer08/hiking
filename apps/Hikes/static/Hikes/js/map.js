$(document).ready(function(){
  $('#btnPath').click(function(){
    var destination = $('#destination').val();
    if(destination == '')
    {
      document.getElementById("error").innerHTML = "required field!!";
    }
    else
    $("#mapArea").css({'display':'block'});
    return findPath();

  });
});
var points = [{}, {}];
var map;
function findPath()
{
  if(navigator.geolocation)
  {
    navigator.geolocation.getCurrentPosition(onSuccess, onError,
      {maximumAge:60*1000,
       timeout: 5*60*1000,
       enableHighAccuracy: true});
  }
  else
  document.getElementById("error").innerHTML = "Your browser does not support HTML5 Geolocation!!";
}
function onSuccess(position)
{
  points[0].lat = position.coords.latitude;
  points[0].long = position.coords.longitude;

  var localAddress = document.getElementById("destination").value.replace(" ","+");

  var xmlhttpAddr = new XMLHttpRequest();
  var url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ localAddress + "&secretkey";
  xmlhttpAddr.open("GET", url, false);
  xmlhttpAddr.send();

  if(xmlhttpAddr.readyState == 4 && xmlhttpAddr.status == 200)
  {
    var result = xmlhttpAddr.responseText;
    var jsResult = eval("(" + result + ")");

    points[1].lat = jsResult.results[0].geometry.location.lat;
    points[1].long = jsResult.results[0].geometry.location.lng;
  }
  var mapOptions = {
    center: new google.maps.LatLng(points[0].lat, points[0].long),
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("mapArea"), mapOptions);
  var latlngbounds = new google.maps.LatLngBounds();
  for(var i = 0; i<points.length; i++)
  {
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(points[i].lat, points[i].long),
      map:map
    });
    latlngbounds.extend(marker.position);
  }
  map.fitBounds(latlngbounds);
  drawPath();

}
function drawPath()
{

  var directionsService = new google.maps.DirectionsService();
  var poly = new google.maps.Polyline({strokeColor: "#FF0000", strokeWeight:4});

  var request = {
    origin: new google.maps.LatLng(points[0].lat, points[0].long),
    destination: new google.maps.LatLng(points[1].lat, points[1].long),
    travelMode: google.maps.DirectionsTravelMode.DRIVING
  };
  directionsService.route(request, function(response, status){
    if(status == google.maps.DirectionsStatus.OK)
    {
      new google.maps.DirectionsRenderer({
        map:map,
        polylineOptions: poly,
        directions: response
      });
    }
  })
}

function onError(error)
{
  switch(error.code)
  {
    case PERMISSION_DENIED:
      alert("User denied permission");
      break;
    case TIMEOUT:
      alert("Geolocation timed out");
      break;
    case POSITION_UNAVAILABLE:
      alert("Geolocation information is not available");
      break;
    default:
      alert("Unknown error");
      break;
  }
}
// var watchId, geocoder, startLat, startLong;
// var start = 1;
// window.onload = function()
// {
//   if(navigator.geolocation)
//   {
//     watchId = navigator.geolocation.watchPosition(onSuccess, onError,
//        {maximumAge:60*1000,
//         timeout: 5*60*1000,
//         enableHighAccuracy: true});
//   }
// }
// function onSuccess(position)
// {
//   var currentLat = position.coords.latitude;
//   var currentLong = position.coords.longitude;

//   if(start == 1)
//   {
//     startLat = currentLat;
//     startLong = currentLong;
//     start = 0;
//   }

//   var geocoder = new google.maps.Geocoder();
//   var latlong = new google.maps.LatLng(currentLat, currentLong);
//   geocoder.geocode({'latLng': latlong}, function(results, status){
//     if(status == google.maps.GeocoderStatus.OK)
//     {
//       if(results)
//       {
//         document.getElementById("location").innerHTML = "Your are near " + results[0].formatted_address;
//       }

//     }
//     else
//         alert("Could not get the geolocation information");
//   });

//   var mapOptions = {
//     center: new google.maps.LatLng(startLat, startLong),
//     zoom: 10,
//     mapTypeId: google.maps.MapTypeId.ROADMAP
//   };
//   var map = new google.maps.Map(document.getElementById("mapArea"), mapOptions);
//   var marker = new google.maps.Marker({
//     position: latlong,
//     map: map,
//     title: "My first marker",
//     animation: google.maps.Animation.BOUNCE
//   });
//   var info = new google.maps.InfoWindow({
//     content: "My information window!!!"
//   });
//   google.maps.event.addListener(marker, "click", function(){
//     info.open(map, marker);
//   })

  
// }
// function onError(error)
// {
//   switch(error.code)
//   {
//     case PERMISSION_DENIED:
//       alert("User denied permission");
//       break;
//     case TIMEOUT:
//       alert("Geolocation timed out");
//       break;
//     case POSITION_UNAVAILABLE:
//       alert("Geolocation information is not available");
//       break;
//     default:
//       alert("Unknown error");
//       break;
//   }
// }

// var watchId= false;
// function watchPosition()
// {
//   if (navigator.geolocation)
//   {
//     watchId = navigator.geolocation.watchPosition(successPosition, failurePosition, {
//       enableHighAccuracy: false,
//       timeout: 3000,
//       maximumAge: 4000
//     });
//   }
//   else
//       document.getElementById("result").innerHTML = "Your browser does not support Geoloaction API";
// }

// function failurePosition(error)
// {
//   alert("Error Code: " + error.code + " Error Message: " + error.message)
// }

// function stopWatching()
// {
//   navigator.geolocation.clearWatch(watchId);
// }
// function successPosition(position)
// {
//   var lat = position.coords.latitude;
//   var long = position.coords.longitude;

//   document.getElementById("result").innerHTML = "Latitude: " + lat + "<br/>Longitude: " + long;
  // alert("Accuracy: " + position.coords.accuracy);
  // alert("Altitude: " + position.coords.altitude);
  // alert("Altitude Accuracy: " + position.coords.altitudeAccuracy);
  // alert("Direction: " + position.coords.heading);
  // alert("speed: " + position.coords.speed);
  // alert("Timestamp: " + position.timestamp);
//}
