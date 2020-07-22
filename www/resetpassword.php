<?php
require_once('connection.php');
$password=$_POST['passwordName'];
$email=$_POST['hiddenEmail'];
$otp=$_POST['otpName'];
$encryptedPassword=password_hash($password,PASSWORD_DEFAULT);
$query="select otp,otptime from users where emailid='$email'";
$result=mysqli_query($con,$query);
if($result){
	$data=mysqli_fetch_row($result);
	$actualOTP=$data[0];
	if($otp==$actualOTP){
		$query="update users set password='$encryptedPassword' where emailid='$email'";
		$result=mysqli_query($con,$query);
		if($result){
			$var=null;
			$query="update users set otp='$var',otptime='$var'";
			mysqli_query($con,$query);
			header("Location: login.php?change=1");
		} else{
			header("Location: forgotpassword.php?error=1");
		}
	} else{
		header("Location: forgotpassword.php?change=0");
	}
} else{
	header("Location: forgotpassword.php?error=1");
}
/*
error=1 means database error
*/
?>
