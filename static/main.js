//var socket = new WebSocket('ws://192.168.1.221:8080/ws/updateNotif/');

var ws_url = 'ws://' + window.location.host + '/ws/updateNotif/';
var socket = new WebSocket(ws_url);

socket.onmessage = function(e){
	console.log("test");
	var djangoData = JSON.parse(e.data);
	console.log("test");
	console.log(djangoData);
	
	var x = document.getElementById('updateNotif');

	document.getElementById('updateNotif').innerHTML = '<div class="alert"><span class="closebtn" onclick="this.parentNode.remove();">&times;</span>New Post Reload Page</div>';
}

function NewPost() {
	socket.send(JSON.stringify({'value': "New Post"}));
}
