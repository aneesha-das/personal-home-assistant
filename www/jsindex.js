"use strict"
function prepareEventHandlers(){
var r=document.getElementById('resultID');
var b=document.getElementById('micID');
var ip="192.168.1.102";
var response=document.getElementById("responseID");
var interval=null;

interval=setInterval(function(){$.get("getresponse.php", function(data, status){
					if(data!="" && data!="Hello! I am ready to talk."){
						response.innerHTML=data;
						clearInterval(interval);
					} else if(data!=""){
						clearInterval(interval);
					}
			        })},1000);

b.onclick=function(){
if('webkitSpeechRecognition' in window){
	var speechRecognizer=new webkitSpeechRecognition();
	speechRecognizer.continuous=false;
	speechRecognizer.interimResults=true;
	speechRecognizer.lang="en-IN";
	speechRecognizer.start();
	var finalTranscripts='';
	speechRecognizer.onresult=function(event){
	var intermTranscripts='';
	for(var i=event.resultIndex;i<event.results.length;i++){
	var transcript=event.results[i][0].transcript;
	transcript.replace("\n","<br>");
	if(event.results[i].isFinal){
		finalTranscripts+=transcript;
	}else{
		intermTranscripts+=transcript;
	}
}
r.innerHTML=finalTranscripts + '<span style="color: #999">'+intermTranscripts+'</span>';
speechRecognizer.onend=function(){
if(finalTranscripts!=""){
	$.post("/senddata.php",{question: finalTranscripts},function(data){});
	interval=setInterval(function(){$.get("getresponse.php", function(data, status){
					if(data!=""){
						response.innerHTML=data;
						clearInterval(interval);
					}
			        })},1000);

}
}
};

speechRecognizer.onerror=function(event){

};

} else{
r.innerHTML="Browser Not Supported";
}
}
}
window.onload=function(){
prepareEventHandlers();
}

