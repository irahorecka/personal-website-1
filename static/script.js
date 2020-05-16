$(document).ready(function () {
  var title = document.title
  if (title === "Home Page") {
    var htmlTags = ['h1.fade-in', 'h3', 'li'];
  } else if (title === "AC Transit") {
    var htmlTags = ['h3.fade-in', 'img.fade-in'];
  } else if (title === "YouTube to Audio") {
    var htmlTags = ['h3.fade-in', 'p.fade-in'];
  } else {
    var htmlTags = ['h3.fade-in', 'li'];
  }
  var msDelay = 0;
  var msFadeIn = 800;

  for (tag in htmlTags) {
      $(htmlTags[tag]).css('visibility','visible').hide().delay(msDelay).fadeIn(msFadeIn);
      msDelay += 300;
  }
});