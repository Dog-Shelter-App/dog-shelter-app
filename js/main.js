// Initialize collapse button
$(".button-collapse").sideNav();
// Initialize collapsible (uncomment the line below if you use the dropdown variation)
//$('.collapsible').collapsible();

console.log("is gulp working?")


//define what we have ws = connection form = the form we use messageInput = where we input data
//messagesList = where messages are stored message = the message we currently have entered
var ws;
var form = document.getElementById('form');
var messageInput = document.getElementById('message');
var messagesList = document.getElementById('messages');
var socketStatus = document.getElementById('status');
var closeBtn = document.getElementById('close');

window.onload = function() {
// hack for localhost versus production. will fix better later.
var url = document.URL;

ws = new WebSocket("ws://localhost:8080/websocket");

console.log("heloo there");

// Triggers when message is sent
ws.onmessage = function(event) {
  console.log("new message attempt");
  // defines message as the contents of the message
  var message = event.data;
  // overwrites messages with new message that is received
  messagesList.innerHTML += '<tr class="sent"><td>Received:</td><td>' + message + '</td></tr>';
};
// Triggers on open websocket
ws.onopen = function(event) {
  console.log("new connection attempt");
  socketStatus.innerHTML = 'open';
  socketStatus.className = 'open';
};
//Triggers on close connection
ws.onclose = function(event) {
  console.log("new close attempt");
  socketStatus.innerHTML = 'closed';
  socketStatus.className = 'closed';
};
form.onsubmit = function(e) {

  // e.preventDefault();
  //define message field value
  var message = messageInput.value;
  // Send the message through the WebSocket.
  ws.send(message);
  // overwrites messages with new message that is sent
  messagesList.innerHTML += '<tr class="sent"><td>Sent:</td><td>' + message + '</td></tr>';
  // Clear out the message field.
  messageInput.value = '';
  //terminate function
  window.location.reload()
  return false;
};
// Close the WebSocket connection when the close button is clicked.
closeBtn.onclick = function(e) {
  console.log("new close queue attempt");
  //prevents page refresh
  e.preventDefault();
  // Close the WebSocket.
  ws.close();
  //terminate function
  return false;
  };
}

var urlForm = document.getElementById("urlForm");
var urlInput = document.getElementById("urlInput");

urlForm.onsubmit = function(e) {

  // e.preventDefault();
  //define message field value
  var url = urlInput.value;
  // Send the message through the WebSocket.

  var redirect = "/py-scraper?url=" + url

  window.location.replace(redirect)
  return false;
};

module.exports = tornadoPy;
