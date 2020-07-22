window.onload=function(){
	var canvas = document.getElementById("clock");
	var ctx = canvas.getContext("2d");
	var radius = canvas.height / 2;
	ctx.translate(radius, radius);
	var newrad=radius*0.95;
	radius = radius * 0.90;
	var datediv=document.getElementById("datediv");
	var time1=new Date(datediv.innerHTML);
	drawclock(time1);
	function drawclock(time){
/*	ctx.beginPath();
	ctx.arc(0,0,newrad,0,2*Math.PI);
	ctx.strokeStyle ="black";
	ctx.lineWidth=10;
	ctx.stroke();*/
	ctx.beginPath();
	ctx.arc(0, 0, radius, 0, 2*Math.PI);
	ctx.fillStyle ="#000";
	ctx.fill();
	var grad;
	grad=ctx.createRadialGradient(0,0,radius*0.95,0,0,radius*1.05);
	grad.addColorStop(0,"#000");
	grad.addColorStop(0.5,"#FFF");
	grad.addColorStop(1,"#000");
	ctx.strokeStyle=grad;
	ctx.lineWidth=radius*0.1;
	ctx.stroke();
	for(var i=1;i<=12;i++){
	var angle=i*Math.PI/6;
	ctx.textBaseline="middle";
	ctx.textAlign="center";
	ctx.font="50px Arial"
	ctx.rotate(angle);
	ctx.translate(0,-radius*0.80);
	ctx.fillStyle="white";
	ctx.rotate(-angle);
	ctx.fillText(i,0,0);
	ctx.rotate(angle);
	ctx.translate(0, radius*0.80);
	ctx.rotate(-angle);
	}
	time=new Date(time);
	var hour=time.getHours();
	var minute=time.getMinutes();
	var second=time.getSeconds();
	hour=(hour*Math.PI/6)+(minute*Math.PI/(6*60))+(second*Math.PI/(6*60*60));
	minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
	second=(second*Math.PI/30);
	drawhand(hour,25,radius*0.50);
	drawhand(minute,15,radius*0.75);
	drawhand(second,2,radius*0.80);
	ctx.beginPath();
	ctx.fillStyle="white"
	ctx.arc(0,0,10,0,2*Math.PI);
	ctx.fill();
	setTimeout(function(){drawclock(time.setSeconds(time.getSeconds()+1));},1000);
	}
//drawclock(time.setSeconds(time.getSeconds()+1));},1000
	function drawhand(pos,width,length){
	ctx.beginPath();
	ctx.strokeStyle="white";
	ctx.lineCap="round";
	ctx.lineWidth=width;
	ctx.moveTo(0,0);
	ctx.rotate(pos);
	ctx.lineTo(0,-length);
	ctx.stroke();
	ctx.rotate(-pos);
	}
}
