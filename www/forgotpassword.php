<html>
<head>
<title>Forgot Password</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
</head>
<body>
<center>
<?php
$change=$_GET["change"];
if(isset($change) && $change=="0"){
	echo("<div style='padding:20px;display:inline;font-size:2em;color:red;'>Incorrect OTP. Please try again with new OTP.</div>");
}
?>
<div style="margin-top:45%;">
<form id="form1ID">
<fieldset style="border:3px inset black;background-color:#BFEFFF;">
<legend style="font-size:1.7em;">Enter an email address where your one-time password will be sent</legend>
<br/>
<input type="email" id="emailIDID"name="emailName" placeholder="Enter Email ID" style="font-size:2.5em;"/>&nbsp
<input type="submit" id="emailSendID" name="submit" value="Send OTP" style="font-size:2.5em;"/><br/><br/>
</fieldset>
</form>
<form id="form2ID" action="resetpassword.php" method=POST>
<fieldset style="border:3px inset black;background-color:#BFEFFF;">
<legend style="font-size:2.5em;">Reset Password</legend>
<br/>
<input type="password" id="passwordID" name="passwordName" placeholder="Enter New Password" style="font-size:2.5em;"/><br/><br/>
<input type="password" id="confirmPasswordID" name="confirmPasswordName" placeholder="Confirm Password" style="font-size:2.5em;"/><br/><br/>
<input type="password" id="otpID" name="otpName" placeholder="Enter OTP" style="font-size:2.5em; width:20%;"/><br/><br/>
<input type="hidden" name="hiddenEmail" id="hiddenID"/>
<input type="submit" id="resetID" name="submit" value="Reset Password" style="font-size:2.5em;"/><br/><br/>
<span style="font-size:2.5em;color:red">The OTP will expire in 10 minutes</span><br/>
</fieldset>
</form>
</div>
</center>
<script>
window.onload=function(){
var form1=document.getElementById("form1ID");
var form2=document.getElementById("form2ID");
var email=document.getElementById("emailIDID");
var emailButton=document.getElementById("emailSendID");
var password=document.getElementById("passwordID"); 
var confirmPassword=document.getElementById("confirmPasswordID");
var otp=document.getElementById("otpID");
var resetButton=document.getElementById("resetID");
var hidden=document.getElementById("hiddenID");

form2.style.display="none";
emailButton.onclick=function(){
	if(email.value!=""){
		hidden.value=email.value;
		$.post("/sendotp.php",{email: email.value},function(data){});
		form1.style.display="none";
		form2.style.display="block";
		setTimeout(function(){location.reload()},10*60*1000);	
	}
	return false;
}

resetButton.onclick=function(){
	if(password.value!="" && confirmPassword.value!="" && otp.value!=""){
		if(password.value==confirmpassword.value){
			return true;
		} else{
			alert("Passwords Do Not Match");
			return false;
		}
	} else{
		alert("Please Fill Up The Required Fields");
		return false;
	}
}

}
</script>
</body>
</html>

