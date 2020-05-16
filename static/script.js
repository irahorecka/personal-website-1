$(document).ready(function () {
  var urlCurrent = window.location.href
  var urlReference = document.referrer;
  var title = document.title
  var titleFadeAttribute = {
    "Home Page": ['h1.fade-in', 'h3.fade-in', 'li'],
    "AC Transit": ['h3.fade-in', 'img.fade-in'],
    "YouTube to Audio": ['h3.fade-in', 'p.fade-in']
  };

  if (title in titleFadeAttribute) {
    htmlTags = titleFadeAttribute[title];
  } else {
    htmlTags = ['h3.fade-in', 'li'];
  }

  // Don't fade-in h1 if previous pages were from my site
  if (title === "Home Page") {
    if (urlReference.includes('localhost:5000')) {
      $('h1.fade-in').css('visibility','visible');
      htmlTags = ['h3.fade-in', 'li'];
    }
  }

  // Don't fade in h3 if previous pages were attributed with /projects/ 
  if (urlReference.includes('/projects/') && urlCurrent.includes('/projects')) {
    $('h3.fade-in').css('visibility','visible');
    htmlTags = htmlTags.slice(1,)
  } 

  var msDelay = 0;
  var msFadeIn = 800;

  // Allow fade-in with delay
  for (tag in htmlTags) {
      $(htmlTags[tag]).css('visibility','visible').hide().delay(msDelay).fadeIn(msFadeIn);
      if (title != 'Coding Projects') {
        msDelay += 300;
      }
  }
});