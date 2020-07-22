<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</head>
<body style="background-color:#000;">
<?php
require_once("authenticate.php");
?>
<center>
<div style="margin-top:30%;">
<img id="upID" src="/images/arrow_up.png" height=250 width=250 onclick="javascript:control(1);return false;"/>
<br/>
<img id="leftID" src="/images/arrow_left.png" height=250 width=250 onclick="control(2);return false;"/>
<img id="stopID" src="/images/stop.png" height=250 width=250 onclick="control(0);return false;"/>
<img id="rightID" src="/images/arrow_right.png" height=250 width=250 onclick="control(3);return false;"/>
<br/>
<img id="downID" src="/images/arrow_down.png" height=250 width=250 onclick="control(4);return false;"/>
</div>
</center>
<script>
var upButton=document.getElementById("upID");
var leftButton=document.getElementById("leftID");
var rightButton=document.getElementById("rightID");
var downButton=document.getElementById("downID");
var stopButton=document.getElementById("stopD");
var buttonPressed="stop";
$(window).on("beforeunload",function(e){
if(e.originalEvent){
buttonPressed="stop";
sendData();
}
else{}
$(this).trigger('beforeunload');
});

function sendData(){
	$.post("/move.php",{direction : buttonPressed},function(data){});
}
function control(v){
	if(v==0){
		buttonPressed="stop";
		upButton.setAttribute("src","/images/arrow_up.png");
		downButton.setAttribute("src","/images/arrow_down.png");
		leftButton.setAttribute("src","/images/arrow_left.png");
		rightButton.setAttribute("src","/images/arrow_right.png");
	}
	else if(v==1){
		upButton.setAttribute("src","/images/highlighted_up.png");
		downButton.setAttribute("src","/images/arrow_down.png");
		leftButton.setAttribute("src","/images/arrow_left.png");
		rightButton.setAttribute("src","/images/arrow_right.png");
		buttonPressed="front";
	} else if(v==2){
		upButton.setAttribute("src","/images/arrow_up.png");
		downButton.setAttribute("src","/images/arrow_down.png");
		leftButton.setAttribute("src","/images/highlighted_left.png");
		rightButton.setAttribute("src","/images/arrow_right.png");
		buttonPressed="left";
	} else if(v==3){
		upButton.setAttribute("src","/images/arrow_up.png");
		downButton.setAttribute("src","/images/arrow_down.png");
		leftButton.setAttribute("src","/images/arrow_left.png");
		rightButton.setAttribute("src","/images/highlighted_right.png");
		buttonPressed="right";
	} else if(v==4){
		buttonPressed="back";
		upButton.setAttribute("src","/images/arrow_up.png");
		downButton.setAttribute("src","/images/highlighted_down.png");
		leftButton.setAttribute("src","/images/arrow_left.png");
		rightButton.setAttribute("src","/images/arrow_right.png");
	}
	sendData();
}

</script>
</body>
</html>



