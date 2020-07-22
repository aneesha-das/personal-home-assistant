<?php
require_once('connection.php');
require_once('authenticate.php');
$email=$_POST['gIDName'];
$password=$_POST['gIDPasswordName'];
session_start();
$userID=$_SESSION["username"];
if($email!="" && $password!=""){
	$query="update users set gmail='$email',gmailpassword='$password' where emailid='$userID';";
	if(mysqli_query($con,$query)){
		header('Location: index.php?configure=1');
	} else{
		header('Location: settings.php?configure=0');
	}
}
?>
