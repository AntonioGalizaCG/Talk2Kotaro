//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

var toggle = 0;

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

var Button = document.getElementById("Button");

//add events to those 2 buttons
Button.addEventListener("click", Recording);

function Recording() {
	console.log("Button clicked");

	/*
		Simple constraints object, for more advanced audio features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/
    if (!toggle){
		toggle=1;
		var constraints = { audio: true, video:false }
		/*
			Disable the record button until we get a success or fail from getUserMedia() 
		*/

		Button.innerText="Stop";

		/*
			We're using the standard promise based getUserMedia() 
			https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
		*/

		navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
			console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

			/*
				create an audio context after getUserMedia is called
				sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
				the sampleRate defaults to the one set in your OS for your playback device

			*/
			audioContext = new AudioContext();

			//update the format 
			document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

			/*  assign to gumStream for later use  */
			gumStream = stream;
			
			/* use the stream */
			input = audioContext.createMediaStreamSource(stream);

			/* 
				Create the Recorder object and configure to record mono sound (1 channel)
				Recording 2 channels  will double the file size
			*/
			rec = new Recorder(input,{numChannels:1})

			//start the recording process
			rec.record()

			console.log("Recording started");

		}).catch(function(err) {
			toggle=0;
			//enable the record button if getUserMedia() fails
			Button.innerText = "Record";
		});
	}else{
		toggle=0;
		console.log("Button clicked");

		//disable the stop button, enable the record too allow for new recordings
		Button.innerText = "Record";
		rec.stop();
		//stop microphone access
		gumStream.getAudioTracks()[0].stop();
		//create the wav blob and pass it on to createDownloadLink
		rec.exportWAV(createDownloadLink);
	}
}

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
	xhr.open("POST","upload.php",true);
	xhr.send(fd);

}
