window.onload = function() {
  function clock() {
    // Seconds
    let seconds = new Date().getSeconds()
    document.getElementById("seconds").innerHTML = (seconds < 10 ? '0' : '') + seconds

    // Minutes
    let minutes = new Date().getMinutes()
    document.getElementById("minutes").innerHTML = (minutes < 10 ? '0' : '') + minutes

    // Hours
    let hours = document.getElementById("hours").innerHTML
    document.getElementById("hours").innerHTML = hours.padStart(2, '0')
  };

  clock()
  setInterval(clock, 1000)
}