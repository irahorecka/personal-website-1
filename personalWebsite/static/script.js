$(document).ready(function () {
  fadeIn();
});


// Function to handle fade-out of text above when scrolling down
$(window).on("load",function() {
  function fade(pageLoad) {
    var windowTop=$(window).scrollTop(), windowBottom=windowTop+$(window).innerHeight();
    var min=0.3, max=1.0, threshold=0.01;
    
    $(".fade-scroll").each(function() {
      /* Check the location of each desired element */
      var objectHeight=$(this).outerHeight(), objectTop=$(this).offset().top, objectBottom=$(this).offset().top+objectHeight;
      
      /* Fade element in/out based on its visible percentage */
      if (objectTop < windowTop) {
        if (objectBottom > windowTop) {$(this).fadeTo(0,min+((max-min)*((objectBottom-windowTop)/objectHeight)));}
        else if ($(this).css("opacity")>=min+threshold || pageLoad) {$(this).fadeTo(0,min);}
      } else if ($(this).css("opacity")<=max-threshold || pageLoad) {$(this).fadeTo(0,max);}
    });
  } fade(true);
  $(window).scroll(function(){fade(false);}); //fade elements on scroll
});


// A function to handle fade-in properties of webpage
function fadeIn() {
  var urlCurrent = window.location.href;
  var urlReference = document.referrer;
  var title = document.title
  // all p-tags should be wrapped in div tag
  var titleFadeAttribute = {
    "Ira Horecka": ['h1.fade-in', 'h3.fade-in', 'li'],
    "About": ['h3.fade-in', 'div.fade-in'],
    "Coding Projects": ['h3.fade-in', 'li'],
    "Bike Gallery": ['h3.fade-in', 'li'],
    "projects": ['h3.fade-in', 'div.fade-in'],
    "bikes": ['h3.fade-in', 'div.fade-in']
  };

  // set default fade in attributes if none of special pages selected
  if (title in titleFadeAttribute) {
    htmlTags = titleFadeAttribute[title];
  } else if (urlCurrent.includes('projects')) {
    htmlTags = titleFadeAttribute["projects"];
  } else if (urlCurrent.includes('bikes')) {
    htmlTags = titleFadeAttribute["bikes"];
  } else {
    htmlTags = [];
  }

  // Don't fade-in h1 if previous pages were from my site
  if (title === "Ira Horecka") {
    if (urlReference.includes('localhost:5000')) {
      $('h1.fade-in').css('visibility','visible');
      htmlTags = ['h3.fade-in', 'li'];
    }
  }

  // Don't fade in h3 if previous pages were attributed with /projects/ 
  if (urlReference.includes('/projects/') && urlCurrent.includes('/projects')) {
    $('h3.fade-in').css('visibility','visible');
    htmlTags = htmlTags.slice(1,);
  } 

  // Don't fade in h3 if previous pages were attributed with /bikes/ 
  if (urlReference.includes('/bikes/') && urlCurrent.includes('/bikes')) {
    $('h3.fade-in').css('visibility','visible');
    htmlTags = htmlTags.slice(1,);
  } 

  // Allow fade-in with delay
  var msDelay = 0;
  var msFadeIn = 800;
  for (tag in htmlTags) {
      $(htmlTags[tag]).css('visibility','visible').hide().delay(msDelay).fadeIn(msFadeIn);
      msDelay += 300;
  }
}

