<?php

require_once('connection.php');
$email=$_POST['email'];
$query="select count(*) from users where emailid='$email'";
$result=mysqli_query($con,$query);
if($result){
	$data=mysqli_fetch_row($result);
	if($data[0]==1){
		$shell=escapeshellcmd("python3 /home/pi/Desktop/nanpy/Final/sendotp.py ".$email);
		$result=shell_exec($shell);
	} else{
		echo("No match found");
	}
} else{
	echo("Database error");
}
?>
