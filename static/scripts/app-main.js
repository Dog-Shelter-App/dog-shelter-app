

$( "#dogForm" ).submit(function( event ) {
  var date = $("#date_found");
  var files = $("my_File");

  $("input").removeClass("invalid")

  if(date.val() == "") {
    let slide = date.data("section");
    $("#date_found").addClass("invalid")
    $("#formCarousel").carousel(1);
    return false
  }

  if(document.getElementById("my_File").files.length == 0 ){
    let slide = files.data("section");
    $("#file_label").addClass("invalid")
    $("#formCarousel").carousel(0);
    return false
}
});


// Dog Form Logic
$('#formCarousel').on('slid.bs.carousel', function (ev) {
  var id = ev.relatedTarget.id;
  switch (id) {
    case "1":
      $('#buttonLeft').hide();
      $("#buttonRight").show();
      $("#slide1").addClass("active");
      $("#slide2").removeClass("active");
      $("#slide3").removeClass("active");
      break;
    case "2":
      // do something the id is 2
      $('#buttonLeft').show();
      $('#buttonRight').show();
      $("#slide1").removeClass("active");
      $("#slide2").addClass("active");
      $("#slide3").removeClass("active");
      break;
    case "3":
      // do something the id is 3
      $("#buttonRight").hide();
      $("#buttonLeft").show();
      $("#slide1").removeClass("active");
      $("#slide2").removeClass("active");
      $("#slide3").addClass("active");
      break;
    default:
      //the id is none of the above
  }
})

// // Sticky Plugin
$(document).ready(function () {
  var top = $('.sticky-scroll-box').offset().top;
  $(window).scroll(function (event) {
    let width = $( window ).width();
    var y = $(this).scrollTop();
    if (y >= top && width > 800)
      $('.sticky-scroll-box').addClass('fixed');
    else
      $('.sticky-scroll-box').removeClass('fixed');
    // $('.sticky-scroll-box').width($('.sticky-scroll-box').parent().width());
  });
});
