<html>
<head>
<title>AARTI CONTROL PANEL</title>
</head>
<body style="background-color:#BFEFFF;">
<?php
function checkSession(){
	if(isset($_SESSION["username"])){
		return true;
	} else{
		return false;
	}
}
if(checkSession()){
	header('Location: index.php');
}
?>
<div style="background-color:#000;color:#42C0FB;font-size:1.7em;padding-left:20px;padding-top:3px;padding-bottom:3px;">
<h1>AARTI</h1>
</div>
<br/>
<br/>
<center>
<div style="border-style:solid; border-color:black;">
<br/>
<br/>
<form action="generatesession.php" method="post">
<span style="font-size:2.3em;">Email ID: </span><input type="text" name="emailName" id="emailID" style="font-size:2.3em;width:30%;border-style:solid; border-color:black;"/>
<span style="font-size:2.3em;">Password: </span><input type="password" name="passwordName" id="passwordID" style="font-size:2.3em;width:30%;border-style:solid; border-color:black;"/>
<br/>
<div style="float:right;padding-right:10px;"><a style="font-size:2em;color:#800080" href="forgotpassword.php">Forgot Password</a></div>
<br/><br/>
<input type="submit" value="Log In"  style="font-size:2em;background-color:#EE82EE;color:#000;padding:15px 15px 15px 15px;box-shadow:2px 5px 5px rgba(0, 0, 0, .5);"/>
</form>
<br/>
</div>
</center>
<br/><br/>
<?php
$change=$_GET["change"];
$error=$_GET['error'];
if(isset($change) && $change=="0"){
	echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Please try again</div></center>");
} elseif(isset($change) && $change=="1"){
	echo("<center><div style='padding:20px;display:inline;font-size:2em;color:#008000;'>Your password has been changed successfully.</div></center>");
} elseif(isset($error)){
	switch($error){
		case "1":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Invalid Password</div></center>");
			break;
		case "2":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Email ID or Password is invalid</div></center>");
			break;
		case "3":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Error connecting to database</div></center>");
			break;
		case "4":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Invalid Input</div></center>");
			break;

}
}
?>
<br/><br/>
<center><h3 style="font-size:4.3em;">SIGN UP</h3></center>
<br/><br/>
<center>
<form action="signup.php" method="post">
<fieldset style="border-style:inset; border-color:black;">
<legend style="font-size:2em;">Enter Your Details</legend>
<br/><br/>
<input type="text" name="firstNameName" id="firstNameID" placeholder="First Name" style="font-size:2.3em;border-style:solid; border-color:black;width:45%"/>&nbsp&nbsp&nbsp&nbsp
<input type="text" name="lastNameName" id="lastNameID" placeholder="Last Name" style="font-size:2.3em;border-style:solid; border-color:black;width:45%"/>
<br/><br/>
<input type="text" name="nickNameName" id="nickNameID" placeholder="Nick Name (optional)" style="font-size:2.3em;border-style:solid; border-color:black;"/>
<br/><br/>
<span style="font-size:2.3em;">Male</span><input type="radio" name="genderName" id="genderID" value="male"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<span style="font-size:2.3em;">Female</span><input type="radio" name="genderName" id="genderID" value="female"/>
<br/><br/>
<input type="text" name="emailIDName" id="emailIDID" placeholder="Email ID" style="font-size:2.3em;border-style:solid; border-color:black;"/>
<br/><br/>
<input type="password" name="passwordName" id="passwordID" placeholder="Password" style="font-size:2.3em;border-style:solid; border-color:black;"/>
<br/><br/>
<input type="submit" value="Sign Up" style="font-size:2em;background-color:#EE82EE;color:#000;padding:15px 15px 15px 15px;box-shadow:2px 5px 5px rgba(0, 0, 0, .5);"/>
<br/><br/>
</fieldset>
</form>
<br/><br/>
<?php
$create=$_GET["create"];
$error=$_GET['error'];
if(isset($create) && $create=="0"){
	echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Something went wrong. Please try again</div></center>");
} elseif(isset($create) && $create=="1"){
	echo("<center><div style='padding:20px;display:inline;font-size:2em;color:#008000;'>Your account has been created successfully.</div></center>");
} elseif(isset($error)){
	switch($error){
		case "10":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Error connecting to database</div></center>");
			break;
		case "11":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Email ID already exists in the database</div></center>");
			break;
		case "12":
			echo("<center><div style='padding:20px;display:inline;font-size:2em;color:red;'>Please fill up all the required fields</div></center>");
	}
}
?>
</center>

</body>
</html>
