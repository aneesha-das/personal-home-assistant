window.onload=function(){
	var numberOfAnswers=document.getElementById("numberOfAnswersID");
	var setButton=document.getElementById("setButton");
	var answerDiv=document.getElementById("answerBox");
	var question=document.getElementById("questionID");
	setButton.onclick=function(){
		if(numberOfAnswers.value!="" && numberOfAnswers.value>0){
			answerDiv.innerHTML="";			
			var x=0;
			while(x<numberOfAnswers.value){
				var text=document.createElement("textarea");
				text.setAttribute("name","answer"+x);
				text.setAttribute("rows",2);
				text.setAttribute("cols",40);
				text.setAttribute("id","text"+x);
				answerDiv.appendChild(text);
				text.style.border="3px solid black";
				text.style.fontSize="3em";
				text.setAttribute("placeholder","Answer "+(x+1));
				var br=document.createElement("br");
				var br1=document.createElement("br");
				answerDiv.appendChild(br);
				answerDiv.appendChild(br1);
				x++;
			}
		submit=document.createElement("button");
		submit.setAttribute("id","submitID");
		submit.style.fontSize="3em";
		submit.style.border="3px solid black";
		submit.style.padding="25px 25px 25px 25px";
		submit.style.backgroundColor="#BFEFFF"
		submit.onclick=submitClick.bind();
		var textNode=document.createTextNode("Save");
		submit.appendChild(textNode);
		answerDiv.appendChild(submit);
		}
	return false;
	}
	function submitClick(){
	var link="answer.php/?question="+question.value;
	var answerArray=answerDiv.getElementsByTagName("textarea");
	var i=1;
	var j=0;	
	var n=answerArray.length;
	while(j<n){
		if(answerArray[j].value!=""){
			link=link+"&response"+i+"="+answerArray[j].value;
			i++;
		}	
		j++;
	}
	if(i>1){
		$.get(link+"&total="+--i, function(data, status){
						if(data!=""){
							question.value=data;
							alert("Response added successfully");
						} else{
							question.value="Nothing To Show";
						}7
						answerDiv.innerHTML="";
					});
	}
	return false;
	}
}
