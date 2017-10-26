// // user type
//
// // monitor user_type input value
// // $( "#dogForm" ).submit(function( event ) {
// //   var date = $("#date_found");
// //   var files = $("my_File");
// //
// //   $("input").removeClass("invalid")
// //
// //   if(date.val() == "") {
// //     let slide = date.data("section");
// //     $("#date_found").addClass("invalid")
// //     $("#formCarousel").carousel(1);
// //     return false
// //   }
// //
// //   if(document.getElementById("my_File").files.length == 0 ){
// //     let slide = files.data("section");
// //     $("#file_label").addClass("invalid")
// //     $("#formCarousel").carousel(0);
// //     return false
// // }
// // });
//
//
// // Dog Form Logic
//
// $('#formCarousel').on('slid.bs.carousel', function (ev) {
//   var id = ev.relatedTarget.id;
//   switch (id) {
//     case "1":
//       $('#buttonLeft').hide();
//       $("#buttonRight").show();
//       $("#slide1").addClass("active");
//       $("#slide2").removeClass("active");
//       $("#slide3").removeClass("active");
//       break;
//     case "2":
//       // do something the id is 2
//       $('#buttonLeft').show();
//       $('#buttonRight').show();
//       $("#slide1").removeClass("active");
//       $("#slide2").addClass("active");
//       $("#slide3").removeClass("active");
//       break;
//     case "3":
//       // do something the id is 3
//       $("#buttonRight").hide();
//       $("#buttonLeft").show();
//       $("#slide1").removeClass("active");
//       $("#slide2").removeClass("active");
//       $("#slide3").addClass("active");
//       break;
//     default:
//       //the id is none of the above
//   }
// })
//
// // date, image,
//
// // Sticky Plugin
//
// $(document).ready(function () {
//   var top = $('.sticky-scroll-box').offset().top;
//   $(window).scroll(function (event) {
//     let width = $( window ).width();
//     var y = $(this).scrollTop();
//     if (y >= top && width > 800)
//       $('.sticky-scroll-box').addClass('fixed');
//     else
//       $('.sticky-scroll-box').removeClass('fixed');
//     // $('.sticky-scroll-box').width($('.sticky-scroll-box').parent().width());
//   });
// });
//
//
//
// $(document).ready(function () {
// //DOG-FORM Button trigger if COLLAR_YES
// $('#collar_color').hide();
// $('#collarYes').click(function(event){
//   $('#collar_color').slideToggle();
// })
// $('#collarNo').click(function(event){
//   $('#collar_color').hide();
// })
//
// var range = 100;
//
// $(window).on('scroll', function () {
//   var scrollTop = $(this).scrollTop(),
//       height = $('#header').outerHeight(),
//       offset = height/0.5,
//       calc = 1 - (scrollTop - offset + range) / range;
//   $('#header').css({ 'opacity': calc });
//   if (calc > '1') {
//     $('#header').css({ 'opacity': 1 });
//   } else if ( calc < '0' ) {
//     $('#header').css({ 'opacity': 0 });
//   }
// });
//
// });
// //////////////////////////
// //END JULIE
//
// //////////////////// Soft Query for Age and Name //////////////////////////
// // $(document).ready(function () {
// //   $("#age_list").hide();
// //   $('/querybar').load()
//
//
//
// // }
//
// //////////////////// End Soft Query ///////////////////////////////////////
//
//
// //define what we have ws = connection form = the form we use messageInput = where we input data
// //messagesList = where messages are stored message = the message we currently have entered
// $(document).ready (function() {
//   var ws;
//   var form = document.getElementById('form');
//   var messageInput = document.getElementById('message');
//   var messagesList = document.getElementById('messages');
//   var socketStatus = document.getElementById('status');
//   var closeBtn = document.getElementById('close');
//
//   window.onload = function() {
//   // hack for localhost versus production. will fix better later.
//   var url = document.URL;
//
//   ws = new WebSocket("ws://localhost:8080/websocket");
//
//   console.log("heloo there");
//
//   // Triggers when message is sent
//   ws.onmessage = function(event) {
//     console.log("new message attempt");
//     // defines message as the contents of the message
//     var message = event.data;
//     // overwrites messages with new message that is received
//     messagesList.innerHTML += '<tr class="sent"><td>Received:</td><td>' + message + '</td></tr>';
//   };
//   // Triggers on open websocket
//   ws.onopen = function(event) {
//     console.log("new connection attempt");
//     socketStatus.innerHTML = 'open';
//     socketStatus.className = 'open';
//   };
//   //Triggers on close connection
//   ws.onclose = function(event) {
//     console.log("new close attempt");
//     socketStatus.innerHTML = 'closed';
//     socketStatus.className = 'closed';
//   };
//   form.onsubmit = function(e) {
//
//     // e.preventDefault();
//     //define message field value
//     var message = messageInput.value;
//     // Send the message through the WebSocket.
//     ws.send(message);
//     // overwrites messages with new message that is sent
//     messagesList.innerHTML += '<tr class="sent"><td>Sent:</td><td>' + message + '</td></tr>';
//     // Clear out the message field.
//     messageInput.value = '';
//     //terminate function
//     window.location.reload()
//     return false;
//   };
//   // Close the WebSocket connection when the close button is clicked.
//   closeBtn.onclick = function(e) {
//     console.log("new close queue attempt");
//     //prevents page refresh
//     e.preventDefault();
//     // Close the WebSocket.
//     ws.close();
//     //terminate function
//     return false;
//     };
//   }
//
//   var urlForm = document.getElementById("urlForm");
//   var urlInput = document.getElementById("urlInput");
//
//   urlForm.onsubmit = function(e) {
//
//     // e.preventDefault();
//     //define message field value
//     var url = urlInput.value;
//     // Send the message through the WebSocket.
//
//     var redirect = "/py-scraper?url=" + url
//
//     window.location.replace(redirect)
//     return false;
//   };
//
//   // module.exports = tornadoPy;
// });
