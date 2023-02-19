window.onload = function() {
  function calcTime(offset) {
    let d = new Date()
    let utc = d.getTime() + (d.getTimezoneOffset() * 60000)
    let nd = new Date(utc + (3600000*offset))
    return nd
  }

  function clock() {
    let offset = document.getElementById("offset").innerHTML
    let date = calcTime(offset)
    // Seconds
    let seconds = date.getSeconds()
    document.getElementById("seconds").innerHTML = (seconds < 10 ? '0' : '') + seconds

    // Minutes
    let minutes = date.getMinutes()
    document.getElementById("minutes").innerHTML = (minutes < 10 ? '0' : '') + minutes

    // Hours
    let hours = date.getHours()
    document.getElementById("hours").innerHTML = (hours < 10 ? '0' : '') + hours
  };

  clock()
  setInterval(clock, 1000)
}