$(document).ready(function(){
  let video = document.querySelector("#videoElement");
  var canvas = document.querySelector("#canvasElement");
  var ctx = canvas.getContext('2d');
  var photo = document.getElementById('photo');
  var localMediaStream = null;
  let formu = document.getElementById('canca');
  var stop_recording = false;
  var oneShot = false;
  var counter = false;

  var constraints = {
    video: {
      width: { min: 640 },
      height: { min: 480 }
    }
  };

  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    video.srcObject = stream;
    localMediaStream = stream;

var buttonSpeak = document.getElementById("speak");
var audio = new Audio();
var reccer = false ;
var toggle = false;
var buttonLogOut = document.getElementById("logout");
var buttonDeleteData = document.getElementById("DD");

URL = window.URL || window.webkitURL;
var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

buttonSpeak.onclick = function() {
	if (!reccer){
		if (toggle){
			//buttonSpeak.innerText="Listen";
      document.getElementById("ListenImage").style.display = "none";
      document.getElementById("SpeakImage").style.display = "block";
			rec.stop();
			//stop microphone access
			gumStream.getAudioTracks()[0].stop();
			//create the wav blob and pass it on to createDownloadLink
			rec.exportWAV(createDownloadLink);
      //////////////////////////////////////////////////////////////////
      oneShot = true;
      counter = false;
      //////////////////////////////////////////////////////////////////
      // audio.play();
			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function() {
				if (xhr.readyState == 4 && xhr.status == 200) {
					// alert(xhr.responseText);
				}
			}
			xhr.open("POST", "rec_status");
			xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
			xhr.send(JSON.stringify({ status: "true" }));
			reccer = true;
      stop_recording = false;
		}else{
			audio = new Audio('wav');
			var constraints = { audio: true, video:false }
			//buttonSpeak.innerText="Speak ";
      document.getElementById("SpeakImage").style.display = "block";
      document.getElementById("ListenImage").style.display = "none";
			navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
				console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
				audioContext = new AudioContext();
				//update the format
				gumStream = stream;
				input = audioContext.createMediaStreamSource(stream);
				rec = new Recorder(input,{numChannels:1});
				rec.record();
				console.log("Recording started");
			})
		}
		toggle = !toggle;
	}
};

var vis = false;
var boca = false;
function Blinker(){
	var roll = Math.floor(Math.random() * 50);
	if (roll==0){
		vis = !vis;
	}else{
		if(vis){
			if (boca){
				document.getElementById("avatar0").style.display = "none";
				document.getElementById("avatar1").style.display = "block";
				document.getElementById("avatar2").style.display = "none";
				document.getElementById("avatar3").style.display = "none";
			}else{
				document.getElementById("avatar0").style.display = "none";
				document.getElementById("avatar1").style.display = "none";
				document.getElementById("avatar2").style.display = "block";
				document.getElementById("avatar3").style.display = "none";
			}
		}else{
			if (boca){
				document.getElementById("avatar0").style.display = "none";
				document.getElementById("avatar1").style.display = "none";
				document.getElementById("avatar2").style.display = "none";
				document.getElementById("avatar3").style.display = "block";
			}else{
				document.getElementById("avatar0").style.display = "block";
				document.getElementById("avatar1").style.display = "none";
				document.getElementById("avatar2").style.display = "none";
				document.getElementById("avatar3").style.display = "none";
			}
		}
	}
};
function Mouther(){
	if(!audio.paused){
		boca = !boca;
    buttonSpeak.disabled=true;
    document.getElementById("ListenImage").style.display = "none";
    document.getElementById("SpeakImage").style.display = "none";
    document.getElementById("SpeakDisImage").style.display = "block";
    //buttonSpeak.style.backgroundColor = '#b0b0b0'
	}else{
			boca = false;
      buttonSpeak.disabled=false;
      //buttonSpeak.style.backgroundColor = '#00cccc'
			if (reccer && stop_recording){
        document.getElementById("SpeakImage").style.display = "none";
        document.getElementById("SpeakDisImage").style.display = "none";
        document.getElementById("ListenImage").style.display = "block";
				reccer = false;
				var xhr = new XMLHttpRequest();
				xhr.onreadystatechange = function() {
					if (xhr.readyState == 4 && xhr.status == 200) {
						// alert(xhr.responseText);
					}
				}
				xhr.open("POST", "rec_status");
				xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
				xhr.send(JSON.stringify({ status: "false" }));
			}
	}
}

setInterval(Blinker, 50);
setInterval(Mouther, 200);

var frequency = 300;

setInterval(function () {
 if (!localMediaStream) {
      return;
    }
		ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight, 0, 0, 300, 150);
		let dataURL = canvas.toDataURL('image/jpeg');
		photo.setAttribute('src', dataURL);
    if (reccer){
    frequency = 50;
    }
    if (oneShot && counter){
      ctx.fillRect(0, 0, 480, 640);
  		let dataURL = canvas.toDataURL('image/jpeg');
      var xhr = new XMLHttpRequest();
  		xhr.open("POST", "rec");
  		xhr.setRequestHeader('Content-Type', 'application/json');
  		xhr.send(JSON.stringify(dataURL));
      oneShot = false;
      counter = false;
      audio.play();
      stop_recording = true;
    }else{
      if (!counter){counter = true;}
  		var xhr = new XMLHttpRequest();
  		xhr.open("POST", "rec");
  		xhr.setRequestHeader('Content-Type', 'application/json');
  		xhr.send(JSON.stringify(dataURL));}}, frequency);
  }).catch(function(error) {
    console.log(error);
  });
});

function createDownloadLink(blob) {

	var url = URL.createObjectURL(blob);
	var au = document.createElement('audio');
	//name of .wav file to use during upload and download (without extendion)
	var filename = new Date().toISOString();
	au.controls = true;
	au.src = url;

	var xhr=new XMLHttpRequest();
	xhr.onload=function(e) {
		if(this.readyState === 4) {
			console.log("Server returned: ",e.target.responseText);
		}
	};
	var fd=new FormData();
	fd.append("audio_data",blob, filename);
	xhr.open("POST","rec_voice",true);
	xhr.send(fd);
}
