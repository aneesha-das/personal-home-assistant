parent.window.onload=function(){
var imageArray=document.getElementsByTagName("img");
var hidden=document.getElementById("hiddenID");
console.log("hidden: "+hidden.value);
var i=1;
for(i=1;i<=parseInt(hidden.value);i++){
document.getElementById(i).onclick=highlight.bind(i)
}


function highlight(i) {
	id=parseInt(this);
	console.log(id);
	for(i=1;i<=parseInt(hidden.value);i++){
		document.getElementById(i).style.width=280;
		document.getElementById(i).style.height=280;
		document.getElementById(i).style.boxShadow="";
		document.getElementById(i).style.marginLeft="10px";
		document.getElementById(i).style.marginRight="0px";
	}
	element=document.getElementById(id);
	element.style.width=350;
	element.style.height=350;
	element.style.boxShadow="5px 10px 20px rgba(0, 0, 0, .5)";
	element.style.marginLeft="20px";
	element.style.marginRight="20px";

}
}

