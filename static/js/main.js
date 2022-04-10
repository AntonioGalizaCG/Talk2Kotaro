$(document).ready(function(){
  let namespace = "/test";
  let video = document.querySelector("#videoElement");
  let canvas = document.querySelector("#canvasElement");
  let ctx = canvas.getContext('2d');
  var photo = document.getElementById('photo');
  var localMediaStream = null;
  let formu = document.getElementById('canca');
  var constraints = {
    video: {
      width: { min: 640 },
      height: { min: 480 }
    }
  };

  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    video.srcObject = stream;
    localMediaStream = stream;

    setInterval(function () {
 if (!localMediaStream) {
      return;
    }
    ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight, 0, 0, 300, 150);
    let dataURL = canvas.toDataURL('image/jpeg');
    //var img = new Image();
    //img.src = dataURL//data.image_data
    photo.setAttribute('src', dataURL);
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "/rec", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify(dataURL));
	}, 50);
  }).catch(function(error) {
    console.log(error);
  });
});

