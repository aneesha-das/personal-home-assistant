window.onload=function(){
	var url=window.location.href;
	var home=window.frames['menuName'].document.getElementById("homeButtonID");
	var voiceInput=window.frames['menuName'].document.getElementById("voiceInputButtonID");
	var contacts=window.frames['menuName'].document.getElementById("contactsButtonID");
	var aartiRemote=window.frames['menuName'].document.getElementById("aartiRemoteButtonID");
	var photoStudio=window.frames['menuName'].document.getElementById("photoStudioButtonID");
	var surveillance=window.frames['menuName'].document.getElementById("surveillanceButtonID");
	if(url.search("/home.php")>=1){
		home.style.backgroundColor="#EE82EE";
		home.style.color="#FFF";

		voiceInput.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		contacts.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		aartiRemote.style.backgroundColor="#BFEFFF";
		aartiRemote.style.color="#000";

		photoStudio.style.backgroundColor="#BFEFFF";
		photoStudio.style.color="#000";
		
		surveillance.style.backgroundColor="#BFEFFF";
		surveillance.style.color="#000";
	} else if(url.search("/voiceinput.php")>=1){
		voiceInput.style.backgroundColor="#EE82EE";
		voiceInput.style.color="#FFF";

		home.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		contacts.style.backgroundColor="#BFEFFF";
		contacts.style.color="#000";

		aartiRemote.style.backgroundColor="#BFEFFF";
		aartiRemote.style.color="#000";

		photoStudio.style.backgroundColor="#BFEFFF";
		photoStudio.style.color="#000";
		
		surveillance.style.backgroundColor="#BFEFFF";
		surveillance.style.color="#000";
	} else if(url.search("/contacts.php")>=1){
		contacts.style.backgroundColor="#EE82EE";
		contacts.style.color="#FFF";

		voiceInput.style.backgroundColor="#BFEFFF";
		voiceInput.style.color="#000";

		home.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		aartiRemote.style.backgroundColor="#BFEFFF";
		aartiRemote.style.color="#000";

		photoStudio.style.backgroundColor="#BFEFFF";
		photoStudio.style.color="#000";
		
		surveillance.style.backgroundColor="#BFEFFF";
		surveillance.style.color="#000";
	} else if(url.search("/photostudio.php")>=1){
		photoStudio.style.backgroundColor="#EE82EE";
		photoStudio.style.color="#FFF";

		voiceInput.style.backgroundColor="#BFEFFF";
		voiceInput.style.color="#000";

		contacts.style.backgroundColor="#BFEFFF";
		contacts.style.color="#000";

		aartiRemote.style.backgroundColor="#BFEFFF";
		aartiRemote.style.color="#000";

		home.style.backgroundColor="#BFEFFF";
		home.style.color="#000";
		
		surveillance.style.backgroundColor="#BFEFFF";
		surveillance.style.color="#000";
	} else if(url.search("/surveillance.php")>=1){
		surveillance.style.backgroundColor="#EE82EE";
		surveillance.style.color="#FFF";

		home.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		contacts.style.backgroundColor="#BFEFFF";
		contacts.style.color="#000";

		aartiRemote.style.backgroundColor="#BFEFFF";
		aartiRemote.style.color="#000";

		photoStudio.style.backgroundColor="#BFEFFF";
		photoStudio.style.color="#000";
		
		voiceInput.style.backgroundColor="#BFEFFF";
		voiceInput.style.color="#000";
	}  else if(url.search("/movebot.php")>=1){
		aartiRemote.style.backgroundColor="#EE82EE";
		aartiRemote.style.color="#FFF";

		home.style.backgroundColor="#BFEFFF";
		home.style.color="#000";

		contacts.style.backgroundColor="#BFEFFF";
		contacts.style.color="#000";

		surveillance.style.backgroundColor="#BFEFFF";
		surveillance.style.color="#000";

		photoStudio.style.backgroundColor="#BFEFFF";
		photoStudio.style.color="#000";
		
		voiceInput.style.backgroundColor="#BFEFFF";
		voiceInput.style.color="#000";
	}
}
