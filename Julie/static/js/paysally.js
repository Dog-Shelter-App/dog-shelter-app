$(document).ready(function () {


  $('#section1').hide();
  $('#section2').hide();
  $('#section3').hide();
$('#section-header1').click(function(event){
  $('#section1').slideToggle()
  })
  $('#section-header2').click(function(event){
    $('#section2').slideToggle()
    })
    $('#section-header3').click(function(event){
      $('#section3').slideToggle()
      })
});

var range = 100;

$(window).on('scroll', function () {
  var scrollTop = $(this).scrollTop(),
      height = $('#header').outerHeight(),
      offset = height/0.5,
      calc = 1 - (scrollTop - offset + range) / range;
  $('#header').css({ 'opacity': calc });
  if (calc > '1') {
    $('#header').css({ 'opacity': 1 });
  } else if ( calc < '0' ) {
    $('#header').css({ 'opacity': 0 });
  }
});
