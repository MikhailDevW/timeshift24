window.onload = function() {
  function clock() {
    // Seconds
    let seconds = number (document.getElementById("seconds").innerHTML)
    document.getElementById("seconds").innerHTML = (seconds < 10 ? '0' : '') + seconds;

    // Minutes
    let minutes = number (document.getElementById("minutes").innerHTML)
    document.getElementById("minutes").innerHTML = (minutes < 10 ? '0' : '') + minutes;

    // Hours
    let hours = number (document.getElementById("hours").innerHTML)
    document.getElementById("hours").innerHTML = (minutes < 10 ? '0' : '') + hours;
  };

  clock()
  setInterval(clock, 1000);
  
}