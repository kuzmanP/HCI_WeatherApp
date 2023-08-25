const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');
const currentWeatherItemsEl = document.getElementById('current-weather-items');
const timeZoneEl = document.getElementById('time-zone');
const contryEl = document.getElementById('country');
const weatherForecastEl = document.getElementById('weather-forecast');
const temperatureEl = document.getElementById('current-temp');


/* to make the app real-time */
const days = [ 'Sunday', 'Monday', 'Tuesday', 
'Wednesday', 'Thursday', 'Friday', 'Saturday']

const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 
'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

setInterval(() => {
    const time = new Date();
    const month = time.getMonth();
    const date = time.getDate();
    const day = time.getDay();
    const hour = time.getHours();

    const timeIn12HourFormat = hour >= 13 ? hour %12 : hour
    const minutes = time.getMinutes();
    const ampm = hour >=12 ? 'PM' : 'AM';

    /* make the time correspond to the current time */
    timeEl.innerHTML = timeIn12HourFormat + ':' + minutes + ' ' + `<span id="am-pm">${ampm}</span>`;
    dateEl.innerHTML = days[day] +  ', ' + date + ' ' + months[month]

}, 1000);