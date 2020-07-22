<?php
/*
error 10 means database error
error 11 means username exists
error 12 means incomplete form
*/
error_reporting(E_ALL);
ini_set('display_errors', 1);
require_once('connection.php');
$firstName=$_POST['firstNameName'];
$lastName=$_POST['lastNameName'];
$email=$_POST['emailIDName'];
$gender=$_POST['genderName'];
$password=$_POST['passwordName'];
$nickname=$_POST['nickNameName'];
$encryptedPassword=password_hash($password, PASSWORD_DEFAULT);
if($firstName!=""&&$lastName!=""&&$email!=""&&$gender!=""&&$password!=""){
	$query="select count(*) from users where emailid='$email'";
	$result=mysqli_query($con,$query);
	if($result){
		if($data=mysqli_fetch_row($result)){
			if($data[0]==1){
				header("Location: login.php?error=11");
			} else{
				$query="insert into users (emailid,firstname,lastname,gender,nickname,password) values('$email','$firstName','$lastName','$gender','$nickname','$encryptedPassword')";
				$result=mysqli_query($con,$query);
				if($result){
					header('Location: login.php?create=1');
				} else{
					header('Location: login.php?create=0');
				}
			}
		} else{
			header("Location: login.php?error=10");
		}
	}else{
		header("Location: login.php?error=10");
}
}else{
	header("Location: login.php?error=12");
}





?>
