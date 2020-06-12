$(document).ready(function(){
    $('#submitCity').click(function(){
       return getWeather();

    });

 });

 function getWeather(){

    var city = $('#city').val();
    if(city != ''){

       $.ajax({
          url: 'http://api.openweathermap.org/data/2.5/weather?q=' + city + "&units=imperial" + "&KEY",
          type: "GET",
          dataType: "jsonp",
          success: function(data){
             var widget = showResults(data)
             $("#showWeather").fadeIn(3000).html(widget);
             $("#city").val('');
             $("#error").html('');
          }

       });

    }else{
       $('#error').html('<div>City field cannot be empty!</div>');
    }

 }
 function showResults(data){

    return "<h2>Current Weather for "+data.name+" "+data.sys.country+"</h2>"+
    "<p><img src='http://openweathermap.org/img/wn/"+data.weather[0].icon+".png'>"+
    "<p>Weather: "+data.weather[0].main+"</p>"+
    "<p>Weather Description: "+data.weather[0].description+"</p>"+
    "<p>Temperature: "+data.main.temp+"&deg;F </p>"+
    "<p>Pressure: "+data.main.pressure+"hpa</p>"+
    "<p>Humidity: "+data.main.humidity+"%</p>"+
    "<p>Min Temperature: "+data.main.temp_min+"&deg;F</p>"+
    "<p>Max Temperature: "+data.main.temp_max+"&deg;F</p>"+
    "<p>Wind Speed: "+data.wind.speed+"m/s</p>"+
    "<p>Wind Direction: "+data.wind.deg+"&deg;</p>";

 }